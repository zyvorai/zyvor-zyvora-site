# Troubleshooting

**Pilot-ready software, not a certified medical product. Synthetic data only.**

## The browser says the connection is not private

That is expected. The demo makes its own security certificate on your computer. Choose **Advanced**, then **Proceed** (Safari: **Show Details**, then **visit this website**; Firefox: **Advanced**, then **Accept the Risk**). You do this once per browser.

## Nothing opened, or the page cannot be reached

Give it a minute after the command finishes, then run:

```bash
~/.zyvora/zyvora status
```

All five lines should say `Up`. Open the address the installer printed. The app listens on port 8443 on this computer only.

## It asked me to install something

If there is no container engine, the installer offers to install one (podman, using Homebrew on a Mac, or your package manager on Linux; WSL and podman on Windows). **It always asks first.** Answering no stops with the exact steps to do it yourself.

## Port 8443 is already in use

Add a different port at the end of the command, for example `--port 9443`. On Windows, put it after `--seed` as well.

## Windows: what happens the first time

If WSL 2 is missing, the script offers to install it. Windows asks for administrator approval, then you restart Windows, open **Ubuntu** once from the Start menu to create a Linux user, and run the same command again. Windows is **not yet verified** on a real PC; please tell us what you see.

## I am behind a company proxy or firewall

The installer downloads from `github.com` and `ghcr.io`. Ask IT to allow both, or try from a home connection.

## The checks did not pass

Run `~/.zyvora/zyvora test` and send us its output and your computer type.

## Start over, or remove everything

```bash
~/.zyvora/zyvora uninstall     # deletes the containers and their data
rm -rf ~/.zyvora               # also deletes the settings folder (on Windows, run it inside Ubuntu)
```

Then run the install command again.

## Still stuck

Email [sales@zyvor.dev](mailto:sales@zyvor.dev). Never send patient data or credentials.
