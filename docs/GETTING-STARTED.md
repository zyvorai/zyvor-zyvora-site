# Getting started

**Pilot-ready software, not a certified medical product. Synthetic data only.**

About five minutes, a hospital full of invented patients, no sign-up, nothing to buy, and **nothing leaves your machine.**

## 1. Install the demo

**Mac or Linux.** Open a terminal, paste this and press Return:

```bash
curl -fsSL https://github.com/zyvorai/zyvor-zyvora-site/releases/latest/download/get.sh | sh -s -- up --demo --seed
```

**Windows.** Open PowerShell, paste this and press Enter. It runs ZYVORA inside WSL 2 (Windows 10 version 2004 or later, or Windows 11):

```powershell
& ([scriptblock]::Create((irm https://github.com/zyvorai/zyvor-zyvora-site/releases/latest/download/get.ps1))) up --demo --seed
```

> **Windows has not been verified on a real Windows PC yet.** The script is tested with simulated Windows calls only. If you try it, please [tell us what you see](#tell-us-how-it-went).

You need nothing installed first. If there is no container engine, the installer offers to set one up (Homebrew then podman on a Mac; podman through apt or dnf on Linux; WSL and podman on Windows) and **asks before it does anything.** Answering no stops with the exact steps to do it yourself. On Windows, expect an administrator prompt and one restart the first time; afterwards run the same command again.

### Read the installer first

The installer is short and only writes under `~/.zyvora`. If you would rather read it before running it:

```bash
curl -fsSL https://github.com/zyvorai/zyvor-zyvora-site/releases/latest/download/get.sh -o get.sh
less get.sh                      # read it
sh get.sh up --demo --seed       # then run it
```

It downloads the install bundle from the same release, **checks its SHA-256 against the release's `SHA256SUMS` and refuses to run on a mismatch**, then unpacks it under `~/.zyvora/app`. More on verifying files yourself: [Releases](RELEASES.md#verify-your-download).

## 2. What you will see

1. **The installer runs.** It downloads two small images, starts ZYVORA, loads invented patients and opens your browser.
2. **The browser warns once.** The demo uses a security certificate it made itself, so every browser shows a warning the first time. It is safe here: the address is your own computer. Chrome and Edge: **Advanced**, then **Proceed**. Safari: **Show Details**, then **visit this website**. Firefox: **Advanced**, then **Accept the Risk**.
3. **Choose a demo user.** Click **Continue with single sign-on**, then pick **Dr. Meera Rao**. There is no password in the demo, because every user is invented. Real installations sign in through the hospital's own identity provider.

## 3. A doctor's test drive

Eight things to try, about ten minutes.

| | What to do | You should see |
|---|---|---|
| 1 | **Sign in as Dr. Meera Rao.** If a welcome tour appears, press Skip. | A dashboard that says "Good morning, Dr. Rao", a waiting room and a red banner. |
| 2 | **See who is waiting.** Look at the Waiting room card, then open Appointments in the top bar. | Today's appointments with a queue number, status, and Check in, No-show and Cancel actions. |
| 3 | **Deal with the critical lab result.** Click Open on the red banner to read the result, then Acknowledge. | The banner goes away for everyone at once. Unacknowledged results escalate to the nurses. |
| 4 | **Open a patient and start an encounter.** Patients, then a name, then Start encounter. Write a note, add a vital sign, prescribe something. | The allergy card comes first. Notes keep every revision, and signing is for doctors only. |
| 5 | **Send an urgent message to the nurse.** On a patient choose Message the care team, tick Urgent, send. Then sign out and sign in as Nurse Kavya Iyer. | The nurse sees an alert that stays until it is opened. |
| 6 | **Look at the emergency board.** Open Emergency in the top bar. | Arrivals by urgency, with triage and bed placement. |
| 7 | **Search from the keyboard.** Press Cmd+K (Mac) or Ctrl+K, type `bed`, press Enter. | You jump to Beds and admissions. Patient names are searchable here too. |
| 8 | **Switch to dark mode.** Click the moon icon in the top bar. | The whole app changes appearance and remembers it. |

The assistant that drafts notes is a **stand-in in the demo**, and every patient, result and number is invented. Nothing you type leaves your computer.

## 4. Afterwards

**Check that everything installed correctly:**

```bash
~/.zyvora/zyvora test
```

It signs in, creates a record and reads it back. **`all checks passed`** means everything works. `~/.zyvora/zyvora status` should show all five lines as `Up`.

**Remove it:**

```bash
~/.zyvora/zyvora uninstall
```

The containers and their data are deleted; only a small settings folder, `~/.zyvora`, stays until you delete it (`rm -rf ~/.zyvora`; on Windows, run that inside Ubuntu).

## Tell us how it went

What worked, what confused you, what you wanted to see. If something failed, include the output of `~/.zyvora/zyvora test` and your computer type. Email [sales@zyvor.dev](mailto:sales@zyvor.dev?subject=ZYVORA%20demo%20feedback), or open a **Feedback** issue here (never include patient data or credentials).

Stuck? [Troubleshooting](TROUBLESHOOTING.md) · What ZYVORA is not: [Intended use and limits](INTENDED-USE.md)
