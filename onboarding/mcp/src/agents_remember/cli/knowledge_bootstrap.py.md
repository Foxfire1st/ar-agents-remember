# mcp/src/agents_remember/cli/knowledge_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175` |
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
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
payload. `EXIT_REPORTED` is `0` and `EXIT_REFUSED` is `2` (`:91-92`). Since `260928-MIK-L12` the run
mode is its own function, `_run`: when the admitted memory root is **converted** (it holds
`knowledge/layout.json`), it hands the run to the curator file writer through
`cli/knowledge_write_route.run_wave_write`, writing as the wave `--wave` names (its history file is
`knowledge/history/<wave>.json`, MIK-R07 rule 8) with the bootstrap's own scope
(`knowledge-bootstrap:<repo>`) as the records' task; otherwise it calls `bootstrap_knowledge` exactly as
before. A converted run without a valid `--wave` is refused with exit 2.

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
actor the authorship envelope names. `--wave` (added by `260928-MIK-L12`) names the wave a bootstrap of
converted memory writes as; it is required only when the memory is converted and means nothing on the
database route.

### Conventions

The module composes the admission resolver, the run, the staging cleanup owner and the umbrella CLI's
settings discovery. It imports the report renderer for the ingest report's own vocabulary; it never opens
a dataset and never mints an identity.

### Invariants And Boundaries

- The destination is never an argument: the read route's own owner computes it.
- Without `--commit` nothing is written — no batch, no publication, no progress record.
- Contradictory modes are refused, never resolved by precedence.
- Exit `0` means a report was produced, **not** that anything was published.
- Converted memory is written as files and unconverted memory keeps the database bootstrap: until the
  cutover (MIK-R37) no memory root is converted, so the production bootstrap is unchanged (MIK-R12 rule 7;
  the database modules stay until L26).
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
| The two exit meanings: a report was produced, or the invocation was refused. | `EXIT_REPORTED`; `EXIT_REFUSED` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:100-101 |
| **The whole argument surface, including the absent destination argument.** | `add_arguments`; "--repo" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:104-155 |
| **`--commit` documented as the whole write act, with "Without it this reports and writes nothing, which is the dry run."** | "--commit"; "which is the dry run" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:117-124 |
| The two read-only modes and their own stated boundaries. | "--status"; "--discard-staging" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:125-137 |
| The authorization reference that is both the admission's authority and the authorship actor. | "--authorization-ref" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:113-117 |
| **Why contradictory modes are refused rather than resolved by precedence.** | `_invocation_refusal`; "silently picking one is how a dry run becomes a real one" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:158-170 |
| **The two refusals that keep `--status`, `--discard-staging` and `--commit` from meaning two things at once.** | `_mode_refusal`; "one run cannot mean both" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:173-183 |
| The run's own requirements: a readable list and a non-blank authorization. | `_list_refusal` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:186-195 |
| **Settings resolution through the umbrella CLI's own discovery, with no second convention.** | `_settings`; `load_config`; `discover_config` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:198-211 |
| The one admission this invocation runs under, or the refusal that stopped it. | `_admitted` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:214-220 |
| The typed refusal payload a refusal is rendered from. | `_refusal_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:223-229 |
| The read-only status payload: what the staging retains and what the location holds now. | `_status_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:232-288 |
| The run payload the report is rendered from. | `_run_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:291-397 |
| The identity record one payload renders, and the cleanup payload. | `_identity_record`; `_cleanup_payload` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:400-407; mcp/src/agents_remember/cli/knowledge_bootstrap.py:410-416 |
| **`run`: the invocation refusal answered first, then the one selected mode; the run mode is `_run`.** | `run`; `_dispatch` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:487-494; mcp/src/agents_remember/cli/knowledge_bootstrap.py:497-512 |
| **The run mode: a converted admitted memory root is written by the curator file writer as a wave, with the bootstrap scope as task; anything else takes `bootstrap_knowledge` as before.** | `_run`; `run_wave_write` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:515-537; mcp/src/agents_remember/cli/knowledge_write_route.py:168-202 |
| The `--wave` argument, required only for converted memory. | "--wave" | mcp/src/agents_remember/cli/knowledge_bootstrap.py:144-149 |
| **The cleanup's one outcome, and the exit that is refused unless nothing was at stake.** | `_cleanup` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:540-547 |
| **The admission resolver this entry point is the public face of.** | `admit_bootstrap_context`; `BootstrapRefusal`; `AdmittedKnowledgeBootstrap` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:118-129; mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:132-151; mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:175-214 |
| **The run this subcommand drives, and its refusal value.** | `bootstrap_knowledge`; `BootstrapRunRefusal` | mcp/src/agents_remember/application/knowledge_bootstrap.py:98-104; mcp/src/agents_remember/application/knowledge_bootstrap.py:157-244 |
| **The bounded cleanup owner behind `--discard-staging`.** | `discard_bootstrap_staging`; `StagingCleanup` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:214-221; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:418-479 |
| The subcommand registration that makes this file reachable. | `knowledge_bootstrap`; "knowledge-bootstrap" | mcp/src/agents_remember/cli/__main__.py:62-70 |

## Cross-Repo References

No cross-repository behavior is implemented in this file: the repository is named by `--repo` and every
resolution stays inside that repository's own declared scope. The resolved settings' `crossRepo.allow` is
empty, so nothing here names, reads or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `__main__.py`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `EXIT_REPORTED`; `EXIT_REFUSED` repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:100-100; mcp/src/agents_remember/cli/knowledge_bootstrap.py:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `_invocation_refusal`; "silently picking one is how a dry run becomes a real one" repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:158-170; mcp/src/agents_remember/cli/knowledge_bootstrap.py:164-164. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `_mode_refusal`; "one run cannot mean both" repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:173-183; mcp/src/agents_remember/cli/knowledge_bootstrap.py:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `_list_refusal` repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:186-195. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `_admitted` repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:214-220. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `_refusal_payload` repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:223-229. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:08:46+00:00: Generated citation repair: `_cleanup` repointed to mcp/src/agents_remember/cli/knowledge_bootstrap.py:540-547. No content impact: mechanical anchor-range projection bound to citation source snapshot c2ff7be37748258a742372475ca8866db78df73e27e0de3f4e49550bdfa6662e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): **body update — the converted-memory dispatch and `--wave`.** The Logic now says the run mode is `_run`, which sends a converted admitted memory root to `cli/knowledge_write_route.run_wave_write` as the wave `--wave` names (task = the bootstrap scope) and otherwise calls `bootstrap_knowledge` unchanged; the argument paragraph names `--wave`; an invariant states that unconverted memory keeps the database bootstrap until the cutover. The `run`/`_dispatch` row was reworded and re-derived to the constructs' own extents (`:487-494`, `:497-512`; its old ranges still passed only because the word `run` also sits in `_summary`), and two rows were added (`_run` at `:515-537`, `--wave` at `:144-149`). The other rows moved by the docstring, import and argument insertions and were re-pointed by the fixer or by exact base-to-working line mapping; their wording is retained. The prose line references in the Logic paragraphs (`:456-491` and the like) predate this leaf and are left as history. No verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 registers `knowledge-census` in `cli/__main__.py` (one import line and a longer docstring sentence), which moves the later registrations down by two lines; this card's registration row was re-pointed to the new extent, its claim unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`__main__.py`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
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
