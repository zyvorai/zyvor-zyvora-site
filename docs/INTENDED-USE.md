# Intended use and limits

**Pilot-ready software, not a certified medical product. Synthetic data only.**

> **In one minute.** Use ZYVORA to **evaluate it and to run a pilot with invented data.** Do not put real patients in it. It is not a clinical decision tool, it is not certified, and no AI model in it has been clinically validated. We would rather you hear that from us. Every line below is stated in the product's own documentation.

## Where things stand

| Area | Where it stands |
|---|---|
| **Data** | Built and tested with synthetic data only. |
| **Certification** | Not certified against HIPAA, GDPR, ISO 27001, SOC 2, IEC 62304, NABH/JCI or similar. A gap list is published. |
| **Security review** | No independent penetration test yet. The audit trail is tamper-evident, not tamper-proof against a database owner. |
| **Clinical safety** | No clinical validation of any model. Drug-interaction and dose checks say `unavailable` where there is no drug database; they never say "passed". Scores and alerts are advisory aids. |
| **AI** | Off by default, drafts only, review is mandatory. No accuracy figure is claimed. |
| **Connections to other systems** | FHIR R4 is read-only. Only FluxVM has been verified live; Netra and Nuvora are tested against stand-ins. HL7 and ASTM have been tried with written messages and simulated instruments only. |
| **Sending to outside bodies** | Nothing sends records to a regulator, registry, payer, tax authority, scheme or national exchange. Modules build the file or message and a person sends it. The national-exchange profiles are working approximations, not certified specifications. |
| **Scale and testing** | No load testing. Browser tests run in Chrome only. No screen-reader testing. |
| **Messaging and alerts** | Not a certified paging system: no pager or nurse-call connection. Email and SMS were tested only against local test sinks, never a real provider. |
| **Reference content** | Code sets, terminologies, DRG rules, payer file layouts, accreditation clauses, tax rules and scheme packages are supplied by the hospital. Only small synthetic samples are built in. |

## Also not built yet

- Transmission of prescriptions. Numbered prescription documents arrive in the [next release](NEXT-RELEASE.md#ward-safety-and-clinical-workflow), but none is transmitted.
- A real payment gateway (payment links are a labelled simulator) and WhatsApp Business.
- A live connection to the ABDM gateway, or any national exchange.
- Patient self-booking.
- Scheduled backups with monitoring (the installer has backup and restore commands).
- Full translation of the interface (draft Arabic and Hindi for one screen are in the next release).
- A released native mobile app (a first build has never been run on a phone).
- Tumour-board meetings, a DICOM worklist service (C-FIND) and MPPS.

## What this means in practice

- **Do** use it to evaluate, to train staff on invented patients, and to run a pilot with synthetic data.
- **Do not** load real patient data.
- **Do not** treat it as a clinical decision tool. The AI is off by default, only drafts, and never decides; a named clinician reviews every draft. Scores and alerts inform people; they do not replace them.
- **Before any real clinical use** you would need work that has not been done here: clinical validation, the certifications and compliance your jurisdiction requires, an independent security review, load testing, and acceptance testing of each connection against your real systems.

## Placeholders you will see on the website

Pricing tiers and customer stories are **deliberately unfinished**. Pricing has not been decided and no figure is an offer; ZYVORA has not been deployed with a customer.

Questions: [sales@zyvor.dev](mailto:sales@zyvor.dev) · [security@zyvor.dev](mailto:security@zyvor.dev) · Unfamiliar word: [glossary](GLOSSARY.md)
