# l-01-agent-lifecycles/criteria/doctrine.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/doctrine.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|

## Purpose

Packaged runtime copy of the doctrine-review criteria catalog. The canonical
`skills/l-01-agent-lifecycles/criteria/doctrine.md` owns the criteria; the skill sync process
publishes this exact artifact for installed runtimes.

## Code Commentary

### Logic

The catalog binds when agent-obeyed doctrine changes. D-1 requires implementation anchors for
enforcement claims, D-2 checks the whole instruction surface for contradictions, and D-3 walks the
obeying-agent state machine for deadlocks. The current D-3 evidence resolves master handover with a
wait-free raise and structural master-document decision, without packet-carried transport identity.

### Conventions

Reviewers run the standing list whenever this catalog binds and use the promotion ratchet for new
criteria. Edit the canonical catalog, then synchronize; this packaged copy has no independent
criteria history.

### Invariants And Boundaries

- Every enforcement claim remains evidence-backed.
- Structural document/role authority must not be weakened into exact-id instructions.
- This file must remain byte-identical to its canonical source after synchronization.

### Todos

None recorded.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Criteria Catalog — Doctrine Review` | skills/l-01-agent-lifecycles/criteria/doctrine.md:1-58 |
| The reviewer role that binds this catalog per review type. | "Criteria Catalogs (the review test bench — bound here)" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md:69-69 |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L2 Topology Doctrine Criteria

D-4 now sweeps every role, brief, handover, and verdict for the selected execution nature: an
organizational master has no integration branch, an atomic master does, and neither main, super,
nor an atomic integration ref is a feature/fix workbench. D-5 independently checks that mechanisms
surface facts while named roles own and record dependency, priority, classification, blocker, and
queue judgment.

## 260815-DAG-L15 Review-Doctrine

D-6 now stands: bounded `L<leaf>-R<n>` / `L<leaf>-S<n>` requirement identifiers in source comments
are allowed — the repo carries them at scale (83 comment lines across 22 modules at L15) — and are
the preferred way to tie a comment to its contract, while task/chat/review/decision-item/report
provenance and paths stay out. The criterion records the Source Comment Scope reconciliation
(260815-DAG-L12 F3, 260815-DAG-L16 F4).

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: D-6 added — bounded `L<leaf>-R<n>` / `L<leaf>-S<n>`
  requirement identifiers in source comments are allowed; provenance prose and paths stay out.
  Verified at code commit de3a0fd9.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: added the topology/authority and detection-versus-
  judgment regression criteria. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `doctrine.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 4 initial citation findings (2 anchor, 0 prose, 2 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/doctrine.md` seed catalog (leaf 260703-L12): D-1 doctrine-vs-code anchoring (AR-5), D-2 cross-file contradiction sweep (L10 chat-build survivors), D-3 stuck-state walk (L8 round-2 seam deadlock), with the exploratory mandate and the promotion ratchet. Verification metadata pinned until closeout stamps the L12 commit.
