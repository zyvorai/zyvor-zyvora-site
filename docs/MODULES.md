# Modules

**Pilot-ready software, not a certified medical product. Synthetic data only.**

ZYVORA has twelve modules: dashboard, patients, appointments, emergency, beds, lab, imaging, pharmacy, billing, insights, audit and setup. This is what they do.

## Clinical core

| Feature | What it does |
|---|---|
| Patient registry | Demographics, allergies, restricted records, relationship-based access |
| Appointments | Booking, check-in and a waiting-room queue; no double-booking, enforced by the database |
| Encounters | SOAP notes with append-only revisions, vitals, signing, reasoned amendments (only doctors sign) |
| Prescribing | Prescriptions with an honest safety report: where there is no drug database, checks say `unavailable`, never "passed" |

## Hospital

| Feature | What it does |
|---|---|
| Emergency | Tracking board with triage decision support (a trained classifier plus safety rules, not an LLM) |
| Wards and beds | Admissions, transfers and discharge; a bed map per ward |
| Laboratory | Specimens, results, separate verification, critical alerts, result history |
| Imaging | Orders, DICOM header registration with a wrong-patient guard, reports (only radiologists report), an external viewer link |
| Pharmacy | FEFO stock ledger, purchasing, dispensing, returns (only pharmacists dispense) |

## Business

| Feature | What it does |
|---|---|
| Billing | Exact money, tax rules held as data, idempotent payments, refunds |
| Insurance | Pre-authorisation and claims |
| Insights | Eleven fixed metrics with charts and a table view for each; a closed catalogue, no generated SQL |
| Setup | Facilities, wards, formulary, tax rates and payers, with a first-run checklist |

## Live and connected

| Feature | What it does |
|---|---|
| Live screens | Boards, queues and the dashboard update as things happen over a live event stream (no patient data in events); screens fall back to polling if it drops |
| Alerts that need a person | A critical lab result, a red-triage arrival or an urgent message stays on screen until someone acknowledges it; if nobody does, an editable ladder tells the next group |
| Staff messaging | Direct and team conversations, handover notes (SBAR), threads about one patient (clinical staff only, audited), read receipts; messages cannot be edited or deleted |
| Patient messages | A patient writes to the clinic; the care team answers from an inbox with a waiting indicator |
| Email and SMS | Pluggable and off by default (log-only until configured); reminders only to patients who agreed, saying as little as the organisation chooses; no patient data in staff nudges |
| Video visits | The clinician is told when the patient is waiting; signed Jitsi links with strict who-and-when rules |

**Not a certified paging system:** no pager or nurse-call integration, and email and SMS delivery has been verified only to local test sinks.

## Patients

| Feature | What it does |
|---|---|
| Portal | A patient's own appointments, medicines, released results and visit summaries |

## Governance

| Feature | What it does |
|---|---|
| Roles | Nine roles, deny by default, plus relationship and facility checks |
| Audit | Viewer with chain verification; every read and change of a record is recorded (metadata only) |
| Privacy | A privacy impact assessment and an honest compliance gap list exist in the product documentation |

## AI, with review

| Feature | What it does |
|---|---|
| Opt-in | Off unless an organisation enables it, on a private OpenAI-compatible server (Nuvora, vLLM, Ollama, mlx-lm) |
| Drafts | SOAP drafts, summaries, coding suggestions, document extraction, an operations brief, natural-language questions over the closed metric catalogue |
| Review | Every clinical draft needs a named human review bound to the clinician's own note revision |
| Limits | No clinical validation of any model |

## Standards and integration

| Feature | What it does |
|---|---|
| FHIR R4 | Read-only: Patient, Encounter, Observation, AllergyIntolerance, MedicationRequest, Appointment, `$everything` |
| OpenAPI | One document and a typed client; 182 operations on 158 paths |
| Zyvor platform | Netra, Nuvora and FluxVM adapters. Only FluxVM has been verified live; Netra and Nuvora are tested against stand-ins. |

Back to the [documentation index](README.md).
