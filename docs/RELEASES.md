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

**Which version should I install?** The latest release, **0.5.2**, which is what the one-command installer fetches. Read down from the top: each entry says what changed. Special words are in the [glossary](GLOSSARY.md).

### Next release (built and tested, not yet released)

39 modules are finished on the main branch and will arrive together in the next release: notifiable diseases and registers, nursing scales and early warning scores, birth and death registration, infection control, waiting lists, handover, prescription documents, telemedicine rules, privacy and records governance, quality indicators, language access, terminology, tariffs, tax invoices, claim files, DRG grouping, scheme billing and more. Every one is described, with what it refuses and where its limits are, in **[Next release](NEXT-RELEASE.md)**. They are not in any download yet.

### 0.5.2 (latest)

Many new hospital departments, built since 0.5.1. Pilot-ready software, synthetic data only; nothing here is certified and no AI model has been clinically validated. New since 0.5.1:


- **Patient-safety incidents:** any staff member reports a near miss, adverse event or sentinel event (patient optional, restricted records honoured); an administrator triages and assigns, records root cause and contributing factors, and closes with an outcome.
- **Ambulance crew care record and ED pre-arrival:** append-only observations (vitals, GCS), drugs and interventions against a trip, a handover sign-off at the ED that closes the record, a once-only medico-legal form (police informed, MLC number, brought-by), and an incoming alert with a hand-entered ETA that pre-registers the patient on the ED board.
- **Ward stock, barcodes and ward controlled-drug register:** par levels and an append-only ward stock ledger (issue from pharmacy, return, use), scan-by-barcode to receive or dispense, and a witnessed ward register of controlled drugs with a running balance.
- **Saved dashboards and report exports:** per-user dashboards of catalogue metrics shared with a role, per-metric permission gating, period-over-period comparison, targets with met/missed, and aggregate-only CSV export.
- **Demand forecasting and stores batch expiry:** read-only moving-average consumption from the pharmacy and stores ledgers with the window and formula shown, suggested orders, stock-out and over-stock flags; stores receipts may carry a batch number and expiry date, with a near-expiry list.
- **Occupancy forecast and staffing gaps:** a same-weekday-average forecast of inpatient census and ED arrivals with its measured past error, administrator-set minimum-cover rules per ward and shift, and an advisory list of days where the rota falls short.
- **De-identified analytics export:** an administrator defines datasets over five fixed aggregate sources (counts by month, kind and status; no names, identifiers or free text), a background job writes the CSV with groups under 5 records left out, and the file is downloaded once through a link that expires; every generation and download is audited.
- **IoT telemetry depth:** per-patient alert limits that replace the adult defaults (doctor-set, append-only, with paediatric presets), offline-device alerts when an attached device is silent past its interval, bucketed per-device trends, and infusion-pump and ventilator device kinds with their reading codes.
- **Dialysis session record:** a doctor prescribes (access, dry weight, schedule); a nurse starts a session with weights and a documented clothing or wheelchair allowance, adds machine readings and complications at intervals (append-only), records fluid removed and intake, and signs it off, after which the session is final; today's sessions per facility.
- **Maternity and labour record:** one obstetric episode per pregnancy per patient with antenatal visits, labour and append-only partograph observations that alert outside configurable safe ranges, the delivery summary and postpartum visits; doctors and nurses only, restricted patients need break-glass.
- **Oncology treatment plans:** chemotherapy and radiotherapy plans with a cycle calendar, drug doses a second clinician must verify (never the prescriber) before the infusion starts, infusion start and stop times, an append-only radiation dose ledger that stops at the plan total unless a doctor gives a written override, and a weekly chart check.
- **Resistance surveillance:** organisms and S/I/R susceptibilities recorded against a culture result and finalised by a second person; aggregate resistance rates by organism, antibiotic and period with cells under five patients hidden; a counts-and-ward-only outbreak signal for 3+ patients with one organism on a ward in 7 days.
- **Accounts payable:** vendors and their bills; the desk enters a bill, a different person approves or rejects it, an approved bill is paid once.
- **Facility management:** a per-facility register of building and plant assets, scheduled preventive-maintenance tasks with overdue flags and a completion log, and breakdown work orders that go open, assigned, done; audited, no patient data.
- **Staff credentials and attendance:** an administrator records licences, registrations and certifications with expiry and sees an expiring-soon list; credentials are withdrawn with a reason, never edited.
- **Pharmacy customers, sale returns and saved sale templates:** a walk-in customer register (name, phone, purchase history) that a counter sale can name; returns against a walk-in sale as credit notes that put stock back to its batch once and never exceed what was sold; per-pharmacist saved sale templates.
- **Patient self check-in kiosks:** a registered, revocable, per-facility device token that can only find today's visit from a one-time code plus date of birth (one uniform answer for every miss, codes lock after 5 wrong dates, kiosks throttle after 10 misses.
- **Inter-hospital referrals and transfers:** a patient is referred between two facilities of the same organisation; the receiving side (never the requester) accepts, with an optional bed note, or declines with a reason; the sender marks the patient transferred, the receiver marks them arrived; a return referral carries a follow-up instruction for a local clinic.
- **General stores:** non-drug supplies per facility on an append-only ledger that cannot go below zero; wards ask on requisitions, stores staff receive, adjust, issue or decline.
- **Pharmacy supplier invoices and GST:** a supplier invoice is matched three ways against the purchase order and goods received, differences become exceptions the approver accepts with a note, nobody approves their own, an approved invoice is paid once; CGST/SGST/IGST in whole paise from stored rates, drug GST rates copied onto sale lines, GST registers.
- **Staff rota and leave:** administrators schedule shifts that cannot overlap or fall on approved leave; staff see their own shifts and ask for leave; an administrator decides it, never their own.
- **White-label branding:** an organisation's name, tagline and one accent colour in the top bar and patient portal; text and colour only, and a colour too light for white button text is refused.
- **Health record sharing, ABDM-style:** a patient's ABHA address (recorded, not verified), signed visits linked as care contexts, consent requests decided once and withdrawable, and records shared only under a granted, unexpired consent that covers that kind of record and date; every share is logged and audited.
- **Medical device feeds:** bedside devices are registered by an administrator and push numeric readings (heart rate, SpO₂, blood pressure, temperature, respiratory rate, glucose.
- **Hospital scorecard:** `GET /dashboard/scorecard` and a panel at the top of Insights give one set of aggregate figures per newer module (queues, feedback, medication rounds, bed cleaning, day care, blood stock, ambulance, homecare).
- **Homecare:** a doctor orders a course of home visits (wound care, injections, physiotherapy, elderly, post-surgical, palliative.
- **Ambulance:** calls are taken with priority, pickup, destination and either a registered patient or a description; a vehicle and crew are dispatched and the trip goes one step at a time to completion, each step stamped by the database and logged.
- **Radiology depth:** scanners get booked slots that the database will not let overlap; pre-scan screening (identity, pregnancy, MRI implants, contrast allergy and recent kidney function) is recorded per order and, when the department turns the requirement on (off by default).
- **Laboratory depth:** a specimen can be dispatched and received (no result while it is in transit) or rejected with a reason and collected again.
- **Pharmacy depth:** every delivery now leaves a goods receipt note with the supplier's invoice (received once).
- **Sterile services (CSSD):** instrument sets and their packs go round a loop (used, washed and packed, loaded, sterilised, released, issued, returned).
- **Medical records department:** a new `records_officer` role (no chart access) keeps a ledger of physical record folders that move only by recorded movements (issue with a due date, return, missing, found, archive.
- **Day care:** planned same-day treatments in a new *day care* ward kind.
- **Cath lab:** the procedure record for a catheterisation booked as a theatre case.
- **Corporate clients and an employer portal:** the administrator agrees health check packages and prices with an employer; the employer's own HR contact (a new `corporate_contact` role with no clinical access) keeps a staff roster, asks for health checks, and sees where each stands and the account.
- **Payer receivables:** a ledger of what insurers and TPAs owe on approved claims, aged against the days each payer agreed to (1–30, 31–60, 61–90, over 90 late, and falling due soon); one payment from a payer is recorded once and allocated, to the paisa, across many claims.
- **Doctor payout:** the administrator sets each doctor's share (a percentage or a fixed amount) per kind of service; billing counts what signed visits have earned from invoices paid in full, with the rate frozen on each entry, and pays a doctor everything owed in one numbered payment that must match what the payer saw.
- **Blood bank, transfusion side:** a patient's blood group is trusted only when two people find the same group on two samples; doctors request blood (an emergency needs their written statement); the laboratory cross-matches and holds units.
- **Blood bank, stock side:** laboratory technicians register donors, take donations (age, weight.
- **Patient feedback:** patients rate an area of the hospital (1 to 5, with an optional comment.
- **Queue management:** numbered tickets for registration, triage, consultation, lab, imaging, pharmacy and billing, restarting each day; priority first, then longest waiting; two counters never get the same ticket; tickets only move forward and carry no patient.
- **Housekeeping and a housekeeper role:** a cleaning job opens whenever a bed goes into cleaning (terminal clean for isolation wards); housekeepers start and finish jobs on a new Housekeeping page and see ward and bed labels, never a patient; finishing frees the bed and the page shows today's turnaround.
- **Diet orders:** doctors and nurses set an admitted patient's diet from the stay dialog; a change stops the old order and keeps it as history, nil by mouth must say why, and orders cannot be edited or deleted (database trigger).
- **Medication administration record:** nurses schedule an admitted patient's doses from an approved prescription and record each as given, held or refused on a new Medication round screen; held and refused need a reason and a recorded dose cannot be changed (database trigger).
- **Demo seed: the phone-app patient:** the demo patient login is linked to a synthetic patient with appointments, a message thread and a released result, so the Patient app has something to show.
- **Patient identifiers:** ABHA number, Emirates ID (check digit verified) and passport; masked in lists, whole number only for editors and audited, one patient per number, desk lookup.
- **Prior authorisation tracking:** record what was asked of an insurer and the answer, a waiting list for the desk, expiry worked out.
- **Upgrading:** new database migrations (0067 to 0109), applied by `upgrade`, which rolls back on failure.
- **Checks:** the Rust workspace tests on the tagged tree: **726 passed, 0 failed, 4 ignored** in 141 test binaries (on the maintainer's machine, against PostgreSQL), plus the web type check, build and 88 unit tests, `cargo deny` and `pnpm audit`. **Not done for this release:** the hosted continuous-integration run, the secret scan and the full browser suite. The images are published for amd64 and arm64.

### 0.5.1

Four small conveniences for everyday work. Pilot-ready software, synthetic data only; nothing here is certified and no AI model has been clinically validated. New since 0.5.0:

- **Starred patients:** a star on a patient's page keeps them under "My patients" on your dashboard. The list is private to you, holds at most 50, and leaves out records you may not open.
- **Thank-yous between colleagues:** a short note to a colleague, shown only to the person thanked. It is refused if it has five or more digits in a row, an `@` or a link, so it cannot carry a patient number; ten a day at most per sender. No scores, no streaks.
- **Your unfinished visits:** a doctor's own visits waiting for their signature first, then those still open, with a plain count signed in the last 24 hours. No targets, no ranking.
- **Tip of the day:** one short tip about something the app really does, the same all day, only offered to people who can use it, and can be hidden for good.
- **Upgrading:** two new database migrations (starred patients, thank-yous), applied by `upgrade`, which rolls back on failure.
- **Checks:** 419 Rust tests, 531 API operations and 77 permissions. The full browser suite was last run at 0.5.0; the new specs were each run on their own.

### 0.5.0

Drafting help in the patient's language, a check before signing, and a better patient list. Pilot-ready software, synthetic data only; nothing here is certified and no AI model has been clinically validated. New since 0.4.0:

- **Summary for the patient, in the patient's language, and medicine instructions:** a draft of the latest signed visit, or only the approved medicines with doses and days, in plain words, in 13 languages. The English sentences are checked against the record; the translation is **not** checked against anything except that its numbers match the English, so someone who reads the language must read it before the patient gets it. Nothing is saved or sent. Identifiers are removed before the model is called, on both calls.
- **Referral letter draft:** you give the specialty and the reason in your own words; the facts about the patient come only from the record, each sentence cited and checked. Nothing is saved, sent or filed; you copy the text and send it yourself.
- **Speech in several languages, installed on request:** an administrator can add speech for Hindi, Marathi, Malayalam, Tamil, Kannada, Telugu, Odia and others by listing a speech model per language. Nothing is installed by default and the server never downloads a model. On the consultation screen the clinician picks the language spoken. **No Indian-language speech model has been tested by us; read every transcript against what was said.**
- **Before you sign:** while a visit is in review, a panel lists what would stop the signature and what is not recorded (no measurements, no allergy on file, an empty section). Plain rules, no AI. A reminder says something is not recorded, never that the patient has none.
- **Patient list:** allergies, last signed visit and next appointment beside each name, for people who may read charts (front desk sees the plain list). A cell shows "…" while loading and "–" if it failed, never a false "none". Records a person may not open are left out.
- **Allergy line beside the patient's name:** checking, "No allergies recorded" (never "no known allergies"), or the substances with severity.
- **Menus shaped by role:** a "Your work" group first for each role; no module is hidden. The module bar gains an "All modules" menu when it does not fit, and the dashboard shows "Loading" instead of false zeros while figures arrive.
- **Phones:** the search button no longer shows a keyboard chip, and small buttons are 44 px on touch screens.
- **Digits in any Indian script** now count as the same number in the consultation grounding check.
- **Fix:** the payment simulator's reference could contain a run of 13 digits and be refused by the card-number check (a few percent of simulated payments). Now shorter.
- **Upgrading:** two new database migrations (new kinds of AI job) are applied by `upgrade`, which rolls back on failure.
- **Checks:** 413 Rust tests, 525 API operations and 77 permissions.

### 0.4.0

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
