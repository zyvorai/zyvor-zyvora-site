#!/usr/bin/env python3
"""Writes the light and dark SVG illustrations for the /try/ page (assets/try-*.svg) and the AI flow and review illustration (assets/ai-*.svg) from one template each.
Run from the repository root:  python3 scripts/gen-try-graphics.py
Colours follow site.css; every graphic carries a title and description for screen readers."""
from pathlib import Path

FONT = "-apple-system,BlinkMacSystemFont,'SF Pro Display','SF Pro Text','Segoe UI',Roboto,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"
PAL = {
    "light": dict(bg="#ffffff", card="#f5f5f7", line="#d2d2d7", text="#1d1d1f", dim="#6e6e73", green="#34c759", accent="#0071e3", warn="#ff9f0a", warnbg="#fff4e0", key="#ffffff", term="#1d1d1f", termtext="#f5f5f7"),
    "dark": dict(bg="#000000", card="#1d1d1f", line="#3a3a3c", text="#f5f5f7", dim="#a1a1a6", green="#30d158", accent="#2997ff", warn="#ffd60a", warnbg="#2b2300", key="#2c2c2e", term="#0b0b0c", termtext="#f5f5f7"),
}


def t(x, y, s, size=16, weight=400, fill="text", anchor="start", mono=False, p=PAL["light"], ls=0.0):
    fam = MONO if mono else FONT
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{p[fill]}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>'


def rect(x, y, w, h, r, fill, p, stroke=None, sw=1.0):
    st = f' stroke="{p[stroke]}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{p[fill]}"{st}/>'


def svg(w, h, title, desc, body, p):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>'
            f'<rect width="{w}" height="{h}" fill="{p["bg"]}"/>{body}</svg>\n')


# ---- 1. the whole journey, five steps -------------------------------------------------------------------------------
def steps(p):
    items = [("1", "Paste one command", "into Terminal or PowerShell"), ("2", "Accept the warning", "once: the certificate is your own"),
             ("3", "Pick a doctor", "no password in the demo"), ("4", "Look around", "invented patients, real screens"),
             ("5", "Check it", "one command says all passed")]
    b = [t(640, 52, "From paste to dashboard in five steps", 30, 700, p=p, anchor="middle", ls=-0.8),
         t(640, 84, "About five minutes. Nothing leaves your computer.", 17, 400, "dim", p=p, anchor="middle")]
    w, gap, x0, y0, h = 224, 20, 40, 120, 250
    for i, (n, head, sub) in enumerate(items):
        x = x0 + i * (w + gap)
        b.append(rect(x, y0, w, h, 20, "card", p, "line"))
        b.append(f'<circle cx="{x + 34}" cy="{y0 + 36}" r="16" fill="{p["accent"]}"/>' + t(x + 34, y0 + 42, n, 16, 700, "bg", "middle", p=p))
        cx, cy = x + w // 2, y0 + 118
        if i == 0:   # terminal window
            b += [rect(cx - 70, cy - 40, 140, 80, 10, "term", p), f'<circle cx="{cx - 56}" cy="{cy - 28}" r="3.5" fill="#ff5f57"/><circle cx="{cx - 44}" cy="{cy - 28}" r="3.5" fill="#febc2e"/><circle cx="{cx - 32}" cy="{cy - 28}" r="3.5" fill="#28c840"/>',
                  t(cx - 58, cy + 2, "$ curl … | sh", 14, 500, "termtext", mono=True, p=p), f'<rect x="{cx - 58}" y="{cy + 14}" width="9" height="15" fill="{p["green"]}"/>']
        elif i == 1:  # warning triangle
            b += [f'<path d="M{cx} {cy - 42} L{cx + 46} {cy + 34} L{cx - 46} {cy + 34} Z" fill="{p["warnbg"]}" stroke="{p["warn"]}" stroke-width="4" stroke-linejoin="round"/>',
                  f'<rect x="{cx - 3}" y="{cy - 18}" width="6" height="30" rx="3" fill="{p["warn"]}"/><circle cx="{cx}" cy="{cy + 22}" r="3.5" fill="{p["warn"]}"/>']
        elif i == 2:  # avatars
            for k, (dx, lab, hl) in enumerate([(-52, "MR", True), (0, "IK", False), (52, "KI", False)]):
                b.append(f'<circle cx="{cx + dx}" cy="{cy}" r="22" fill="{p["bg"]}" stroke="{p["accent"] if hl else p["line"]}" stroke-width="{3 if hl else 1.5}"/>' + t(cx + dx, cy + 6, lab, 15, 700, p=p, anchor="middle"))
            b.append(f'<path d="M{cx - 66} {cy + 44} l14 -12 l14 12" fill="none" stroke="{p["accent"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
        elif i == 3:  # dashboard thumbnail
            b += [rect(cx - 74, cy - 46, 148, 92, 10, "bg", p, "line"), rect(cx - 66, cy - 38, 60, 26, 6, "card", p), rect(cx + 2, cy - 38, 64, 26, 6, "card", p),
                  f'<polyline points="{cx - 66},{cy + 30} {cx - 40},{cy + 8} {cx - 18},{cy + 22} {cx + 8},{cy - 2} {cx + 34},{cy + 12} {cx + 66},{cy - 6}" fill="none" stroke="{p["accent"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>']
        else:         # check
            b += [f'<circle cx="{cx}" cy="{cy}" r="44" fill="{p["green"]}" fill-opacity="0.18" stroke="{p["green"]}" stroke-width="4"/>',
                  f'<path d="M{cx - 20} {cy + 2} l14 14 l28 -30" fill="none" stroke="{p["green"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>']
        b += [t(x + w // 2, y0 + 202, head, 18, 700, p=p, anchor="middle", ls=-0.3), t(x + w // 2, y0 + 226, sub, 13, 400, "dim", p=p, anchor="middle")]
    return svg(1280, 400, "Five steps to try ZYVORA",
               "Paste one command, accept the browser's certificate warning once, pick a demo doctor, look around the dashboard, and run the check command.", "".join(b), p)


# ---- 2. the certificate warning ----------------------------------------------------------------------------------
def warning(p):
    b = [rect(30, 40, 820, 440, 16, "card", p, "line"), rect(30, 40, 820, 46, 16, "line", p), rect(30, 66, 820, 20, 0, "line", p),
         '<circle cx="56" cy="63" r="6" fill="#ff5f57"/><circle cx="78" cy="63" r="6" fill="#febc2e"/><circle cx="100" cy="63" r="6" fill="#28c840"/>',
         rect(130, 50, 440, 26, 13, "bg", p), t(150, 69, "https://localhost", 14, 400, "dim", mono=True, p=p),
         f'<path d="M440 150 L488 232 L392 232 Z" fill="{p["warnbg"]}" stroke="{p["warn"]}" stroke-width="5" stroke-linejoin="round"/><rect x="436" y="174" width="8" height="32" rx="4" fill="{p["warn"]}"/><circle cx="440" cy="220" r="4.5" fill="{p["warn"]}"/>',
         t(440, 290, "Your connection is not private", 28, 700, p=p, anchor="middle", ls=-0.6),
         t(440, 322, "This computer made its own security certificate, so the browser cannot vouch for it.", 15, 400, "dim", p=p, anchor="middle"),
         rect(330, 358, 220, 46, 23, "bg", p, "accent", 2.5), t(440, 387, "Advanced", 17, 600, "accent", "middle", p=p),
         f'<path d="M330 381 L286 381" stroke="{p["accent"]}" stroke-width="3" stroke-linecap="round"/><path d="M296 371 L284 381 L296 391" fill="none" stroke="{p["accent"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
         t(268, 388, "1. Click this", 17, 700, "accent", "end", p=p), t(440, 438, "Proceed to localhost (unsafe)", 15, 500, "dim", "middle", p=p),
         f'<line x1="326" y1="443" x2="554" y2="443" stroke="{p["dim"]}" stroke-width="1"/>',
         f'<path d="M640 438 L590 438" stroke="{p["green"]}" stroke-width="3" stroke-linecap="round"/><path d="M602 428 L590 438 L602 448" fill="none" stroke="{p["green"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
         t(656, 444, "2. Then this", 17, 700, "green", "start", p=p),]
    b.append(t(440, 510, "Illustration: your browser's wording differs a little", 13, 400, "dim", "middle", p=p))
    return svg(880, 520, "The browser's certificate warning and what to click",
               "A browser window showing a warning that the connection is not private, with an arrow to Advanced and then to Proceed. Wording differs by browser.", "".join(b), p)


# ---- 3. where to type the command -----------------------------------------------------------------------------------
def where(p):
    cols = [("Mac", "Terminal", [("⌘", ""), ("Space", "")], ("Press Command and Space,", "type Terminal, press Return.")),
            ("Windows", "PowerShell", [("⊞", "")], ("Press the Windows key,", "type PowerShell, press Enter.")),
            ("Linux", "Terminal", [("Ctrl", ""), ("Alt", ""), ("T", "")], ("Press Ctrl, Alt and T together,", "or open Terminal from your apps."))]
    b = [t(640, 52, "Where do I paste it?", 30, 700, p=p, anchor="middle", ls=-0.8), t(640, 84, "Any terminal works. These are the quickest ways to open one.", 17, 400, "dim", p=p, anchor="middle")]
    w, gap, x0, y0 = 380, 30, 40, 120
    for i, (osn, app, keys, how) in enumerate(cols):
        x = x0 + i * (w + gap)
        b += [rect(x, y0, w, 250, 20, "card", p, "line"), t(x + 28, y0 + 52, osn, 26, 700, p=p, ls=-0.5), t(x + 28, y0 + 80, f"Open {app}", 16, 400, "dim", p=p)]
        kx = x + 28
        for k, _ in keys:
            kw = 38 + 14 * len(k)
            b += [rect(kx, y0 + 108, kw, 46, 10, "key", p, "line", 1.5), t(kx + kw / 2, y0 + 139, k, 17, 600, p=p, anchor="middle")]
            kx += kw + 12
        b += [t(x + 28, y0 + 196, how[0], 15, 400, "dim", p=p), t(x + 28, y0 + 218, how[1], 15, 400, "dim", p=p)]
    return svg(1280, 400, "How to open a terminal on Mac, Windows and Linux",
               "On a Mac press Command and Space and type Terminal. On Windows press the Windows key and type PowerShell. On Linux press Control, Alt and T.", "".join(b), p)


# ---- 4. the AI review flow (home page and /ai/) -----------------------------------------------------------------------
def ai_flow(p):
    items = [("1", "Note or transcript", "With the patient's consent"),
             ("2", "Private model", "Identifiers removed first"),
             ("3", "Draft", "Quotes the lines it came from"),
             ("4", "Named clinician", "Accepts, edits or rejects"),
             ("5", "Audit chain", "Bound to the note revision")]
    b = [t(640, 52, "The assistant drafts. A named clinician decides.", 30, 700, p=p, anchor="middle", ls=-0.8),
         t(640, 84, "Off until an administrator turns it on. On a private server you control. Synthetic data only.", 17, 400, "dim", p=p, anchor="middle")]
    w, gap, x0, y0, h = 224, 20, 40, 120, 220
    for i, (n, head, sub) in enumerate(items):
        x = x0 + i * (w + gap)
        hl = i == 3
        b.append(rect(x, y0, w, h, 20, "card", p, "accent" if hl else "line", 2.5 if hl else 1))
        b.append(f'<circle cx="{x + 34}" cy="{y0 + 36}" r="16" fill="{p["accent"]}"/>' + t(x + 34, y0 + 42, n, 16, 700, "bg", "middle", p=p))
        cx, cy = x + w // 2, y0 + 106
        if i == 0:    # note lines
            b += [rect(cx - 50, cy - 36, 100, 72, 10, "bg", p, "line")] + [rect(cx - 36, cy - 22 + k * 16, 72 - (k % 2) * 18, 6, 3, "line", p) for k in range(4)]
        elif i == 1:  # server with lock
            b += [rect(cx - 46, cy - 36, 92, 28, 8, "bg", p, "line"), rect(cx - 46, cy + 2, 92, 28, 8, "bg", p, "line"),
                  f'<circle cx="{cx - 30}" cy="{cy - 22}" r="4" fill="{p["green"]}"/><circle cx="{cx - 30}" cy="{cy + 16}" r="4" fill="{p["green"]}"/>']
        elif i == 2:  # draft with a citation marker
            b += [rect(cx - 50, cy - 36, 100, 72, 10, "bg", p, "accent"), rect(cx - 36, cy - 22, 60, 6, 3, "accent", p), rect(cx - 36, cy - 6, 72, 6, 3, "line", p), rect(cx - 36, cy + 10, 48, 6, 3, "line", p),
                  t(cx + 36, cy - 17, "[1]", 12, 700, "accent", "middle", p=p)]
        elif i == 3:  # person and tick
            b += [f'<circle cx="{cx}" cy="{cy - 14}" r="16" fill="{p["bg"]}" stroke="{p["accent"]}" stroke-width="3"/><path d="M{cx - 30} {cy + 34} q30 -40 60 0" fill="none" stroke="{p["accent"]}" stroke-width="3" stroke-linecap="round"/>',
                  f'<circle cx="{cx + 34}" cy="{cy + 24}" r="14" fill="{p["green"]}"/><path d="M{cx + 27} {cy + 24} l5 5 l9 -11" fill="none" stroke="{p["bg"]}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>']
        else:         # chain links
            b += [rect(cx - 62 + k * 44, cy - 14, 36, 28, 8, "bg", p, "line", 2) for k in range(3)] + [f'<line x1="{cx - 26 + k * 44}" y1="{cy}" x2="{cx - 18 + k * 44}" y2="{cy}" stroke="{p["accent"]}" stroke-width="3"/>' for k in range(2)]
        b += [t(x + w // 2, y0 + 176, head, 18, 700, p=p, anchor="middle", ls=-0.3), t(x + w // 2, y0 + 200, sub, 13, 400, "dim", p=p, anchor="middle")]
        if i < 4:
            ax = x + w + 2
            b.append(f'<path d="M{ax} {y0 + h // 2} l16 0 m-6 -6 l6 6 l-6 6" fill="none" stroke="{p["dim"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(t(640, 384, "Draft only: no tools, no actions, no generated SQL. No model has been clinically validated.", 14, 400, "dim", p=p, anchor="middle"))
    return svg(1280, 410, "How an AI draft is reviewed",
               "Draft only. A note or consented transcript goes to a private model after identifiers are removed. The draft quotes its sources. A named clinician accepts, edits or rejects it, and the review is bound to the note revision and recorded on the hash-chained audit trail. Synthetic data only.", "".join(b), p)


# ---- 5. an illustrated review panel (rendered to shots/*-ai.jpg; clearly an illustration, not a screenshot) ---------------
def ai_panel(p):
    b = [rect(0, 0, 1440, 900, 0, "bg", p), rect(60, 60, 1320, 780, 24, "card", p, "line"),
         t(100, 130, "Draft assessment and plan", 34, 700, p=p, ls=-0.8),
         rect(1000, 98, 340, 44, 22, "warnbg", p), t(1170, 127, "DRAFT: clinician must review", 16, 700, "warn", "middle", p=p),
         t(100, 168, "Synthetic patient · invented note · illustration, not a screenshot", 16, 400, "dim", p=p)]
    rows = [("Subjective", "Cough for three days, worse at night. No fever reported.", "note line 2"),
            ("Objective", "Temperature 36.8 °C. Chest clear on auscultation.", "note lines 5-6"),
            ("Assessment", "Consider a viral upper respiratory infection.", "note lines 2, 6"),
            ("Plan", "Fluids and rest. Review in one week if not improving.", "note line 8")]
    y = 210
    for head, body, cite in rows:
        b += [rect(100, y, 780, 118, 16, "bg", p, "line"), t(128, y + 38, head, 15, 700, "accent", p=p, ls=0.5), t(128, y + 74, body, 21, 500, p=p),
              t(128, y + 102, "Source: " + cite, 14, 400, "dim", p=p)]
        y += 134
    b += [rect(920, 210, 420, 524, 16, "bg", p, "line"), t(950, 252, "Review", 22, 700, p=p, ls=-0.4),
          t(950, 288, "Reviewer: a named clinician", 15, 400, "dim", p=p), t(950, 312, "Bound to note revision 3", 15, 400, "dim", p=p)]
    for k, (lab, hl) in enumerate([("Accept", True), ("Edit", False), ("Reject", False)]):
        b += [rect(950, 352 + k * 66, 360, 50, 25, "accent" if hl else "bg", p, "accent"), t(1130, 384 + k * 66, lab, 18, 600, "bg" if hl else "accent", "middle", p=p)]
    b += [t(950, 590, "Nothing joins the record until a", 15, 400, "dim", p=p), t(950, 612, "named clinician has reviewed it.", 15, 400, "dim", p=p),
          t(950, 660, "Recorded on the audit chain.", 15, 400, "dim", p=p),
          t(720, 806, "ILLUSTRATION · SYNTHETIC DATA · NOT A SCREENSHOT OF THE PRODUCT", 14, 700, "dim", "middle", p=p, ls=1.2)]
    return svg(1440, 900, "Illustration of a draft review", "An illustration with invented text: a draft assessment and plan, each statement citing note lines, with Accept, Edit and Reject for a named clinician.", "".join(b), p)


def main():
    out = Path("assets")
    for name, fn in (("try-steps", steps), ("try-warning", warning), ("try-where", where), ("ai-flow", ai_flow), ("ai-panel", ai_panel)):
        for mode, p in PAL.items():
            (out / f"{name}-{mode}.svg").write_text(fn(p), encoding="utf-8")
    print("wrote", ", ".join(sorted(f.name for f in out.glob("*.svg"))))


if __name__ == "__main__":
    main()
