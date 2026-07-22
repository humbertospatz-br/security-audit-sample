# Sample Audit (Audit-1) — How to Run It in Your Own Environment

> **You're in full control.** The audit runs in YOUR environment and the report stays LOCAL, on your
> machine. **We (the consultants) do not receive** your code or the result — the kit sends nothing to
> us and publishes nothing anywhere.
>
> **Transparency (important):** since Claude is an Anthropic service, the files it reads are processed
> on Anthropic's servers, under the data policy of the account you use. This applies to any use of
> Claude. If privacy is critical, use an account/mode **without training retention** (e.g. team/business
> plans). What we guarantee here is that the kit sends nothing to the consultants and does not expose
> the result.

---

## What this is

A **free sample** technical audit. It runs a quick scan looking for the most severe and most common
problems — mainly **security** — and stops as soon as it finds the first ones. The goal is to show you,
in minutes, whether your system is hiding critical risks.

It's not the full audit — it's the proof that the full one is worth doing.

## Requirements

- Claude Code installed (CLI, VS Code or the Claude Code App).
- The code of the project you want to audit, accessible on the machine.

## Preparation (important — it protects your project)

So that **nothing is touched** in your original project or in your Claude configuration, the audit runs
in a separate folder, with **a copy of your project and the kit side by side**:

1. Create a new folder, e.g. `AUDIT-SAMPLE`.
2. Copy **the project folder you want to audit** into it — with its **real name** (e.g. `MySystem`).
   - **Recommended: copy the `.git` along with it.** The history makes it possible to detect secrets
     that were committed (even if deleted later) and access tokens embedded in the remote URL. **It's
     optional** — without `.git` the audit still runs, it just skips that history check and the report
     states it was left out. (The `.git` folder does **not** give access to your GitHub account — it
     only carries the code history.)
   - You can leave out `node_modules/`, `vendor/`, `dist/` (they aren't analyzed anyway).
3. Copy **the `audit1-selfservice` folder** (this kit) into it too — **at the same level as the project**.

It should look like this:
```
AUDIT-SAMPLE/
├── MySystem/              <- copy of your project (real name, with .git)
└── audit1-selfservice/    <- this kit (same level as the project)
```

> **The audit does NOT change anything in the project folder.** It is **read-only** and writes the
> report **OUTSIDE** it — at the root of `AUDIT-SAMPLE`. Your project (original and copy) stays intact.
> You can even put **several projects** side by side and audit them one at a time.

## How to run (2 ways)

Open Claude Code in the `AUDIT-SAMPLE` folder and replace `<project-dir>` with your project's folder
name (e.g. `MySystem`).

**Way A — simplest (recommended):**
```
Read audit1-selfservice/AUDIT1.md and run the audit on the <project-dir> folder.
```
When it finishes, the report will be at `RELATORIO_AMOSTRA_<project>.md` (e.g.
`RELATORIO_AMOSTRA_MySystem.md`), at the root of `AUDIT-SAMPLE` (outside the project folder).

**Way B — command:**
1. Copy `audit1-selfservice/.claude` into `AUDIT-SAMPLE` (it becomes `AUDIT-SAMPLE/.claude/commands/audit1.md`).
2. Run:
   ```
   /audit1 <project-dir>
   ```

### Auditing more than one project

No need to delete anything or create another folder. Just **copy the new project** (e.g. `MySystem2`)
into the same `AUDIT-SAMPLE`, next to the first one, and run again pointing at it:
```
AUDIT-SAMPLE/
├── MySystem/                          (already audited)
├── MySystem2/                         <- new project
├── audit1-selfservice/
├── RELATORIO_AMOSTRA_MySystem.md      (1st report — preserved)
└── RELATORIO_AMOSTRA_MySystem2.md     (2nd report)
```
Since each report is named after its project (`RELATORIO_AMOSTRA_<project>.md`), **one never overwrites
the other**.

## What the audit will do

- Read your code files (read-only — **it changes nothing**).
- Look for critical security and logic problems.
- **Stop as soon as it confirms the first 2 critical issues** (it's a sample, not the full scan).
- Generate a 1-page report, in plain language, in `RELATORIO_AMOSTRA_<project>.md`.

## What the audit will NOT do

- ❌ Send the result to the consultants or publish it anywhere (the report stays with you only).
- ❌ Change, move or delete your code.
- ❌ Run your system (it's static analysis — read-only).
- ❌ Audit everything — it's a sample; the full audit covers much more.

## After running it

The report ends with a contact. If you want the **full audit** (security, logic, database,
infrastructure — with multiple verifiers and a prioritized remediation plan), get in touch.

---

**Kit issued to:** ______________________  (filled in by the consultant)
**Sample valid until:** ____ / ____ / ______
**Contact:** Humberto Spatz — humberto@spatz.com.br
