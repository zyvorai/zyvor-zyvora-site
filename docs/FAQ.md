# FAQ

**Pilot-ready software, not a certified medical product. Synthetic data only.**

> **In one minute.** ZYVORA is hospital software you run yourself. It is built and tested with invented data, it is not certified, and its AI only drafts; a named person always decides. Below are the questions people ask first, answered plainly. Words in *italics* are in the [glossary](GLOSSARY.md).

**Jump to:** [About ZYVORA](#about-zyvora) · [Safety and the AI](#safety-and-the-ai) · [Data and security](#data-and-security) · [Running it](#running-it) · [Connecting other systems](#connecting-other-systems) · [Versions](#versions) · [Cost and customers](#cost-and-customers)

## About ZYVORA

### What is ZYVORA?
Software for running a hospital or clinic: patient records, appointments, the emergency board, wards and beds, theatre, laboratory, imaging, pharmacy, billing and insurance, plus follow-up after the visit. 99 modules are documented; see [Modules](MODULES.md).

### Is ZYVORA a certified medical product?
No. It is pilot-ready software built and tested with synthetic (invented) data. It carries no regulatory certification and no clinical validation, and a published gap list says what is missing. See [Intended use and limits](INTENDED-USE.md).

### Can I use it with real patients?
Not yet, and please do not load real patient data. Real clinical use would need work that has not been done: clinical validation, the certifications your country requires, an independent security review, load testing and acceptance of each connection to your real systems.

### Can I try it without installing anything on a server?
Yes. The [demo](GETTING-STARTED.md) runs on your own computer with one command, uses invented patients and is removed with one command. Nothing leaves your machine.

### Is there a mobile app?
A first version for iPhone and Android is being built, and it has **never been run on a phone**. It is not released. The web app works in a phone browser and can keep note drafts when the connection drops (encrypted on the device for at most 12 hours).

### Which languages does it speak?
English. A first set of draft Arabic and Hindi screens, with right-to-left layout, is in the [next release](NEXT-RELEASE.md#identity-language-codes-and-records) for one screen only, and every translation is marked a draft pending review.

## Safety and the AI

### Does the AI make clinical decisions?
No. It is **off by default**, produces **drafts only**, and cannot order, prescribe, sign or contact a patient. A named clinician must review a draft before it counts, and the review is tied to that clinician's own note revision. There has been no clinical validation of any model.

### What does "propose-only" mean?
Four helpers (discharge, claims, handover and patient replies) read what the signed-in person may read, cite what they read, and leave a *suggestion*. A person accepts it as a task or dismisses it. They cannot send, order, sign or submit anything, and each is off until an administrator turns it on.

### Where does the AI run, and what does it see?
On a private server you control, never a public service by default. Names, record numbers, phone numbers and similar identifiers are replaced before text leaves the application. That reduces exposure; it is not full anonymisation.

### Can we use our own models or Nuvora?
Any server that speaks the common OpenAI-style interface works. Nuvora, a self-hosted AI platform with that interface, is the preferred back end, but its connection has been checked only against Nuvora's offline demo provider, not a live language model.

### Do the scores and alerts replace clinical judgement?
No. Early warning scores, nursing risk bands, triage suggestions and similar aids are **advisory**. They use fixed, published rules, they are not clinically validated, and clinicians stay responsible.

## Data and security

### Where does our data live?
On infrastructure you run: a PostgreSQL database behind the ZYVORA service. Each organisation's rows are separated by the database itself (*row-level security*), not only by the application. Optional AI runs on a private server you choose.

### How do people sign in?
Through your organisation's own identity provider, using OpenID Connect with PKCE. ZYVORA never sees a password. In the **demo**, every user is invented and needs no password.

### Who can see what?
There are 19 roles and 323 separate permissions, and everything is **denied unless a role allows it.** Some actions need more than permission: only a patient's own doctor signs their note, only the ordering clinician releases a lab result. Records marked restricted open only through *break-glass* with a written reason, which an administrator reviews.

### Can anyone change the history?
Signed notes, results, payments, stock movements and the audit trail are *append-only*: corrections are new entries, never edits. The audit trail is also chained, so tampering is detectable. It is tamper-evident, not tamper-proof against someone who owns the database.

### Has it been security tested?
There is an automated test suite (953 Rust tests and 88 web unit tests at the last full run) and automated accessibility checks. There has been **no independent penetration test**, no load test and no screen-reader testing. Details: [Security overview](SECURITY-OVERVIEW.md).

## Running it

### What does it run on?
Docker Compose on one host, a Helm chart for Kubernetes, or a k3s deployment with an Envoy edge. PostgreSQL 14 to 18. One service, one database, a web app.

### How do we back it up?
The installer has `backup`, `restore` (which also checks the audit chain) and `upgrade` (which rolls back on failure) commands for a single host. Scheduled backups, monitoring and recovery drills are yours to arrange. See [Releases](RELEASES.md#upgrade-back-up-restore-remove).

### Can I see the source code or the full documentation?
The product source is private. This repository publishes the website, the installer, the release notes and these pages. Ask [sales](mailto:sales@zyvor.dev) what can be shared with evaluators.

## Connecting other systems

### Can we connect it to other systems?
Yes, in these ways, all tested only against simulated or written examples, never a real hospital system:
- **FHIR R4**, *read-only*: Patient, Encounter, Observation, AllergyIntolerance, MedicationRequest, Appointment and everything-for-a-patient. It has not been run through the official validator.
- **HL7 v2 and ASTM** messages from other systems and laboratory analysers, held for a person to check when a patient cannot be matched.
- **A documented HTTP interface** (1,509 operations, one OpenAPI description) with read-only keys and signed outgoing webhooks, off until switched on.

Nothing in ZYVORA sends records to a national system, regulator, payer or tax authority by itself. Several modules in the [next release](NEXT-RELEASE.md) build the files or messages and let a person send them.

## Versions

### What is in the latest release, and what is not?
The latest release is **0.5.2**. 54 more modules are built and tested but not yet released; they are listed one by one in [Next release](NEXT-RELEASE.md), and each carries a "next release" label in [Modules](MODULES.md).

### How do I know my download is genuine?
The installer checks a SHA-256 fingerprint against the release's `SHA256SUMS` and refuses to run on a mismatch. You can check by hand too: [Verify your download](RELEASES.md#verify-your-download).

## Cost and customers

### What does it cost?
Pricing has not been decided. The website shows a layout only and no figure is an offer. To discuss a pilot: [sales@zyvor.dev](mailto:sales@zyvor.dev).

### Has a customer used it?
Not yet. There are no customer stories, and the website says so.

### Who do we contact?
[sales@zyvor.dev](mailto:sales@zyvor.dev) for pilots and demos · [security@zyvor.dev](mailto:security@zyvor.dev) for security.
