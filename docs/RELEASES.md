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

### Next release (on the main branch, not yet published)

These are built and tested in the product repository but are **not in 0.4.0** and have no download yet. Still pilot-ready software, synthetic data only, and no AI model has been clinically validated.

- **Speech in several languages, installed on request:** an administrator can add speech for Hindi, Marathi, Malayalam, Tamil, Kannada, Telugu, Odia and others by listing a speech model per language. Nothing is installed by default and the server never downloads a model. On the consultation screen the clinician picks the language spoken. **No Indian-language speech model has been tested by us; read every transcript against what was said.**
- **Summary for the patient, in the patient's language:** a draft of the latest signed visit in plain words, English sentences checked against the record, then translated. The translation is **not** checked against anything except that its numbers match the English; someone who reads the language must read it before the patient gets it. Nothing is saved or sent.
- **Digits in any Indian script** (Odia, Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati, Gurmukhi, Devanagari) now count as the same number in the consultation grounding check.
- **Dashboard and menu:** the dashboard shows "Loading" instead of false zeros while figures arrive, and the module bar gains an "All modules" menu when it does not fit, so no module is hidden.

### 0.4.0 (latest)

Two AI features, a fix to a safety check, and an accessibility fix. Pilot-ready software, synthetic data only; nothing here is certified and no AI model has been clinically validated. New since 0.3.1:

- **Ask this chart:** on a patient's page, a question about that one patient's record ("what was the last potassium?", "any allergies?"). Every sentence of the answer names the parts of the record it came from and is checked against them; a sentence that cannot be tied to the record is left out and counted. It reads allergies, approved prescriptions, the last five signed visits, verified results and recent vitals, and nothing else, so "not in the record" means "not in those". Read-only, off with AI off (it then lists the parts of the record that share your words). **Not measured for accuracy.**
- **Draft quality:** on the AI model checks screen, what doctors did with AI drafts (accepted, edited, rejected), by feature, model and prompt version, and what the grounding check found in consultation drafts. A measure of use, not of correctness; no patient and no per-clinician figures. A new permission, held by doctors and hospital administrators.
- **Fix (safety check):** the grounding check for consultation drafts missed a claim such as "normal" or "no known allergies" when it came at the very end of a sentence. It now sees it. The first problems found on a statement are also kept when a doctor edits it. Re-scoring every recorded model run with the corrected check changed no published result.
- **Fix (accessibility):** the hover colour of primary buttons now has enough contrast against its text (5.57:1; it was 4.32:1).
- **Tools:** `ml/consult/rescore.sh` re-scores a finished model run with today's check.
- **Upgrading:** one new database migration (a new kind of AI job) is applied by `upgrade`, which rolls back on failure.
- **Checks:** 399 Rust tests, 521 API operations and 77 permissions; the browser suite passes on a fresh database.

### 0.3.1

A small fix release. Nothing else in the product changed since 0.3.0.

- **Fix:** on the **AI model checks** screen, a retired test conversation showed the name of the doctor who *reviewed* it under "Retired", which read as if the reviewer had retired it. The label now says "reviewed by".

### 0.3.0

Pilot-ready software, synthetic data only; nothing here is certified and no AI model has been clinically validated. New since 0.2.0:

- **Imaging operations:** a reading worklist with claim, report turnaround against targets the organisation sets, scanners and use, typed dose against reference levels, critical findings and follow-up tracking; a DICOM JSON modality worklist; header dose values offered for copying (never summed automatically).
- **Records:** possible-duplicate detection and soft linking with read-through of the linked history (nothing is moved).
- **Pharmacy:** part fills, completions and refills; draft prescription revision; controlled drugs with a second-person witness and a register.
- **Care and money:** treatment courses, recurring appointments, payment terms and overdue, lab delta checks.
- **Governance and AI:** a privacy watch over the audit trail (rules the organisation sets, reviewed once), plain-language result-explanation drafts (non-critical verified results, never sent by the system), HL7 mapping suggestions, read-only agent tools as GET endpoints, and a repeatable model-checking pipeline with clinician-written cases. A consultation-draft model was tried on a Mac mini GPU in three rounds and **none is recommended**; results are in the repository.
- **Checks:** 381 Rust tests, 519 API operations, and a browser suite of 64 specs (20 opt-in specs skipped by design) passing on a fresh database.

### 0.2.0

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
curl -fsSL https://github.com/zyvorai/zyvor-zyvora-site/releases/latest/download/get.sh | sh -s -- upgrade --version 0.4.0
```

## Real sign-in

The demo has no passwords. Real sign-in through an identity provider (Keycloak) is described in `INSTALL.md` inside the install bundle, and 0.2.0 adds `--require-otp` for real sign-in mode. Ask [sales](mailto:sales@zyvor.dev?subject=ZYVORA%20pilot) for the deployment documentation that goes with a pilot.
