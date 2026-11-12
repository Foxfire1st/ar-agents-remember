# mcp/src/agents_remember/application/knowledge_routes_report.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The family-route report: each family's routes beside the mechanical suggestion (MIK-R04, MIK-R73 rule 4).**
Routes are authored on a family record; the suggestion is derived from where that family's realizations
actually live in the code checkout. One function produces the rows for both surfaces — the curator's
`knowledge-routes` command and `knowledge_integrity_check`'s `routes` answer — so neither can report a
different route set. The module reads only: no route is written, suggested into place or repaired here.

## Code Commentary

### Logic

- `working_tree_files(code_root)` lists the checkout's tracked and untracked, not ignored files
  (`git ls-files -z --cached --others --exclude-standard`) and raises `KnowledgeTreeReadError` naming the
  root and Git's message when the listing fails.
- `family_route_documents(parsed, wanted, code_files)` walks the parsed tree's records, keeps `FamilyRecord`
  instances (filtered by `wanted` when it is non-empty), computes `family_route_state(family, locations)`
  over `realization_locations(parsed.sidecars)`, and emits one row per family: `family`, `path`, `status`,
  the authored `routes`, and a `state` document.
- The `state` document carries `unrealizedFamily`, `routeUnassigned`, `routeless`, `uncovered` (the first
  `UNCOVERED_SHOWN` = 10 paths), `uncoveredTotal` (every one, so a bounded answer still states the size) and
  `emptied`.
- With `code_files is None` — a code root that is not a Git checkout — the row still reports the family's own
  routes and their state, sets `suggestion` to `None`, states `suggestionState: unavailable` with its detail,
  and `differs` false. A suggestion is never guessed from an empty file list.
- `routes_report(memory_root, code_root, families=None, code_commit=None)` parses the memory tree from its
  directory and reads the code side either from a commit's tree (`code_tree_from_git`) or from the working
  tree (`working_tree_files`), then returns the rows.

### Conventions

- `differs` compares route **sets** (`set(family.routes) != set(suggestion.routes)`), so ordering and
  duplication never read as a difference.
- The mechanical suggestion is labelled as such by its producer (`suggest_family_routes`); this module only
  places the document in the row.

### Invariants And Boundaries

- **Read only.** No route is written, and no family record is touched.
- **Both surfaces share one function**, which is the point of the module: the command and the integrity check
  cannot disagree.
- **A non-checkout states its own limit** rather than reporting an empty suggestion as a computed one.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R73@v1` rule 4 and `MIK-R04`'s route rules for families, of task
`260928_maintained-invariant-knowledge`; the packet lives outside the code and memory repositories and is
named here, not cited as a row.

### Repo-Internal References

No numbered references are recorded for this new module. The functions named in the commentary are its own
public surface; the route rules it reports are the validator's (`family_routes.py`) and are evidenced on the
records that own them.

### Cross-Repo References

None: the module reads one memory tree and one code checkout, both named by its caller.
