# Coming in the next release

**Pilot-ready software, not a certified medical product. Synthetic data only.**

These modules are built and tested on the main branch of ZYVORA and are **not in the latest release (0.5.2)**. Each one follows the same rules as the rest of the product: every action needs a permission (deny by default), restricted patients need a reasoned break-glass, one hospital never sees another's records, and records that must not change are append-only in the database as well as in the application. Nothing here sends data to any outside system, and nothing here is certified or clinically validated.

Each entry says what the module does, then what it refuses, so the limits are as visible as the features.

## Public health and programmes

### Notifiable diseases and public-health reporting

The facility keeps its own list of notifiable conditions, each with a deadline class (immediate: 24 hours, weekly: 7 days). Doctors, nurses and lab technicians notify a case against an active condition with basis, onset date and notes, and the case gets a due time from the moment of notification. The administrator works the queue (pending first by due date, overdue computed), marks each case reported to the health authority (with an optional reference) or withdrawn (with a reason), and exports a de-identified line-list CSV by onset date (no names or patient ids, formula-safe cells, withdrawn cases left out, each export audited). It refuses an unknown or switched-off condition, a future or year-old onset, a second outcome on one case, a restricted patient without break-glass and anything from another hospital. Notifications and outcomes are append-only in the database, conditions are never deleted. Nothing is transmitted to any authority.

### Birth and death registration

Birth notifications are drawn up from the maternity delivery summary and tracked draft, submitted, registered by hand, with the registry's number typed in. Death certificates carry an ICD-10 cause-of-death chain (lines a to d), are certified by one doctor and verified by a different one (checked in the route and in the database), and are voided with a reason rather than edited. A stillbirth variant belongs to the mother's delivery. Printable worksheets and an anonymous register by year are included. Status changes go to an append-only log. It refuses to send anything to a registry, to let a certifier verify their own certificate, to edit or delete records, and to show restricted patients without break-glass.

### Infection control

Nurses and administrators open healthcare-associated infection surveillance cases (CLABSI, CAUTI, SSI) with the device or procedure, onset date and criteria met; the status history is append-only and a case is decided exactly once, confirmed or ruled out, with a note. A case with no criteria cannot be confirmed. They also start and end isolation precautions (one active flag per patient and precaution, ended once), record hand-hygiene observations by WHO moment, log colour-coded biomedical waste in grams and record vendor pickup manifests with a unique manifest number. A monthly report gives counts only: cases by type and status, confirmed HAIs per 1000 device-days or procedures when the caller supplies the denominator, hand-hygiene compliance, and waste logged against waste collected. Doctors read; everyone else is refused. A restricted patient needs break-glass, another hospital sees nothing, and nothing is submitted to a regulator.

### HMIS report export

An administrator maps seven fixed count indicators (completed and missed appointments, admissions, discharges, inpatient deaths, completed lab orders, patients registered) to DHIS2-style data element, category option combo and organisation unit identifiers, then builds a monthly report. The counts are snapshotted as a dataValueSet and start as pending approval. A different administrator must approve or reject with a note, and only an approved report downloads as JSON or CSV. Each download is audited and written to an append-only log. It refuses malformed identifiers, future or malformed periods, a build with no mapping, approval by the person who built the report, a second decision, and download before approval. Mappings and decided reports cannot be edited or deleted, and another hospital sees nothing. There is no live push, no disaggregation and no small-cell suppression.

### Programme tracing

Adds cadence-only register templates (HIV/ART, TB, malaria) that create ordinary programmes on the programmes engine, contact lists for an enrolment, and a lost-to-follow-up queue with append-only trace attempts (channel, outcome, note) and a closure that needs an outcome and a reason of at least 3 characters. Templates carry no target ranges or treatment rules, and nothing is sent to anyone. It refuses tracing on inactive or already-closed enrolments, a second closure, future test dates and unknown channels or outcomes. Restricted patients are left out of the queue and need break-glass to trace, other hospitals see nothing, and attempts, closures and contacts cannot be edited or deleted.

### Immunisation schedules and defaulter lists

A hospital authors its own schedule (vaccine, dose number, earliest age, minimum interval from the previous dose, grace period, optional upper age) and the system computes due and overdue lists from each child's date of birth and the completed doses already in the chart, plus a defaulter view, per-vaccine session tallies (doses given and wasted, with a one-way void and a counts-only summary with wastage percentage) and a print-friendly child health card showing each dose as given, due, overdue, upcoming or waiting. Schedule doses never change (retire and re-author), tallies are never edited, restricted patients are off the lists and need break-glass for the card, other hospitals see nothing, and short reasons are refused with 422. Vaccine stock by lot and a registry export file are not included.

## Ward safety and clinical workflow

### Nursing risk assessments and ward risk board

A nurse scores a bedside scale for an encounter: Morse falls, Braden pressure injury, MUST nutrition, pain rating, Barthel daily living or Padua VTE. The scales and their scoring are fixed in code, so the same answers always give the same score and risk band, and each assessment is stored append-only with its answers (a newer one supersedes the last). The band sets the reassessment due time and creates a task for the ward nurses, replacing the previous open one for that scale. The ward risk board lists admitted patients by ward and bed with the latest band per scale, overdue reassessments, and the falls reported in incidents since admission, plus name-free counts per scale and band. Nurses score; nurses, doctors and the administrator read. It refuses an unknown scale, a missing, unknown or unlisted answer, and a note under 3 characters ; a restricted patient needs break-glass and is left off the board without one; another hospital sees a "not found" answer. The scores are nursing aids, not clinically validated or certified here.

### Early warning scores (NEWS2)

: when a vital sign is saved and all seven NEWS2 parameters were charted within the last hour, the adult NEWS2 score is computed from a fixed table and written append-only with its band (low, low-medium, medium, high), a red-flag marker for any single parameter at the hospital's trigger, and the next observation due. Administrators set the escalation thresholds and observation intervals (a new version with a reason; the latest applies). A medium or high band, or a red flag, raises one urgent escalation task, reused while it stays open. Score trends per encounter and a ward board. Advisory decision support only: not certified or clinically validated.

### Advance directives, code status and goals of care

A doctor records a patient's code status (full code, DNR, DNI, DNR and DNI, comfort care, limited treatment), the directive on file, goals of care, a substitute decision maker and a mandatory review date; every change is a new numbered version, the database refuses any update or delete, and the history stays. Doctors, nurses, discharge coordinators and administrators read it; only doctors write. The chart shows a banner (a patient with nothing recorded reads "none recorded", never full code), the ED board and ward bed board show a code-status chip, and /directives lists current statuses with a review-overdue filter, patient ids only and no names. A restricted patient needs break-glass, another hospital sees nothing, a past or more-than-a-year-away review date or a short reason is refused with 422, and the code status blocks no order or workflow.

### Elective waiting list

A patient is put on the list for a procedure with a specialty, an urgency category from 1 to 4 and a target in days (defaults 30, 90, 180 and 365, adjustable per entry). The clock is derived from an append-only event log: it starts on the referral date, can be paused and resumed (paused days do not count) and is stopped with a controlled outcome, after which the entry is final. The list shows days waited, days remaining and the breach date; a forecast counts entries by urgency that have breached or will within 14 and 28 days (no names); a validation worklist lists open entries with no activity for N days and a recorded validation clears them; and a CSV reporting extract carries no names, record numbers or free text and is audited. Reading needs read access (doctor, nurse, receptionist, theatre coordinator, administrator), changing needs write access (receptionist, theatre coordinator, administrator). Restricted patients need break-glass to be added and are invisible without a grant, other hospitals see nothing, and the database refuses edits, deletes, out-of-order clock events and anything after a stop.

### Clinical handover (ISBAR)

A doctor or nurse writes a structured Identify, Situation, Background, Assessment, Recommendation handover for a currently admitted patient at shift change or transfer, optionally addressed to a named colleague, and the receiving clinician acknowledges it with an optional note. Content is never edited: a correction is a new handover that supersedes a still-waiting one (once, by its sender only), and an acknowledged handover is final. It refuses handovers for patients no longer admitted, an empty or too-short field , sending to yourself, acknowledging your own handover or one addressed to someone else, acknowledging a superseded one, and restricted patients without break-glass; other hospitals see nothing. Row-level security, append-only triggers, audit on every action. Ward screen at /handovers.

### Open disclosure and serious event review

Attached to an incident, the administrator records disclosure conversations (to patient, family, guardian or representative), corrective actions with an owner and due date whose status changes are appended as events, and serious event reviews (root cause analysis or morbidity and mortality) with a panel, findings and sign-offs. All five tables are append-only and isolated per hospital. It refuses incidents with no linked patient for disclosure, past due dates, non-staff owners or panel members, backward action status moves, a second review of the same kind, a repeat sign-off by the same person, a review before triage, and restricted patients without break-glass. Only the hospital administrator has access.

### IT safety self-assessment and downtime drill register

The administrator keeps a checklist of information-system safety items in four areas (access control, audit review, backup restore, cyber continuity), each with an owner, a status (not assessed, met, partly met, not met) and evidence text; every review is kept in an append-only history. Downtime drills (date, scenario, participant count, duration, findings, optional paper form) are recorded once and never change, and four static printable paper fallback forms are served for registration, medication, lab requests and a downtime log. Route checks refuse short text with 422, future-dated drills, owners who are not staff, and duplicate items; every route needs read or write access (administrator only), and it is a self-assessment record, not a certification.

### Prescription documents

A doctor turns an approved prescription of their own into a numbered e-prescription document (RX-2026-000001) carrying the prescriber's primary licence from the regulator registry as it was on the day, a frozen copy of the items, a validity window (30 days by default, up to 180) and a random 12-character verification code that is shown once, only its SHA-256 hash being stored. A pharmacist presents the code at the verify step, which under a lock marks the document dispensed exactly once (of two simultaneous presentations one wins and the other gets 409, backed by a unique index). It refuses a draft prescription, a doctor without a current licence, a second live document, a dispensed, cancelled or expired document, and a restricted patient without break-glass; refused attempts are audited and consume nothing. Documents and their events (issued, printed, dispensed, cancelled) are append-only. No national submission adapters, no QR image.

### Telemedicine guideline workflow

For a telemedicine appointment the doctor records, once and append-only, the mode (video, audio, chat), first visit or follow-up, who gave consent and that consent was explicitly confirmed, with the doctor's HR registration number copied in on the day; the room view shows that registration to the patient. An administrator keeps a tele-formulary of drug terms allowed in a first-visit and/or follow-up tele-consult (entries are retired with a reason, never edited or deleted). Creating or revising a prescription on a telemedicine encounter is refused until consent is recorded and unless every medicine is on the formulary for that visit type; an empty formulary allows nothing. It refuses consent from anyone but the appointment's doctor, a doctor with no active registration, a first-visit claim when the patient was seen by that doctor in the last 180 days (and a follow-up claim when not), a second record for one appointment, restricted patients without break-glass, and any view from another hospital. Record-keeping only; not a legal opinion or certification against a national guideline.

### Mental capacity, safeguarding and restrictive practice records

Decision-specific capacity assessments record the four functional tests and derive the outcome (has capacity only if all four are met); they are append-only, corrected by addenda. Legal authorisations (DoLS-style, mental health order, guardianship) carry start and expiry, can only be ended once, and an expiring list shows those due within N days or already expired. Clinicians raise safeguarding concerns write-only; only the administrator reads the log, every read is audited, and restricted patients stay hidden without break-glass. A restraint and seclusion register takes append-only observations while an event is open, ends only with a debrief, and a monthly report gives counts and minutes by kind with no names or free text. It refuses edits to assessments, concerns and observations, ended authorisations and events, unknown or other-hospital patients, and reasons under three characters. It is not certified or legal advice.

### Medical device vigilance and UDI traceability

A hospital-wide register of implanted devices (kind, manufacturer, model, UDI-DI, lot, serial, expiry, patient), with a pasted GS1 UDI such as (01)...(17)...(10)...(21)... read into its fields, and a repeatable copy of implantable cath-lab devices into the register. The quality officer enters manufacturers' field safety notices by UDI-DI and/or lot; saving a notice matches it to registered devices (and a device registered later is matched against existing notices), each match is resolved once with a note, and a vigilance report can be drafted as text for a person to edit. It refuses a notice that names neither a UDI-DI nor a lot, a duplicate notice reference, a malformed UDI, a future implant time, short notes , a restricted patient without break-glass, and a second resolution. The register and notices are append-only, matches are never deleted, nothing is sent to any regulator or manufacturer, and another hospital sees nothing.

## Identity, language, codes and records

### Regional patient identifiers and social name

The identifiers panel now accepts six more kinds with public check rules: Singapore NRIC/FIN (check letter), Malaysian MyKad (valid birth date), Thai national ID, Brazilian CPF and Chilean RUT (check digits), and Saudi Iqama/national ID (Luhn). Dots, hyphens and spaces are ignored; the existing masking, audited reveal, one-patient-per-number and desk lookup apply unchanged. A patient can also have a social (preferred) name, shown beside the legal name and never replacing it. It refuses a number that fails its check, a country on a regional kind, a number already held by another patient, and a social name outside 2 to 120 characters; the name and the numbers never reach the audit trail. Format only: nothing is looked up at any registry, and Aadhaar stays excluded.

### Regulator registrations

: clinician licence registrations (regulator body such as NMC, SMC, GMC, DHA, SCFHS, MMC or CRM; number, specialty code, issue and expiry dates, one active primary licence per person) and facility registrations tied to the facilities module, with an optional hospital setting, off by default, that blocks work without a licence. Numbers are checked for plausible shape for their regulator only; nothing is verified with a regulator and nothing here claims certification.

### Medical certificates

: a doctor with a recorded licence number issues a sick-leave, fitness, travel or visa certificate with a per-hospital, per-year serial, the licence number as it was that day, the period covered and a random verification code with a public check page. Certificates and their events are append-only; a void by the administrator or records officer needs a reason and a voided certificate cannot be printed. The licence number is self-declared and not checked with any council.

### Code catalogue and coder workbench

The administrator loads diagnosis and procedure code sets with validity dates (or a built-in synthetic sample subset) and picks each facility's edition. Doctors and coders search the editions in force and check codes as ok, unknown, not valid on the date, or bad shape. A coder queue lists discharged admissions with their coding state, a saved coding can be checked against the facility's edition on the discharge date, and the coder raises queries that only the attending doctor answers, once. Loaded sets, edition choices, queries, answers and the change audit are append-only. It refuses wrong-shaped or duplicate codes, restricted patients without break-glass, and any cross-hospital access.

### Record export (patient summary document)

A doctor, records officer or administrator can build a patient's summary as a FHIR R4 document Bundle shaped like an International Patient Summary (a Composition with allergies, problem list, medications from approved prescriptions as MedicationStatement, immunisations and results, empty sections kept with an empty reason) and issue it as an export. An export is refused unless the patient has an effective data-sharing consent, or if the document fails the local structural checks (required sections, reference integrity, per-resource checks); every attempt, issued or refused, is written to an append-only log with who asked, why, the consent relied on, per-section counts and the SHA-256 of what was issued, never the clinical content. Restricted records need break-glass and another hospital's patient is a "not found" answer. The checks are local only: no claim of HL7 IPS or EHDS conformance, and ZYVORA sends nothing to any receiving system.

### Language access

A patient now carries a preferred language and an interpreter-needed flag, set by the front desk or a nurse, and an append-only interpreter request log records who asked for which language and mode (in person, phone, video) and why. The web app gains a minimal locale framework: a locale provider that switches the page to right-to-left, Intl date and number formatting, and draft Arabic and Hindi catalogues for the language-access screen only; every translation is marked a draft pending review. It refuses unknown language codes, reasons under 3 characters, any edit or delete of the request log, restricted patients without break-glass, and any access from another hospital. Translated print templates are not included.

### Terminology service, phase 1

The hospital imports the concept tables it is licensed to use (LOINC, SNOMED CT, dm+d, RxNorm or any coded list) as a CSV, with synonyms, and no licensed content is bundled. Staff search by name, synonym or code; the administrator binds a local lab test to a LOINC concept or a medicine to a SNOMED CT, dm+d or RxNorm concept in an append-only crosswalk (one binding per item per system), and an unmapped report lists active catalogue items still without one, flagging lab units that are not valid UCUM. A small built-in UCUM grammar checks unit spelling. It refuses an import with any bad row as a whole, a lab test bound to anything but LOINC, an unknown or inactive concept, a second binding in the same system, edits or deletes of crosswalks, synonyms and the import log, and anyone but the administrator importing or binding. Other hospitals see nothing.

## Privacy, governance and quality

### Data-subject rights and breach register

The hospital administrator sets the privacy regime (GDPR, DPDP, POPIA, NDPA, PDPA, HIPAA or a custom set of days and hours) and then logs access, rectification, erasure, restriction and objection requests, each with a due date fixed from the regime on the day it was received, an identity check, notes, and a closing outcome with a reason. A request cannot be recorded as fulfilled until the requester's identity is verified, and a closed request is final. Breaches are recorded with severity, an estimate of people affected and the time detected; the regulator and patient notification deadlines start from detection, and append-only events (assessed, regulator notified, patients notified, closed) move the record forward only, with a notification time recorded once. Privacy notice versions are published and never edited. An overdue list and a summary give identifiers, dates and counts only, with no names or free text. It is a record only, not legal advice: it does not erase, restrict, export or notify anything, and the periods are defaults to confirm with counsel. Nothing works until a regime is set, a restricted patient needs break-glass, other roles and other hospitals are refused, and every action is audited.

### Records governance

A register of processing activities, one retention rule per record class (mrd_folder, consent_record), a due-for-disposal view that flags records under legal hold, legal holds on a patient or a record class (placed and released as separate append-only events), and two-person disposal certificates. A disposal is refused when no rule exists, the cutoff is inside the retention period, nothing qualifies, or any record in range is held. The hold check is repeated at approval, and the person who asked cannot approve. Records decisions only; nothing is deleted.

### Release of information: disclosure ledger and withheld items

The records officer and hospital administrator record each disclosure of a patient's record outside treatment, payment and operations, with recipient, purpose, legal basis and what was released, and print an accounting for the last one to six years (default six). Items kept from the portal are logged with the exception that applies and a written reason, and the portal release rule for each result type (release, delay 1 to 720 hours, or withhold) is set as a new numbered version, with withholding refused unless an exception reason is given. All three tables are append-only in the database. Restricted patients need break-glass, another hospital sees nothing, and reasons under three characters, unknown codes and future or twenty-year-old disclosure dates are refused with 422. Rules are recorded but do not yet gate the portal.

### Medico-legal case register

A doctor registers a medico-legal case for a patient with MLC number, nature, who brought the patient, injury description and police intimation (station, time, recorder). Cases are never edited; injury findings, later police intimation, notes and closure are appended as amendments. Samples are sealed once with a unique seal number, and every hand-over is appended to a chain of custody. Access is read and write access, held by the doctor only. A restricted patient's cases are hidden without break-glass, reads are audited, another hospital sees nothing, and a closed case refuses amendments and new samples.

### Quality indicators and accreditation readiness

The administrator sees four measures computed live from existing data (falls per 1000 bed days, medication incidents per 1000 doses given, 30-day readmission, MAR doses given late or still overdue) as numerator, denominator and rate, with drill-down to record, patient and admission ids only, and can store an append-only snapshot of the figures for an ended period. The hospital types in its own NABH, JCI, CBAHI or NSQHS clauses, links append-only evidence (document, route, record, measure), and raises mock-audit findings that close once with a resolution. It refuses everyone but the administrator (read and write access), hides a restricted patient's id without break-glass, rejects short notes, bad frameworks and periods over two years, never deletes or rewrites evidence, snapshots or what an audit found, isolates each hospital by row-level security, and states on every response that it is readiness information and not an accreditation.

## Money and statutory rules

### Statutory controlled-drug registers

Drugs get a schedule (H, H1, X, NDPS); H1, X and NDPS are always controlled. Prescribers carry a registration number and council. The prescriber of an approved prescription takes a gapless numbered controlled prescription (CD-year-nnnnnn) with a validity window of up to 30 days, refused without a registration number. Dispensing an H1, X or NDPS drug is refused without a number inside its window. The controlled register can be exported as CSV for an inspector only after a second person approves; the file is available for one hour, downloads once, holds no patient or names, and is audited.

### Statutory discounts, exemptions and fee waivers

The front desk records a patient's entitlement (senior, disability, indigent or under-5) with an evidence reference and a validity range, and requests a discount, exemption or waiver on an invoice, as a fixed amount in paise or a percentage of the invoice total. The hospital administrator approves or rejects it. The requester can never decide their own request, and the database refuses it too. A hospital-set deduction order decides which approved adjustment is honoured first when they add up to more than the bill. A pre-discharge check flags entitlements with no approved adjustment, and an exemption report gives counts and paise by kind with no names. It refuses a statutory kind without a valid, unrevoked entitlement (checked again at approval), adjustments that would exceed the invoice total, paid or void invoices, reasons shorter than 3 characters, editing or deleting an entitlement (it can only be revoked, once), and changing a decided request. A restricted patient needs break-glass, and another hospital sees nothing.

### Mobile money and till reconciliation

The front desk records a mobile-money receipt against an issued invoice by provider (M-Pesa, MTN MoMo, Airtel Money, Orange Money, other) and transaction code; it is a normal payment with method mobile_money, so part payments leave the invoice partially paid and exact settlement marks it paid. The finance administrator imports the provider's statement as CSV (parsed in the API, the raw file is never kept), matches lines to receipts by provider and code (equal amounts matched, different amounts flagged for review), matches by hand or dismisses a line with a reason, and reads a daily till report of collections by payment method and by cashier (user ids, no names, whole minor units). It refuses duplicate codes, card-like digit runs, overpayment, payments on paid or draft invoices, repeated or overlapping statement lines, a receipt matched twice, and any edit or delete of receipts, imports, lines or matches (append-only). Confidential patients' receipts are hidden without break-glass. No gateway: nothing contacts a provider.

### Tariffs: payer rate cards, self-pay price list and non-binding estimates

The administrator adds effective-dated rate cards, an uplift in basis points (negative for a discount) per payer and room class (general, semi-private, private, deluxe, ICU), layered on the charge master and optional named price lists; a card with no payer is the default self-pay card. Cards are versions that supersede the previous one from their date and are append-only in the database. The front desk reads the self-pay price list by room class and totals a labelled non-binding estimate for chosen items, resolving the payer's card, else the default card, else no uplift, with tax and all money in whole paise. A card cannot start in the past or more than two years ahead, duplicates for the same date, short reasons and unknown payers are refused, the estimate stores nothing beyond its audit entry, and another hospital sees none of it.

Back to the [modules overview](MODULES.md) or the [documentation index](README.md).
