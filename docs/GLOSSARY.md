# Glossary

**Pilot-ready software, not a certified medical product. Synthetic data only.**

> **In one minute.** Plain-English meanings for the special words used across these pages, in alphabetical order. If a word is missing, [tell us](mailto:sales@zyvor.dev) and we will add it.

## A to C

| Word | What it means |
|---|---|
| **ABDM** | India's national digital health mission. ZYVORA holds the local side only (a patient's address, consents and a log); it has no connection to the national gateway. |
| **Advisory** | A hint for a person, never a decision. Early warning scores and risk bands are advisory. |
| **Append-only** | A record that can only be added to. Corrections are new entries beside the old one; nothing is overwritten or deleted. The database enforces this, not just the application. |
| **API** | A set of requests one computer program can make to another. ZYVORA documents 1,509 of them. |
| **ASTM, HL7** | Common message formats that laboratory machines and hospital systems use to send results and admissions. |
| **Audit trail** | A permanent log of who read or changed a record and when (never the clinical content itself). |
| **Break-glass** | Opening a record you would not normally see, in an emergency or for a good reason. You must type the reason, it is logged, and an administrator reviews it. |
| **Certified** | Formally checked and approved by an outside body against a standard. ZYVORA is **not** certified against any. |
| **Clinical validation** | Proof, from testing on real clinical cases, that a tool is accurate and safe. No model in ZYVORA has it. |
| **Container** | A sealed box that holds a program and everything it needs, so it runs the same everywhere. The demo uses two. |
| **CSV** | A plain table in a text file that opens in a spreadsheet. |

## D to M

| Word | What it means |
|---|---|
| **Deny by default** | Nothing is allowed unless a rule says so. If no role grants an action, it is refused. |
| **DRG (diagnosis-related group)** | A way of grouping hospital stays that use similar resources, used for payment and comparison. |
| **FHIR** | A modern standard for sharing health records between systems. ZYVORA offers it read-only. |
| **Hash-chained** | Each log entry carries a fingerprint of the one before it, so any later change breaks the chain and shows. |
| **Idempotent** | Safe to repeat: sending the same payment twice only counts once. |
| **Identity provider** | The system that signs your staff in (for example your organisation's single sign-on). ZYVORA never sees the password. |
| **ISBAR** | A structured way to hand over a patient: Identify, Situation, Background, Assessment, Recommendation. |
| **MAR** | Medication administration record: what was given to a ward patient, when and by whom. |
| **Minor units** | Money counted in its smallest coin (paise, cents) as whole numbers, so there are never rounding errors. |
| **Module** | One department or function inside ZYVORA, such as Laboratory or Billing. |

## N to Z

| Word | What it means |
|---|---|
| **NEWS2** | A standard early warning score for adult patients, worked out from vital signs. |
| **Penetration test** | A paid attempt by outside experts to break into a system. None has been done on ZYVORA yet. |
| **PKCE, OpenID Connect** | The modern, safe way to sign in through an identity provider without sharing a password with the application. |
| **Propose-only** | An assistant that can only leave a suggestion; a person accepts or dismisses it. |
| **Restricted record** | A record marked so that only people with a reason can open it (through break-glass). |
| **Role** | A job, such as doctor or pharmacist, with a fixed list of what it may do. ZYVORA has 19. |
| **Row-level security** | The database itself hides rows that belong to another hospital, even if the application had a bug. |
| **Simulator** | A pretend version of an outside system, used so the feature can be tried without sending anything anywhere. |
| **SHA-256** | A fingerprint of a file. If one letter of the file changes, the fingerprint changes. |
| **Stand-in** | A fake used in place of the real thing during testing, for example a fake AI model. |
| **Synthetic data** | Invented patients and numbers that look real but belong to no one. All ZYVORA testing uses it. |
| **Tamper-evident** | Changes cannot be hidden: they are detectable. Different from tamper-proof, which ZYVORA does not claim. |
| **Tenant** | One organisation's separate space inside the system. |
| **UDI** | A device's unique identifier, used to trace an implant or instrument to the patients who received it. |
| **WSL 2** | Windows' built-in way to run Linux programs, used by the demo installer on Windows. |

Back to the [documentation index](README.md).
