# mcp/src/agents_remember/cli/knowledge_bootstrap.py

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
before. A converted run without a valid `--wave` is refused with exit 2. Since `260928-MIK-L13` the wave also passes
`coordination_root=admitted.authority.coordination_root` (`:526`), so the file writer resolves every
requirement endpoint a lifted decision links and reports it; an unresolved one never refuses the wave
(review F4, ruling 02:05:07, proved by the bootstrap dispatch test in `test_knowledge_writer.py`).

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
- **The database route is locked for unconverted memory once the repository holds converted memory (L37,
  MIK-R09 rule 6; MIK-R37 rule 3).** `_run` routes a converted memory tree to the file writer
  (`run_wave_write`). For an unconverted tree it now asks `cutover_lock_refusal(memory,
  operation="knowledge-bootstrap", ...)` before `bootstrap_knowledge`, prints the refusal and returns
  `EXIT_REFUSED`. In a repository that holds no converted memory the database bootstrap runs as before. `_run`
  is a realization of INV-1XKX9ERN (re-anchored from `run`, which binds twice in this file).

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this entry point implements, and it is a task-tree document rather than a configured domain source.

No external documentation is required for the bootstrap CLI adapter.

### Repo-Internal References

- **The module's own statement of the gap, the two refused shortcuts and the three modes.** [1]
- The two exit meanings: a report was produced, or the invocation was refused. [2]
- **The whole argument surface, including the absent destination argument.** [3]
- **`--commit` documented as the whole write act, with "Without it this reports and writes nothing, which is the dry run."** [4]
- The two read-only modes and their own stated boundaries. [5]
- The authorization reference that is both the admission's authority and the authorship actor. [6]
- **Why contradictory modes are refused rather than resolved by precedence.** [7]
- **The two refusals that keep `--status`, `--discard-staging` and `--commit` from meaning two things at once.** [8]
- The run's own requirements: a readable list and a non-blank authorization. [9]
- **Settings resolution through the umbrella CLI's own discovery, with no second convention.** [10]
- The one admission this invocation runs under, or the refusal that stopped it. [11]
- The typed refusal payload a refusal is rendered from. [12]
- The read-only status payload: what the staging retains and what the location holds now. [13]
- The run payload the report is rendered from. [14]
- The identity record one payload renders, and the cleanup payload. [15]
- **`run`: the invocation refusal answered first, then the one selected mode; the run mode is `_run`.** [16]
- **The run mode: a converted admitted memory root is written by the curator file writer as a wave, with the bootstrap scope as task; an unconverted one takes the cutover lock (L37) and then `bootstrap_knowledge` as before.** [17]
- The `--wave` argument, required only for converted memory. [18]
- **The cleanup's one outcome, and the exit that is refused unless nothing was at stake.** [19]
- **The admission resolver this entry point is the public face of.** [20]
- **The run this subcommand drives, and its refusal value.** [21]
- **The bounded cleanup owner behind `--discard-staging`.** [22]
- The subcommand registration that makes this file reachable. [23]
- The wave passes the admitted authority's coordination root, so requirement endpoints resolve (MIK-R13, review F4). [24]

- A bootstrap run: the file writer for converted memory, the cutover lock, then the database ingest. [25]
- knowledge-bootstrap refuses unconverted memory once the repository holds converted memory. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this file: the repository is named by `--repo` and every
resolution stays inside that repository's own declared scope. The resolved settings' `crossRepo.allow` is
empty, so nothing here names, reads or writes another repository.

No meaningful cross-repo references found.
