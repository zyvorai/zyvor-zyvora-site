# Troubleshooting

**Pilot-ready software, not a certified medical product. Synthetic data only.**

> **In one minute.** Most problems are one of three things: the browser warning (expected, once), a port already in use (pick another), or the installer waiting for you to say yes. Find your symptom below. If nothing fits, run `~/.zyvora/zyvora test` and email us its output.

## Quick finder

| What you see | Go to |
|---|---|
| "Your connection is not private" | [The browser warning](#the-browser-says-the-connection-is-not-private) |
| A blank page, or "cannot be reached" | [Nothing opened](#nothing-opened-or-the-page-cannot-be-reached) |
| A question about installing something | [It asked me to install something](#it-asked-me-to-install-something) |
| "Port 8443 is already in use" | [A busy port](#port-8443-is-already-in-use) |
| Windows asks for approval or a restart | [Windows first run](#windows-what-happens-the-first-time) |
| Downloads fail at work | [Company proxy or firewall](#i-am-behind-a-company-proxy-or-firewall) |
| `all checks passed` did not appear | [The checks did not pass](#the-checks-did-not-pass) |
| You want to begin again | [Start over](#start-over-or-remove-everything) |

## The browser says the connection is not private

**This is expected, and safe here.** The demo makes its own security certificate on your computer, and no browser has heard of it, so every browser warns once. The address is your own computer, so there is nobody to be fooled by.

| Browser | What to click |
|---|---|
| Chrome, Edge | **Advanced**, then **Proceed** |
| Safari | **Show Details**, then **visit this website** |
| Firefox | **Advanced**, then **Accept the Risk** |

You do this once per browser.

## Nothing opened, or the page cannot be reached

Give it a minute after the command finishes (it is starting a small hospital), then run:

```bash
~/.zyvora/zyvora status
```

All five lines should say `Up`. Open the address the installer printed. The app listens on port 8443 on this computer only.

## It asked me to install something

If there is no container engine (the program that runs ZYVORA in a sealed box), the installer offers to install one: podman, using Homebrew on a Mac, your package manager on Linux, or WSL and podman on Windows. **It always asks first.** Answering no stops, and shows the exact steps to do it yourself.

## Port 8443 is already in use

Another program is using that door. Add a different port at the end of the command, for example `--port 9443`. On Windows, put it after `--seed` as well.

## Windows: what happens the first time

If WSL 2 (Windows' built-in Linux) is missing, the script offers to install it:

1. Windows asks for administrator approval.
2. You restart Windows.
3. Open **Ubuntu** once from the Start menu to create a Linux user.
4. Run the same command again.

Windows is **not yet verified** on a real PC. If you try it, please tell us what you see.

## I am behind a company proxy or firewall

The installer downloads from `github.com` and `ghcr.io`. Ask IT to allow both, or try from a home connection.

## The checks did not pass

Run this and send us the output together with your computer type:

```bash
~/.zyvora/zyvora test
```

## Start over, or remove everything

```bash
~/.zyvora/zyvora uninstall     # deletes the containers and their data
rm -rf ~/.zyvora               # also deletes the settings folder (on Windows, run it inside Ubuntu)
```

Then run the install command again from [Getting started](GETTING-STARTED.md).

## Still stuck

Email [sales@zyvor.dev](mailto:sales@zyvor.dev). Never send patient data or credentials. Words you do not know are in the [glossary](GLOSSARY.md).
