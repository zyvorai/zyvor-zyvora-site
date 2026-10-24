# Security overview

**Pilot-ready software, not a certified medical product. Synthetic data only.**

The controls you can point at in a pilot, and, just as important, what has **not** been done. To report a vulnerability, read [SECURITY.md](../SECURITY.md).

## Controls

| Area | What is in place |
|---|---|
| **Tenant isolation** | Row-level security is **forced** on every tenant-owned table, with an application database role that cannot bypass it. (Global tables, such as the tenant list, are not tenant-owned.) |
| **Roles** | Nine roles, **deny by default**, plus relationship and facility checks. Every request is authenticated and authorised by the API itself; the optional Envoy edge is a second layer, not the only one. |
| **Sign-in** | OpenID Connect authorization code flow with **PKCE (S256)** through your organisation's identity provider. ZYVORA never sees a password. |
| **Sessions** | Server-side, token stored **hashed**, **30 minutes idle and 8 hours at most**. |
| **Audit** | **Append-only and hash-chained**, written in the same transaction as the change, with a verify endpoint. Every read and change of a record is recorded (metadata only). |
| **Break-glass** | Access to a record you should not normally see needs a stated reason, is reviewed by an administrator and is on the audit trail. |
| **AI** | **Off by default** per organisation. Drafts only: no tools, no actions, identifiers removed first, and a named human review bound to the clinician's own note revision. |
| **Offline drafts** | Note drafts only, encrypted on the device, for at most 12 hours. |
| **Live screens** | Event streams carry topic and ids only, never patient data, and a stream does not extend a session. |
| **Accessibility** | An automated axe-core audit (WCAG 2.1 A/AA rules, both themes) passes. **This is not a conformance claim, and there has been no screen-reader testing.** |

## What has not been done

- **No certification.** Not certified against HIPAA, GDPR, ISO 27001, SOC 2, IEC 62304, NABH/JCI or similar. A compliance gap list is published in the product documentation.
- **No independent penetration test yet.**
- **The audit trail is tamper-evident, not tamper-proof against a database owner.**
- **No clinical validation of any model.**
- **No load testing.** Browser tests run in Chrome only.
- **Email and SMS** have never been tested through a real provider.
- **Integrations:** only FluxVM has been verified live; Netra and Nuvora are tested against stand-ins. FHIR is read-only.
- **Real data.** ZYVORA has been built and tested with synthetic data only. Do not use real patient data.

## Reporting a vulnerability

Email **[security@zyvor.dev](mailto:security@zyvor.dev)**. Please do not include patient data or credentials, and do not open a public issue for a vulnerability. Details: [SECURITY.md](../SECURITY.md).
