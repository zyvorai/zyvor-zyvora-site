#!/usr/bin/env node
// Checks the built site in real Chrome: no console errors, every image loads, every in-page link and asset resolves,
// axe-core finds no serious/critical issues in either theme, nothing overflows at phone width, content is visible with
// reduced motion, and the gallery controls work. Screenshots go to <shotsDir> (default: a temp dir) for a human to look at.
//   node marketing/site-check.mjs [siteDir] [shotsDir]
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const site = process.argv[2] ?? join(here, "dist", "site");
const shots = process.argv[3] ?? join(tmpdir(), "zyvora-site-shots");
mkdirSync(shots, { recursive: true });
// Playwright and axe come from apps/web in the product repo, or from the nearest package.json when this file is copied into the site repo.
const req = createRequire(existsSync(join(here, "..", "apps", "web", "package.json")) ? join(here, "..", "apps", "web", "package.json") : join(process.cwd(), "package.json"));
const LAUNCH = process.env.CI ? {} : { channel: "chrome" }; // CI uses the Chromium that `playwright install` fetched
const { chromium } = req("@playwright/test");
const AxeBuilder = req("@axe-core/playwright").default ?? req("@axe-core/playwright");

const TYPES = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".xml": "application/xml", ".txt": "text/plain" };
const server = createServer((rq, rs) => {
  const path = normalize(decodeURIComponent(rq.url.split("?")[0])).replace(/^(\.\.[/\\])+/, "");
  let file = join(site, path === "/" ? "index.html" : path);
  if (existsSync(file) && statSync(file).isDirectory()) file = join(file, "index.html");
  if (!existsSync(file)) file = join(site, "404.html");
  rs.writeHead(file.endsWith("404.html") && path !== "/404.html" ? 404 : 200, { "content-type": TYPES[extname(file)] ?? "application/octet-stream" });
  rs.end(readFileSync(file));
});
await new Promise((r) => server.listen(0, "127.0.0.1", r));
const base = `http://127.0.0.1:${server.address().port}`;

const failures = [];
const check = (ok, msg) => { if (!ok) failures.push(msg); };
const browser = await chromium.launch(LAUNCH);
try {
  for (const scheme of ["light", "dark"]) {
    const ctx = await browser.newContext({ colorScheme: scheme, viewport: { width: 1440, height: 900 } });
    const page = await ctx.newPage();
    const bad = [];
    page.on("console", (m) => { if (m.type() === "error") bad.push(m.text()); });
    page.on("pageerror", (e) => bad.push(String(e)));
    page.on("response", (r) => { if (r.status() >= 400) bad.push(`${r.status()} ${r.url()}`); });
    await page.goto(base + "/", { waitUntil: "networkidle" });
    check(await page.evaluate(() => document.documentElement.dataset.theme) === scheme, `theme follows the ${scheme} preference`);
    // reveal content without scrolling every section: scroll through once
    await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); } window.scrollTo(0, 0); });
    await page.evaluate(() => { document.querySelectorAll('img[loading=lazy]').forEach((i) => { i.loading = 'eager'; }); });
    await page.waitForFunction(() => [...document.images].filter((i) => i.offsetParent !== null).every((i) => i.complete), null, { timeout: 10000 }).catch(() => undefined);
    await page.waitForTimeout(500);

    // images: every visible img loaded
    const imgs = await page.evaluate(() => [...document.images].filter((i) => i.offsetParent !== null).map((i) => ({ src: i.currentSrc || i.src, ok: i.complete && i.naturalWidth > 0 })));
    for (const i of imgs) check(i.ok, `image did not load: ${i.src}`);
    // in-page anchors resolve
    const anchors = await page.evaluate(() => [...document.querySelectorAll('a[href^="#"]')].map((a) => a.getAttribute("href")).filter((h) => h.length > 1));
    for (const h of new Set(anchors)) check(await page.locator(h).count() === 1, `anchor target missing: ${h}`);
    // axe
    const r = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
    for (const v of r.violations.filter((x) => x.impact === "serious" || x.impact === "critical")) check(false, `axe (${scheme}) ${v.id}: ${v.nodes.slice(0, 2).map((n) => n.target.join(" ")).join(" | ")}`);
    // gallery
    await page.getByRole("radio", { name: "Lab", exact: true }).click();
    await page.waitForFunction(() => document.getElementById("shot").getAttribute("src").includes("-lab"), null, { timeout: 5000 }).catch(() => check(false, "gallery did not switch to Lab"));
    await page.getByRole("radio", { name: "Dashboard", exact: true }).click();
    // clips stay still until played
    check(await page.locator(".clip img[src$=\".gif\"]").count() === 0, "a clip autoplays");
    await page.locator(".clip .play").first().click();
    check(await page.locator(".clip img[src$=\".gif\"]").count() === 1, "play did not start the clip");
    await page.screenshot({ path: join(shots, `desktop-${scheme}.png`), fullPage: true });
    check(bad.length === 0, `console/network errors (${scheme}): ${bad.slice(0, 3).join(" ; ")}`);
    await ctx.close();
  }
  // sub-pages: load without errors, axe-clean in both themes, in-page and cross-page links resolve
  for (const sub of ["security", "modules", "deploy"]) {
    for (const scheme of ["light", "dark"]) {
      const ctx = await browser.newContext({ colorScheme: scheme, viewport: { width: 1440, height: 900 } });
      const pg = await ctx.newPage();
      const bad = [];
      pg.on("console", (m) => { if (m.type() === "error") bad.push(m.text()); });
      pg.on("response", (r) => { if (r.status() >= 400) bad.push(`${r.status()} ${r.url()}`); });
      await pg.goto(`${base}/${sub}/`, { waitUntil: "networkidle" });
      await pg.evaluate(() => document.querySelectorAll("img[loading=lazy]").forEach((i) => { i.loading = "eager"; }));
      await pg.waitForTimeout(300);
      const ax = await new AxeBuilder({ page: pg }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
      for (const v of ax.violations.filter((x) => x.impact === "serious" || x.impact === "critical")) check(false, `axe /${sub}/ (${scheme}) ${v.id}: ${v.nodes.slice(0, 2).map((n) => n.target.join(" ")).join(" | ")}`);
      const links = await pg.evaluate(() => [...document.querySelectorAll("a[href]")].map((a) => a.getAttribute("href")).filter((h) => !h.startsWith("mailto:") && !h.startsWith("http")));
      for (const h of new Set(links)) {
        const u = new URL(h, `${base}/${sub}/`);
        if (u.pathname !== `/${sub}/` || !u.hash) { const r = await pg.request.get(u.origin + u.pathname); check(r.status() < 400, `/${sub}/ link broken: ${h}`); }
      }
      check(bad.length === 0, `console/network errors on /${sub}/ (${scheme}): ${bad.slice(0, 3).join(" ; ")}`);
      if (scheme === "light") await pg.screenshot({ path: join(shots, `${sub}.png`), fullPage: true });
      await ctx.close();
    }
  }
  // phone: no sideways scroll
  const m = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  const mp = await m.newPage();
  await mp.goto(base + "/", { waitUntil: "networkidle" });
  const overflow = await mp.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  check(overflow <= 0, `phone width overflows by ${overflow}px`);
  for (const sub of ["security", "modules", "deploy"]) {
    await mp.goto(`${base}/${sub}/`, { waitUntil: "networkidle" });
    const o = await mp.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    check(o <= 0, `/${sub}/ overflows by ${o}px on a phone`);
  }
  await mp.goto(base + "/", { waitUntil: "networkidle" });
  await mp.screenshot({ path: join(shots, "phone.png"), fullPage: true });
  await m.close();
  // reduced motion: everything is visible without scrolling or animation
  const rm = await browser.newContext({ reducedMotion: "reduce", viewport: { width: 1440, height: 900 } });
  const rp = await rm.newPage();
  await rp.goto(base + "/", { waitUntil: "networkidle" });
  const hidden = await rp.evaluate(() => [...document.querySelectorAll(".rv")].filter((e) => getComputedStyle(e).opacity !== "1").length);
  check(hidden === 0, `${hidden} sections hidden under reduced motion`);
  await rm.close();
  // 404 page, robots, sitemap
  const nf = await (await browser.newContext()).newPage();
  const res = await nf.goto(base + "/nope");
  check(res.status() === 404, "unknown path is a 404");
} finally {
  await browser.close();
  server.close();
}
if (failures.length) {
  console.error("site check FAILED:\n  " + failures.join("\n  "));
  process.exit(1);
}
console.log(`site check passed (screenshots in ${shots})`);
