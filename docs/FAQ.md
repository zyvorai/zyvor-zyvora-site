# FAQ

**Pilot-ready software, not a certified medical product. Synthetic data only.**

### Is ZYVORA a certified medical product?
No. It is pilot-ready software built and tested with synthetic data. It carries no regulatory certification and no clinical validation, and a gap list says what is missing. See [Intended use and limits](INTENDED-USE.md).

### Does the AI make clinical decisions?
No. It is **off by default**, produces **drafts only**, has **no tools and takes no actions.** A named clinician must review a draft before it counts, and the review is tied to that clinician's own note revision. It runs on a private server you control, the audit trail is hash-chained and written in the same transaction, and questions about the hospital run over a closed catalogue of metrics with no generated SQL. There has been no clinical validation of any model.

### Can we run the AI on our own models or Nuvora?
The AI runs on a private OpenAI-compatible server you control. Nuvora, a self-hosted AI platform with that API, is the preferred back end, but its wire contract has been checked only against Nuvora's offline demo provider, not a live model. No model has been clinically validated and review is mandatory.

### Where does our data live?
On infrastructure you run: PostgreSQL with row-level security per organisation, behind the Rust API. Optional AI runs on a private server you choose, after identifiers are removed.

### How do people sign in?
Through your organisation's own identity provider with OpenID Connect and PKCE. ZYVORA never sees a password. The k3s deployment ships Keycloak (Haven's packaging) with a themed sign-in page. In the **demo**, every user is invented and needs no password.

### Can we connect it to other systems?
There is a read-only FHIR R4 API (Patient, Encounter, Observation, AllergyIntolerance, MedicationRequest, Appointment, `$everything`) and a documented HTTP API. FHIR writes are on the roadmap.

### What does it run on?
Docker Compose on a single host, a Helm chart for Kubernetes, or a k3s deployment with an Envoy Gateway edge. PostgreSQL 14 to 18.

### Can I try it without installing anything on a server?
Yes: the [demo](GETTING-STARTED.md) runs on your own computer with one command, uses invented patients and is removed with one command. Nothing leaves your machine.

### Can I see the source or the docs?
The product source is private. This repository publishes the website, the installer and the release notes. Ask [sales](mailto:sales@zyvor.dev) what we can share with evaluators.

### What does it cost?
Pricing has not been decided; the website shows a layout only and no figure is an offer. To discuss a pilot: [sales@zyvor.dev](mailto:sales@zyvor.dev).

### Has it been used by a customer?
Not yet. There are no customer stories; the website says so.

### Who do we contact?
[sales@zyvor.dev](mailto:sales@zyvor.dev) for pilots and demos · [security@zyvor.dev](mailto:security@zyvor.dev) for security.
