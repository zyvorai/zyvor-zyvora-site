# Releases

**Pilot-ready software, not a certified medical product. Synthetic data only.**

The files are on the [GitHub Releases page](https://github.com/zyvorai/zyvor-zyvora-site/releases). There is **no application source** in this repository, so GitHub's automatic "Source code" archives only contain the website.

## What is in a release

| File | What it is |
|---|---|
| `get.sh` | The installer for **Mac and Linux**. Short, readable, and it only writes under `~/.zyvora`. |
| `get.ps1` | The installer for **Windows** (PowerShell; runs ZYVORA in WSL 2). Not yet verified on a real Windows PC. |
| `zyvora-install.tar.gz` | The install bundle (Compose files, the Envoy edge, the demo sign-in realm and the installer) that `get.sh` downloads. |
| `SHA256SUMS` | Checksums for the three files above. |
| Container images | `ghcr.io/zyvorai/zyvora-api` and `ghcr.io/zyvorai/zyvora-web`, same version tag as the release, `linux/amd64` and `linux/arm64`. |

## Versions

### 0.2.0 (latest)

One-command install for Mac, Windows (WSL 2) and Linux. New since 0.1.1:

- **Demo data with six patient stories**: signed notes, allergies, prescriptions, a chest X-ray report, a note awaiting signature and a nurse conversation.
- **`backup`, `restore FILE`** (checks the audit chain) and **`upgrade`** (rolls back on failure); **`--require-otp`** for real sign-in mode; the installer offers to set up a container engine (it asks first).
- **Fix:** a live screen could sometimes miss an update (the live stream skipped events that committed out of order).
- **Prometheus `/metrics`** (off unless a token is set) with starter alert rules.
- **A fully green browser suite** (35 passed, 19 skipped) in under five minutes.

### 0.1.1 (installer)

One-command install for Linux and macOS (docker or podman). Images tagged 0.1.1, `linux/amd64`.

## Verify your download

Download `SHA256SUMS` and the files into one folder, then:

```bash
shasum -a 256 -c SHA256SUMS      # Mac
sha256sum -c SHA256SUMS          # Linux
```

Each line should say `OK`. You do not have to do this for `get.sh`: it checks the install bundle's SHA-256 against the release's `SHA256SUMS` itself and **refuses to run on a mismatch.** To read the installer before running it, see [Getting started](GETTING-STARTED.md#read-the-installer-first).

## Upgrade, back up, restore, remove

```bash
~/.zyvora/zyvora upgrade                 # rolls back on failure
~/.zyvora/zyvora backup
~/.zyvora/zyvora restore FILE            # checks the audit chain
~/.zyvora/zyvora uninstall               # deletes the containers and their data
```

To upgrade an existing install to a specific version with the bootstrap script:

```bash
curl -fsSL https://github.com/zyvorai/zyvor-zyvora-site/releases/latest/download/get.sh | sh -s -- upgrade --version 0.2.0
```

## Real sign-in

The demo has no passwords. Real sign-in through an identity provider (Keycloak) is described in `INSTALL.md` inside the install bundle, and 0.2.0 adds `--require-otp` for real sign-in mode. Ask [sales](mailto:sales@zyvor.dev?subject=ZYVORA%20pilot) for the deployment documentation that goes with a pilot.
