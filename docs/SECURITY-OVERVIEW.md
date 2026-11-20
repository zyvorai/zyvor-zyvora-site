# Security overview

**Pilot-ready software, not a certified medical product. Synthetic data only.**

> **In one minute.** ZYVORA is built so the database itself keeps hospitals apart, nothing is allowed unless a role allows it, and every change leaves a trail that cannot be quietly rewritten. It has **not** been independently tested or certified, and it has only ever held invented data. Below, each protection says what it means in everyday terms, and what has not been done is listed just as plainly. Special words are in the [glossary](GLOSSARY.md). To report a vulnerability, read [SECURITY.md](../SECURITY.md).

## Controls you can point at

| Area | What is in place | What that means |
|---|---|---|
| **Keeping hospitals apart** | Row-level security is **forced** on every table that belongs to an organisation, and the application connects with a database role that cannot bypass it. (Shared tables, such as the list of organisations, are not owned by one.) | Even a bug in the application cannot show one hospital another's patients. A record from another hospital simply reads "not found". |
| **Who may do what** | 19 roles and 323 permissions, **deny by default**, plus relationship and facility checks. Every request is checked by the service itself; the optional edge is a second layer, not the only one. | Staff see only what their job needs. Only a patient's own doctor signs their note; only pharmacists dispense; a controlled drug needs a second person. |
| **Signing in** | OpenID Connect with **PKCE (S256)** through your organisation's identity provider. ZYVORA never sees a password. | Your existing single sign-on and its rules (multi-factor, leavers) apply. |
| **Sessions** | Kept on the server, the token stored **hashed**, **30 minutes idle and 8 hours at most**. | A forgotten, unlocked screen logs itself out. |
| **Audit trail** | **Append-only and hash-chained**, written in the same transaction as the change, with a check you can run. Every read and change of a record is recorded (who and when, never the clinical content). | You can answer "who looked at this record?" and prove the log was not edited. It is tamper-evident, not tamper-proof against a database owner. |
| **Break-glass** | Opening a record you would not normally see needs a written reason, is reviewed by an administrator and sits on the audit trail. A privacy watch flags unusual patterns, naming a user and a count, never a patient. | Emergencies are not blocked, and they are not invisible. |
| **The AI** | **Off by default** for each organisation. Drafts need a named human review tied to the clinician's own note revision; identifiers are removed first. Propose-only assistants read only what the signed-in person may read, cite only what a tool returned, and cannot send, order, sign or submit. | The AI helps with paperwork; it never acts on its own. |
| **Hospital-written content** | Note templates, chart forms and care-programme ranges are written by the hospital; the software ships none. A value outside the range its author set is refused as a typing error, never interpreted. | Clinical thresholds are your clinicians' decisions, not ours. |
| **Patient messages** | Only wording a doctor approved, only with the patient's consent for that channel, never in quiet hours or past the daily limit. A "result ready" notice says only that something is waiting. | Reminders cannot leak results or spam patients. |
| **The edge** | An Envoy edge with encryption (TLS) and flood limits, a mutual-TLS listener for connecting systems, and an optional **browser certificate gate** (used for demos) that serves nothing, not even the sign-in page, without a certificate. No revocation list. | A closed front door for demos and connecting systems. |
| **Offline drafts** | Note drafts only, encrypted on the device, for at most 12 hours. | A lost connection does not lose a note; a lost laptop does not leak it for long. |
| **Live screens** | Event streams carry a topic and ids only, never patient data, and a stream does not extend a session. | Screens update without becoming a leak. |
| **Accessibility** | An automated axe-core audit (WCAG 2.1 A and AA rules, both themes) passes. **This is not a conformance claim, and there has been no screen-reader testing.** | A good start, not a guarantee. |

## Added in the next release

These are built and tested but not in version 0.5.2. Details: [Next release](NEXT-RELEASE.md#privacy-governance-and-quality).

| Area | What is in place |
|---|---|
| **Privacy requests and breaches** | A register for patients' access, correction and erasure requests, with due dates fixed from the chosen regime on the day they arrive and an identity check before a request can close; a breach register with regulator and patient deadlines. A record only, not legal advice; it erases and notifies nothing. |
| **Retention and legal holds** | Retention rules, legal holds and two-person disposal certificates. Decisions only: nothing is deleted. A record on hold blocks disposal. |
| **Disclosure accounting** | A ledger of every disclosure outside treatment, payment and operations, with a printable multi-year accounting, and a log of items withheld from the patient portal with the exception relied on. |
| **Two-person rules** | Report approval, fee waivers, disposal certificates and inspector exports each need a second person who is not the requester, checked in the application and again in the database. |
| **Sensitive records** | A medico-legal case register (doctors only, never edited), and safeguarding, capacity and restraint records. |

## What has not been done

- **No certification.** Not certified against HIPAA, GDPR, ISO 27001, SOC 2, IEC 62304, NABH/JCI or similar. A compliance gap list is published in the product documentation.
- **No independent penetration test yet.**
- **The audit trail is tamper-evident, not tamper-proof against a database owner.**
- **No clinical validation of any model.**
- **No load testing.** Browser tests run in Chrome only.
- **Email and SMS** have never been tested through a real provider.
- **Connections to other systems:** FluxVM has been verified live and the Nuvora connection against a real Nuvora process (its offline demo provider); Netra only against stand-ins. Laboratory analyser messages (ASTM, HL7) were tried only with simulated instruments, never a real analyser; the ASTM TCP link is plain TCP and belongs on a closed network or behind an encrypted tunnel. FHIR is read-only and has not been run through the official validator.
- **Outside bodies:** nothing is sent to a regulator, payer, tax authority, scheme or national exchange. Payment links and WhatsApp are labelled simulators; no gateway, WhatsApp or ABDM account is connected.
- **Real data.** ZYVORA has been built and tested with synthetic data only. Do not use real patient data.

## Reporting a vulnerability

Email **[security@zyvor.dev](mailto:security@zyvor.dev)**. Please do not include patient data or credentials, and do not open a public issue for a vulnerability. Details: [SECURITY.md](../SECURITY.md).
