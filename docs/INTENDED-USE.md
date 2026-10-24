# Intended use and limits

**Pilot-ready software, not a certified medical product. Synthetic data only.**

We would rather you hear it from us. Each line is stated in the product's own documentation.

| Area | Where it stands |
|---|---|
| **Data** | Built and tested with synthetic data only. |
| **Certification** | Not certified against HIPAA, GDPR, ISO 27001, SOC 2, IEC 62304, NABH/JCI or similar. A gap list is published. |
| **Security review** | No independent penetration test yet. The audit trail is tamper-evident, not tamper-proof against a database owner. |
| **Clinical safety** | No clinical validation of any model. Drug-interaction and dose checks report `unavailable` where there is no drug database; they never say "passed". |
| **Integrations** | FHIR R4 is read-only. Only FluxVM has been verified live; Netra and Nuvora are tested against stand-ins. |
| **Scale** | No load testing yet. Browser tests run in Chrome only, and there has been no screen-reader testing. |
| **Messaging and alerts** | Not a certified paging system: no pager or nurse-call integration. Email and SMS have been tested only against local sinks, never a real provider. |

## Also not built yet

Automated backups, critical-result paging, e-prescription, a payment gateway, patient self-booking, languages other than English, and a native mobile app.

## What this means in practice

- Use it to **evaluate and to run a pilot with synthetic data.** Please do not load real patient data.
- It is **not** a clinical decision tool. The AI is off by default, only drafts, and never decides; a named clinician reviews every draft.
- Real clinical use would need work that has not been done here: clinical validation, the certifications and compliance your jurisdiction requires, an independent security review, load testing, and acceptance of each integration against your real systems.

## Placeholders you will see on the website

Pricing tiers and customer stories are **deliberately unfinished**. Pricing has not been decided and no figure is an offer; ZYVORA has not been deployed with a customer.

Questions: [sales@zyvor.dev](mailto:sales@zyvor.dev) · [security@zyvor.dev](mailto:security@zyvor.dev)
