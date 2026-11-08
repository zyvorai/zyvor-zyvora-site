# Modules

**Pilot-ready software, not a certified medical product. Synthetic data only.**

> **In one minute.** ZYVORA's modules share one patient record, one sign-in, one audit trail and one permission model. This page lists them in two parts: first **the core** that every hospital uses daily, then **every department and specialty**, 82 documented modules in all. Modules marked *next release* are built and tested but not yet in version 0.5.2. Each table says what exists; the limits of a group are stated under it. Unfamiliar words are in the [glossary](GLOSSARY.md).

**Jump to:** [The core](#the-core) · [Every department and specialty](#every-department-and-specialty) · [Coming in the next release](#coming-in-the-next-release)

## The core

### Clinical core

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

### Hospital

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

### Business

| Feature | What it does |
|---|---|
| Billing | Exact money, tax rules held as data, idempotent payments, refunds; payment links are a labelled simulator |
| Charge capture and collections | Events that never reached an invoice are listed (add to a draft invoice, or mark not billable with a reason); ageing, collected by day and method, what insurers hold |
| Insurance and claim cases | Pre-authorisation, claims, checklists, frozen packets with checksums, receipts |
| Insights | Eleven fixed metrics with charts and a table view for each; a patient-journey funnel; a closed catalogue, no generated SQL |
| Setup | Facilities, wards, formulary, tax rates, payers, targets and assistant switches, with a first-run checklist |

### Patients and follow-up

| Feature | What it does |
|---|---|
| Portal | A patient's own appointments, medicines, released results, visit summaries, home collection visits (without the address), follow-up and programmes |
| Follow-up | Care plans with reminders, instructions and questionnaires; **approved wording only**, the patient's consent, quiet hours and a daily limit checked at send time; urgent answers go to a named owner |
| Care programmes | A hospital-defined programme (measures and the ranges its own clinicians set), enrolment, readings from staff, the patient or an analyser, a coach queue, adherence, a task for each reading outside range, optional approved reminders |
| Messages | Staff messaging (direct, team, handover, patient threads) and patient-to-clinic messages |
| Video visits | Signed Jitsi links with strict who-and-when rules |

**Limits:** WhatsApp is a labelled simulator; programmes carry no advice, scores or interpretation; no device connects directly.

### Live and connected

| Feature | What it does |
|---|---|
| Live screens | Boards, queues and the dashboard update as things happen; no patient data in events; polling fallback |
| Alerts that need a person | A critical lab result, a red-triage arrival or an urgent message stays on screen until acknowledged; an editable ladder tells the next group |
| Tasks | One list for "someone must do this", with owners, escalation and history |
| Email and SMS | Pluggable and off by default; reminders only to patients who agreed |

**Not a certified paging system:** email and SMS delivery has been verified only to local test sinks.

### Assistants

| Feature | What it does |
|---|---|
| Drafts | SOAP drafts, summaries, coding suggestions, document extraction, medicines read from a scan, conditions to consider (each must quote the note), an operations brief |
| Propose-only assistants | Discharge, claims, handover and patient-reply assistants: read-only tools under the caller's permissions, every cited id checked, a person accepts a suggestion as a task or dismisses it; off until an administrator turns each on |
| Review | Every clinical draft needs a named human review bound to the clinician's own note revision |

**Limits:** off by default, on a private OpenAI-compatible server. **No model has been clinically validated and no accuracy figure is claimed.**

### Integration and standards

| Feature | What it does |
|---|---|
| Integration hub | HL7 v2 ADT and results by connector token, stored raw and de-duplicated, mapped by versioned rules, matched to patients by identifier only; uncertain matches wait for a person; replay |
| Analysers | ASTM E1394 over HTTPS and over a TCP link, translated to the same intake; tested only with simulated instruments |
| FHIR R4 | Read-only: Patient, Encounter, Observation, AllergyIntolerance, MedicationRequest, Appointment, `$everything` |
| OpenAPI | One document and a typed client; 1,315 documented operations on the main branch (the latest release has fewer) |
| API keys and webhooks | Read-only role-scoped keys; signed outbound webhooks, off until an operator switches them on |
| Edge | TLS, flood limits, a mutual-TLS listener for connecting systems, and an optional browser client-certificate gate |

### Governance

| Feature | What it does |
|---|---|
| Roles | 17 roles and 285 permissions on the main branch, deny by default, plus relationship and facility checks |
| Audit | Viewer with chain verification; every read and change of a record is recorded (metadata only) |
| Privacy | A privacy impact assessment and an honest compliance gap list exist in the product documentation |

## Every department and specialty

Each row is one module with its own page in the product documentation. A module marked *next release* is built and tested but not yet released. Everything here follows the same rules: it needs a permission, restricted patients need a written reason, one hospital never sees another's records, and records that must not change are append-only.

### Wards and nursing

| Module | What it does |
|---|---|
| **Medication rounds** | Nurses record each dose given on the ward, with who gave it and when, so nothing is missed or given twice. |
| **Diet orders** | A doctor or dietitian orders a patient's diet, and the kitchen and ward see one list of who gets what. |
| **Bed cleaning** | When a patient leaves, a cleaning job appears for the housekeeper, so beds are ready faster. Housekeepers see beds, never patients. |
| **Day care** | Same-day stays: booking, who escorts the patient home, a discharge readiness score, and turning the stay into an admission if needed. |
| **Cath lab record** | The record of a catheter procedure: safety checks, the pause before starting, devices and lot numbers, radiation dose and site checks. |
| **Dialysis sessions** | The prescription, each session with machine readings, and nurse sign-off. |
| **Maternity and labour** | Antenatal visits, labour charting with alerts outside safe ranges, the delivery summary and checks after birth. |
| **Cancer treatment plans** | Chemotherapy and radiotherapy plans, cycles, doses checked by a second clinician, and a running radiation total. |
| **Home visits** | Courses of nurse home visits, with concerns flagged for the doctor. |
| **Nursing risk scales** *(next release)* | Falls, pressure sores, nutrition, pain, daily living and clot-risk scores with risk bands, reassessment reminders and a ward board. |
| **Early warning scores** *(next release)* | A standard score from a patient's vital signs that raises one escalation task when it is high. Advice only. |
| **Shift handover** *(next release)* | A structured handover (ISBAR) between staff that the receiver must acknowledge; corrections are new handovers. |
| **Advance directives and code status** *(next release)* | A patient's wishes about resuscitation and care, kept as versions, with a banner on the chart and chips on the boards. |
| **Elective waiting list** *(next release)* | Urgency categories, a clock that can pause, a forecast of who will breach their target, and a name-free report. |
| **Capacity and safeguarding** *(next release)* | Mental-capacity assessments, legal authorisations, a restricted safeguarding log, and a restraint and seclusion register. |
| **Infection control** *(next release)* | Hospital-acquired infection cases, isolation flags, hand-hygiene checks, colour-coded waste logs, and monthly rates. |

### Diagnostics, pharmacy and supplies

| Module | What it does |
|---|---|
| **Blood bank** | Donors, units of blood, screening results and stock levels in one place. |
| **Laboratory extras** | Follows a specimen's journey, handles rejected specimens and tests sent outside, and records quality control. |
| **Radiology extras** | Scanner time slots, safety screening before a scan, and patient arrivals. |
| **Pharmacy stock and sales** | Goods received, reorder alerts, requests from wards and over-the-counter sales. |
| **Supplier invoices** | Supplier invoices matched to what was ordered and received, with tax split and payment. |
| **Pharmacy customers** | Walk-in customers, returns handled as credit notes, and saved sale templates. |
| **Ward stock and controlled drugs** | Stock levels on each ward, scanning barcodes, and a witnessed register of controlled drugs. |
| **General stores** | Non-drug supplies, requests from departments and a stock ledger. |
| **Sterile services** | Instrument sets, sterilisation loads and their indicators, issue to theatre, and recall if a load fails. |
| **Reorder forecasting** | Suggests what to order from past use, flags stock-outs and over-stock, and lists items near expiry. |
| **Controlled-drug rules** *(next release)* | Drug schedules, prescriber registration numbers, numbered prescriptions with validity, and an inspector export approved by a second person. |
| **Prescription documents** *(next release)* | A numbered prescription with the doctor's licence and a validity window, which a pharmacist verifies and dispenses once. |
| **Medical terminology** *(next release)* | Concept lists the hospital is licensed to use, search, and links from lab tests and medicines to the standard codes. |
| **Implants and device recalls** *(next release)* | A register of implanted devices by unique ID, matching safety notices to patients, and a report draft that is never sent. |

### Records, identity and privacy

| Module | What it does |
|---|---|
| **Medical records department** | Tracks paper folders, codes and signs off discharged records, and handles requests for copies. |
| **Diagnosis and procedure codes** *(next release)* | Loadable code sets with validity dates, search, and a coder queue where doctors answer coding queries. |
| **Birth and death registration** *(next release)* | Birth notifications from the delivery record, and death certificates with the cause of death, verified by a second doctor. |
| **National ID formats** *(next release)* | Checks the format of national IDs from Singapore, Malaysia, Thailand, Brazil, Chile and Saudi Arabia, and records a preferred name. |
| **Professional registrations** *(next release)* | Clinician licences and facility registrations with expiry. Format checked only; never verified with the regulator. |
| **Medical certificates** *(next release)* | Numbered sick-leave, fitness, travel and visa certificates anyone can verify with a code. |
| **Patient summary export** *(next release)* | A patient's summary in the international format, issued only with consent and logged. Nothing is sent anywhere. |
| **Records retention** *(next release)* | A register of how data is used, retention rules, legal holds, and disposal certificates signed by two people. Nothing is deleted. |
| **Who was given a patient's record** *(next release)* | A ledger of disclosures with a multi-year accounting, a log of items held back from the portal, and portal release rules. |
| **Privacy requests and breaches** *(next release)* | A register for patients' requests about their data, with due dates and identity checks, plus a breach register with deadlines. |
| **Medico-legal cases** *(next release)* | Injury findings, police intimation, sealed samples with chain of custody; doctors only and never edited. |
| **Language access** *(next release)* | A patient's preferred language, an interpreter-needed flag and request log, and draft Arabic and Hindi screens with right-to-left layout. |
| **Health record sharing** | A patient's health address, consents and a log of shared records. Local only; no connection to the national gateway. |

### Money and statutory rules

| Module | What it does |
|---|---|
| **Doctor payouts** | Works out each doctor's share of collected visit fees and records paying it. |
| **Money owed by insurers** | What each insurer owes, how old it is, payments received and write-offs. |
| **Employer accounts** | Employers send staff for health checks and see their own account, through their own limited portal. |
| **Supplier bills** | A bill is entered, approved by a different person, then paid once. |
| **Discounts and fee waivers** *(next release)* | Statutory discounts and exemptions with evidence, approved by a second person, and checked before discharge. |
| **Mobile money payments** *(next release)* | Records mobile-money receipts, matches them to a statement file, and gives a daily till report. |
| **Price lists and estimates** *(next release)* | Insurer rate cards and a self-pay price list by room class, and a labelled estimate for the front desk. |
| **Tax invoices** *(next release)* | Tax IDs and a tax category on every line, credit notes that chain to the invoice, and unsigned export files. |
| **Insurance claim files** *(next release)* | Insurer file layouts as data, batches checked before export, insurer payment files imported by hand, and denials with an appeal trail. |
| **Case-mix grouping** *(next release)* | Groups discharged stays by rules you load, with case-mix index and length of stay against benchmark. A model, not an official grouper. |
| **Government scheme billing** *(next release)* | Public schemes with co-pay, caps and packages, enrolment, splitting a bill between scheme and patient, and balance alerts. |

### Operations, people and safety

| Module | What it does |
|---|---|
| **Buildings and equipment** | A register of plant and equipment, scheduled maintenance, and breakdown jobs from reported to done. |
| **Staff licences and attendance** | Staff licences and certificates with expiry dates, clocking in and out, and corrections. |
| **Staff rota and leave** | Shifts and leave for staff. |
| **Self check-in kiosks** | Patients check themselves in with a one-time code and their date of birth. Each kiosk can be switched off at once. |
| **Queue tickets** | Numbered tickets for the waiting room and a display that shows whose turn it is. |
| **Patient feedback** | Patients rate their visit, and managers see which areas need attention. |
| **Ambulance dispatch** | Calls, sending a vehicle, the timeline of each trip and which vehicles are ready. |
| **Ambulance care record** | The crew's record of care in the vehicle, the handover at the emergency department, and an alert before arrival. |
| **Referrals and transfers** | Send a patient to another facility in the same organisation, with accept, decline and return. |
| **Patient-safety incidents** | Anyone can report a near miss or harm event; managers triage, investigate and close it. |
| **Serious event review** *(next release)* | Open conversations with the patient or family, corrective actions, and a formal review with sign-off. |
| **IT safety and downtime drills** *(next release)* | A self-assessment of IT safety, a record of downtime drills, and printable paper forms for when systems are down. |
| **Bed and staffing forecast** | Predicts occupied beds and emergency arrivals, shows how wrong past forecasts were, and flags days the rota falls short. |
| **Bedside device readings** | Bedside monitors send readings that attach to the right patient, with alerts for critical values. |
| **Device alerts and trends** | Per-patient and children's alert limits, alerts when a device goes silent, trends, and infusion pumps and ventilators. |

### Insight and public health

| Module | What it does |
|---|---|
| **Hospital scorecard** | One page of totals across the departments, with no patient names. |
| **Saved dashboards** | Build and share dashboards, compare periods, set targets and export figures. |
| **Anonymous data exports** | Counts exported as files with no names or identifiers, and small groups left out. |
| **Quality and accreditation readiness** *(next release)* | Live quality measures, your own accreditation checklist with evidence, and mock-audit findings. Not an accreditation. |
| **Antibiotic resistance** | Which germs resist which antibiotics, rates by ward and period, and a signal when cases cluster. |
| **Notifiable diseases** *(next release)* | The hospital's list of diseases it must report, with deadline clocks, a case queue and an anonymous list for the health authority. |
| **Health statistics report** *(next release)* | Monthly counts mapped to national indicator IDs, approved by a second administrator, then downloaded as a file. |
| **HIV, TB and malaria follow-up** *(next release)* | Register templates, contact lists, and a list of patients who missed follow-up with logged attempts to reach them. |
| **Immunisation schedules** *(next release)* | The hospital's own schedule, who is due or overdue, doses given and wasted, and a printable child health card. |
| **Telemedicine rules** *(next release)* | Consent and visit type recorded for each tele-visit, the doctor's registration shown, and prescribing limited to an approved list. |

### Everyday and branding

| Module | What it does |
|---|---|
| **Your name and colour** | Your organisation's name and accent colour on screens and documents. |
| **Starred patients** | A private shortcut list of patients you follow. |
| **Thank-yous** | Colleagues can send each other thanks. |



## Coming in the next release

37 of the modules above are built and tested on the main branch and are **not in the latest release (0.5.2)**. They are described one by one, with what each refuses and where its limits are, in the **[next-release guide](NEXT-RELEASE.md)**. Same limits apply: pilot-ready, synthetic data only, not certified, and nothing here sends data to any outside system.

Back to the [documentation index](README.md).
