# Security policy

## Reporting a vulnerability

Email **[security@zyvor.dev](mailto:security@zyvor.dev)**. Please do **not** open a public issue for a vulnerability.

Include what you found, where (the installer, a container image or the website), the version, and the steps to reproduce it. **Do not include patient data or credentials** in a report.

## Scope

- The installer and release files published here (`get.sh`, `get.ps1`, `zyvora-install.tar.gz`) and the container images `ghcr.io/zyvorai/zyvora-api` and `ghcr.io/zyvorai/zyvora-web`.
- This website and the files in this repository.

There is no application source in this repository, so reports about source code cannot be handled here; send them by email and we will route them.

## Supported versions

Security fixes ship in the newest release. Check the [latest release](https://github.com/zyvorai/zyvor-zyvora-site/releases/latest). The installer verifies the SHA-256 of its bundle before running it.

## What to expect

ZYVORA is pilot-ready software built and tested with synthetic data only, with no independent penetration test yet. See the [security overview](docs/SECURITY-OVERVIEW.md) for the controls in place and what has not been done.
