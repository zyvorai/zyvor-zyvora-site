# Modules

**Pilot-ready software, not a certified medical product. Synthetic data only.**

ZYVORA's modules share one patient record, one sign-in, one audit trail and one permission model. Each table says what exists; the limits of a group are stated under it.

## Clinical core

| Feature | What it does |
|---|---|
| Patient registry | Demographics, allergies, restricted records, relationship-based access, problems and immunisations |
| Appointments | Booking, check-in and a waiting-room queue; no double-booking, enforced by the database; a missed visit opens a rebooking task |
| Encounters | SOAP notes with append-only revisions, vitals, signing, reasoned amendments (only doctors sign) |
| Prescribing | Prescriptions with an honest safety report: where there is no drug database, checks say `unavailable`, never "passed" |
| Consultation assistant | With the patient's consent, a transcript becomes a draft whose every statement points to the lines it came from; a named clinician accepts, edits or rejects each one and signs |
| Note templates and chart forms | Skeleton text and structured forms (a per-tooth map, right and left pairs, choices) that the **hospital** writes for a specialty; nothing clinical ships in the software; saves are revisions that keep the form they used |
| Medication reconciliation | Before-admission, in-hospital and discharge lists compared by fixed rules; a prescriber decides each difference, a pharmacist signs |
| Protocols | The hospital's own protocols, approved by a second person and immutable once approved; cited answers only from approved passages |

## Hospital

| Feature | What it does |
|---|---|
| Emergency | Tracking board with triage decision support (a trained classifier plus safety rules, not an LLM) |
| Wards and beds | Admissions, transfers and discharge; a bed map per ward |
| Discharge | Plans whose milestones are tasks with owners, waivers with reasons, a board and timing measures |
| Theatre | Rooms, cases and reservations the database will not let overlap, readiness checks, blocks, emergency override |
| Virtual nursing | Bedside call requests, a nurse queue and waiting room, short-lived per-room access revoked on discharge |
| Laboratory | Specimens, results, separate verification, critical alerts, turnaround against the lab's own targets, home sample collection with a printable round |
| Imaging | Orders, DICOM header registration with a wrong-patient guard, reports (only radiologists report), an external viewer link |
| Pharmacy | FEFO stock ledger, purchasing, dispensing, returns (only pharmacists dispense) |

**Limits:** no analyser or PACS has been tested; no real video-media test; no pager or nurse-call integration.

## Business

| Feature | What it does |
|---|---|
| Billing | Exact money, tax rules held as data, idempotent payments, refunds; payment links are a labelled simulator |
| Charge capture and collections | Events that never reached an invoice are listed (add to a draft invoice, or mark not billable with a reason); ageing, collected by day and method, what insurers hold |
| Insurance and claim cases | Pre-authorisation, claims, checklists, frozen packets with checksums, receipts |
| Insights | Eleven fixed metrics with charts and a table view for each; a patient-journey funnel; a closed catalogue, no generated SQL |
| Setup | Facilities, wards, formulary, tax rates, payers, targets and assistant switches, with a first-run checklist |

## Patients and follow-up

| Feature | What it does |
|---|---|
| Portal | A patient's own appointments, medicines, released results, visit summaries, home collection visits (without the address), follow-up and programmes |
| Follow-up | Care plans with reminders, instructions and questionnaires; **approved wording only**, the patient's consent, quiet hours and a daily limit checked at send time; urgent answers go to a named owner |
| Care programmes | A hospital-defined programme (measures and the ranges its own clinicians set), enrolment, readings from staff, the patient or an analyser, a coach queue, adherence, a task for each reading outside range, optional approved reminders |
| Messages | Staff messaging (direct, team, handover, patient threads) and patient-to-clinic messages |
| Video visits | Signed Jitsi links with strict who-and-when rules |

**Limits:** WhatsApp is a labelled simulator; programmes carry no advice, scores or interpretation; no device connects directly.

## Live and connected

| Feature | What it does |
|---|---|
| Live screens | Boards, queues and the dashboard update as things happen; no patient data in events; polling fallback |
| Alerts that need a person | A critical lab result, a red-triage arrival or an urgent message stays on screen until acknowledged; an editable ladder tells the next group |
| Tasks | One list for "someone must do this", with owners, escalation and history |
| Email and SMS | Pluggable and off by default; reminders only to patients who agreed |

**Not a certified paging system:** email and SMS delivery has been verified only to local test sinks.

## Assistants

| Feature | What it does |
|---|---|
| Drafts | SOAP drafts, summaries, coding suggestions, document extraction, medicines read from a scan, conditions to consider (each must quote the note), an operations brief |
| Propose-only assistants | Discharge, claims, handover and patient-reply assistants: read-only tools under the caller's permissions, every cited id checked, a person accepts a suggestion as a task or dismisses it; off until an administrator turns each on |
| Review | Every clinical draft needs a named human review bound to the clinician's own note revision |

**Limits:** off by default, on a private OpenAI-compatible server. **No model has been clinically validated and no accuracy figure is claimed.**

## Integration and standards

| Feature | What it does |
|---|---|
| Integration hub | HL7 v2 ADT and results by connector token, stored raw and de-duplicated, mapped by versioned rules, matched to patients by identifier only; uncertain matches wait for a person; replay |
| Analysers | ASTM E1394 over HTTPS and over a TCP link, translated to the same intake; tested only with simulated instruments |
| FHIR R4 | Read-only: Patient, Encounter, Observation, AllergyIntolerance, MedicationRequest, Appointment, `$everything` |
| OpenAPI | One document and a typed client; 457 operations |
| API keys and webhooks | Read-only role-scoped keys; signed outbound webhooks, off until an operator switches them on |
| Edge | TLS, flood limits, a mutual-TLS listener for connecting systems, and an optional browser client-certificate gate |

## Governance

| Feature | What it does |
|---|---|
| Roles | Thirteen roles, deny by default, plus relationship and facility checks (76 permissions) |
| Audit | Viewer with chain verification; every read and change of a record is recorded (metadata only) |
| Privacy | A privacy impact assessment and an honest compliance gap list exist in the product documentation |

Back to the [documentation index](README.md).
