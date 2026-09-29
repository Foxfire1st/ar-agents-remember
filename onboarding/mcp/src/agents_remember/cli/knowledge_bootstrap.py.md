# mcp/src/agents_remember/cli/knowledge_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T09:20+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64` |
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**The taskless entry the knowledge write plane did not have (ICR-R29@v1).** The ordinary
`knowledge-ingest` subcommand requires `--contract` — a leaf enclosure contract — because that is the
admission its operation was bound to, and a repository whose first knowledge is being written has no
leaf and no enclosure. Fabricating one is refused by the bootstrap handover and a second write path is
refused by the preservation boundaries, so this subcommand resolves the second **real** admission
instead: the repository entry the MCP settings document declares, the memory layer the ordinary read
route resolves, and the exact code and memory revisions the real checkouts stand at. It then drives the
same operation the leaf path drives.

Three modes, and the surface is deliberately small:

```
agents-remember knowledge-bootstrap --repo <repo_id> --list <hand-off list>
    --authorization-ref <ref> [--commit] [--config <MCP settings>] [--json]
agents-remember knowledge-bootstrap --repo <repo_id> --status [--config <MCP settings>] [--json]
agents-remember knowledge-bootstrap --repo <repo_id> --discard-staging [--json]
```

**Planning is the default, and planning is also the dry run.** Without `--commit` the list is read, the
candidate is planned, the destination is read, and **nothing is written**: no batch, no publication and
no retained progress record. `--commit` is the developer's commit word and is the whole of the write
act. **Exit zero is not a publication claim** — the report carries the destination read before the run,
the batch's own state, the publication owner's result, an independent read-back of the declared location
through the read route's own owner, a contents read of what the dataset holds, and the named remaining
work, and a run whose entries all committed can still have published nothing.

## Code Commentary

### Logic

**Every contradiction in the argument list is answered before anything is read** (`:143-180`).
`_invocation_refusal` runs the mode check and then, only for a run, the list check. Two contradictory
modes are **refused rather than resolved by precedence**: `_mode_refusal` (`:158-168`) refuses
`--status` with `--discard-staging` and refuses `--commit` with either read-only mode, with the sentence
stating why — "silently picking one is how a dry run becomes a real one".
`_list_refusal` (`:171-180`) requires a `--list` that is really a file and a non-blank
`--authorization-ref`, because an admitted write needs an authorization.

**Settings resolution is the umbrella CLI's own, with no second convention** (`:183-196`): `--config`
when given, otherwise `discover_config(Path.cwd())`, and a discovery or read failure is returned as a
sentence that names the route (`pass --config with the document the harness registers`) rather than as a
traceback.

**Admission happens once, then the mode dispatches** (`:456-491`). `run` answers the invocation refusal
with `EXIT_REFUSED`, then `_dispatch` resolves the admitted context and returns `EXIT_REFUSED` for a
refusal — printing the typed refusal payload for a `BootstrapRefusal` and the bare sentence for a
settings failure. Only an admitted context reaches a mode: `--discard-staging` goes to `_cleanup`, then
`--status`, then the run, which calls `bootstrap_knowledge` and prints either the run refusal or the run
payload. `EXIT_REPORTED` is `0` and `EXIT_REFUSED` is `2` (`:91-92`).

**The contents block is named for the destination, not for this run's publication** (`:361-375`). It
reports what a read of the declared location found — its state, its revision count, its page count — and
carries `publishedByThisRun` beside it, false whenever this run's publication produced no identity,
with a `detail` sentence that says in that case that nothing in the block is this run's work. The
earlier spelling was `publishedContents`, which in a refused-publication run let a reader take the
*previous* dataset's contents for this run's publication; the state machine was already honest
everywhere else in the payload, and this is the one key whose name had to stop implying authorship.

**Cleanup reports the owner's one outcome and exits refused unless nothing was at stake** (`:494-501`):
`discard_bootstrap_staging` is called with the admitted staging root and context, the payload is stamped
`state: "cleanup"`, and the exit is `EXIT_REPORTED` only for `discarded` or `absent`.

**The mode arguments are the whole write surface.** `--repo` is the repository id the settings document
declares (`:96`); there is **no** `publish_to`, `destination` or `expected_destination` argument
anywhere, because the destination is derived by the read route's own owner. `--commit` (`:110-115`)
documents itself as "Without it this reports and writes nothing, which is the dry run." `--status`
(`:116-121`) and `--discard-staging` (`:122-128`) each state the mode's own boundary, and
`--authorization-ref` (`:104-109`) is the authorization the bootstrap is admitted under **and** the
actor the authorship envelope names.

### Conventions

The module composes the admission resolver, the run, the staging cleanup owner and the umbrella CLI's
settings discovery. It imports the report renderer for the ingest report's own vocabulary; it never opens
a dataset and never mints an identity.

### Invariants And Boundaries

- The destination is never an argument: the read route's own owner computes it.
- Without `--commit` nothing is written — no batch, no publication, no progress record.
- Contradictory modes are refused, never resolved by precedence.
- Exit `0` means a report was produced, **not** that anything was published.
- `--discard-staging` exits refused unless the cleanup owner discarded or found nothing.
- `--config` reuses the umbrella CLI's trusted discovery; no environment variable is invented.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this entry point implements, and it is a task-tree document rather than a configured domain source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the bootstrap CLI adapter. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the gap, the two refused shortcuts and the three modes.** | "the knowledge write plane did not have"; "EXIT ZERO IS NOT A PUBLICATION CLAIM" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:1-90 |
| The two exit meanings: a report was produced, or the invocation was refused. | `EXIT_REPORTED`; `EXIT_REFUSED` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:93-94 |
| **The whole argument surface, including the absent destination argument.** | `add_arguments`; "--repo" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:97-142 |
| **`--commit` documented as the whole write act, with "Without it this reports and writes nothing, which is the dry run."** | "--commit"; "which is the dry run" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:110-117 |
| The two read-only modes and their own stated boundaries. | "--status"; "--discard-staging" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:118-130 |
| The authorization reference that is both the admission's authority and the authorship actor. | "--authorization-ref" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:106-110 |
| **Why contradictory modes are refused rather than resolved by precedence.** | `_invocation_refusal`; "silently picking one is how a dry run becomes a real one" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:145-157 |
| **The two refusals that keep `--status`, `--discard-staging` and `--commit` from meaning two things at once.** | `_mode_refusal`; "one run cannot mean both" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:160-170 |
| The run's own requirements: a readable list and a non-blank authorization. | `_list_refusal` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:173-182 |
| **Settings resolution through the umbrella CLI's own discovery, with no second convention.** | `_settings`; `load_config`; `discover_config` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:185-198 |
| The one admission this invocation runs under, or the refusal that stopped it. | `_admitted` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:201-207 |
| The typed refusal payload a refusal is rendered from. | `_refusal_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:210-216 |
| The read-only status payload: what the staging retains and what the location holds now. | `_status_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:219-275 |
| The run payload the report is rendered from. | `_run_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:278-384 |
| The identity record one payload renders, and the cleanup payload. | `_identity_record`; `_cleanup_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:387-394; mcp/src/agents_remember/cli/knowledge_bootstrap.py:397-403 |
| **`run`: the invocation refusal answered first, then the one selected mode.** | `run`; `_dispatch` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:474-481; mcp/src/agents_remember/cli/knowledge_bootstrap.py:484-509 |
| **The cleanup's one outcome, and the exit that is refused unless nothing was at stake.** | `_cleanup` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:512-519 |
| **The admission resolver this entry point is the public face of.** | `admit_bootstrap_context`; `BootstrapRefusal`; `AdmittedKnowledgeBootstrap` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:118-129; mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:132-151; mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:175-214 |
| **The run this subcommand drives, and its refusal value.** | `bootstrap_knowledge`; `BootstrapRunRefusal` | mcp/src/agents_remember/application/knowledge_bootstrap.py:98-104; mcp/src/agents_remember/application/knowledge_bootstrap.py:157-244 |
| **The bounded cleanup owner behind `--discard-staging`.** | `discard_bootstrap_staging`; `StagingCleanup` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:214-221; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:418-479 |
| The subcommand registration that makes this file reachable. | `knowledge_bootstrap`; "knowledge-bootstrap" | mcp/src/agents_remember/cli/__main__.py:54-62 |

## Cross-Repo References

No cross-repository behavior is implemented in this file: the repository is named by `--repo` and every
resolution stays inside that repository's own declared scope. The resolved settings' `crossRepo.allow` is
empty, so nothing here names, reads or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the `knowledge-bootstrap` registration row re-pointed to `cli/__main__.py:54-62` after MIK-R21 registered `knowledge-format` above it; the other re-pointed rows are the anchor-range projection's. Claim meaning unchanged; no stamp advanced.
- 2026-09-24T10:50+02:00 — 260921-ICR-L29 curator, **micro-round-2 bytes (documentation only)** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`): **re-read against the
  corrected docstrings; the card and the source agree** — the contents block is named `destinationContents` with `publishedByThisRun` in the source, matching this card. All ranges were re-derived for the line shift. **No verification stamp was advanced.**
- 2026-09-24T10:20+02:00 — 260921-ICR-L29 curator, **fix-round bytes** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`; gate `verify-l29-round2.md`,
  first line `pass-with-findings`): **the report's contents block was renamed because its old name was
  false in one state.** `publishedContents` became **`destinationContents`** with a new
  **`publishedByThisRun`** flag, so a refused-publication run can no longer be read as though the
  contents it shows were this run's publication. The block is a read of the declared destination whether
  or not this run published into it. The module is 517 lines on this candidate (501 when this card was
  first written), and two new reference rows cite the block and the flag. **No verification stamp was
  advanced** — the candidate is uncommitted and the governed closeout owns the real code and memory
  commits.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): created this one-to-one card for the module
  `ICR-R29@v1` introduced as **the taskless bootstrap CLI adapter**. The stamp basis is the leaf's base
  commit, because the module is untracked there. Two sentences carry the correctness: the destination is
  **derived, never accepted** — there is no argument that can aim it elsewhere — and **exit zero is not a
  publication claim**, so the report carries the read-back and the named remaining work rather than
  leaving the exit code to be read as success. A third is that planning is the default and writes
  nothing at all, while a contradictory mode pair is refused rather than resolved by precedence. No
  verification stamp beyond the leaf's base is advanced: the candidate is uncommitted and the governed
  closeout owns the real commit.
