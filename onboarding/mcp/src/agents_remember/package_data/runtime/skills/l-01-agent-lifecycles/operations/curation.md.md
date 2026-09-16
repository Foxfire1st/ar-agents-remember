# operations/curation.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/curation.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| lastVerifiedCommitDate | 2026-09-16T22:28:15+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The leaf coherence pass — reconciling intended, current, and implemented meaning and writing the affected onboarding.

Every operation block shares one five-part shape — who carries it, required inputs, normal workflow, authority gates, failure handling, and handoff/exit — which is what makes a long procedure separately loadable instead of padding every role file.

## Code Commentary

### Logic

`## Who carries it, and their job` separates two disjoint jobs in one table: the curator reconciles and
writes memory, the manager compiles the brief and owns the transaction. `## Required inputs` states the
three fed inputs (the landed change set with counters and paths pulled from the leaf contract's recorded
range; the leaf task doc with its approved requirement-corpus ruling and version-addressed packets; and
`notes/` with the builder turn report plus the candidate-bound route-review verdict only when review was
requested) and records the rule that none of them is inferred from transcript memory. The block also
carries the curator's own prohibitions — never runs the closeout preview, never repairs transaction
conflicts, never decides whether a leaf lands — and the routing rule that rejects overview-dumping and
task-log-dumping alike.

### Conventions

The strict 1-to-1 source mapping, governing-overview links, and metadata rules live in the `c-05-create-or-update-onboarding-files` skill, not here.

### Invariants And Boundaries

- An operation block holds procedure only; a rule that applies across roles belongs in `core/`.
- A role file names the operation it selects; it does not restate the procedure.
- The operation vocabulary is closed at eight names, so an unknown operation is an explicit error rather than a silent fallback.
- Authority gates and failure handling stay inside this block, not in the role that triggers it.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/curation.md:1-1 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T22:19+02:00 — **No content impact:** 260915-CAPS-L16 curator. The canonical source gained
  one pronoun — the curator's exit says terminal/finalizer evidence attests only that **this** turn
  ended — and this card's Logic describes the curator/manager job split and the three fed inputs, not
  the completion-truth wording, so nothing in the body asserts the sentence that moved. Reviewed
  against the change set and deliberately left as written rather than reworded to match a one-word
  diff. **Repaired in the same pass (D16):** this card's `governingOverview` field and link pointed five
  levels up, at `onboarding/mcp/src/agents_remember/overview.md`, which does not exist — the card's own
  link text says "MCP package overview", which from `operations/` is **seven** levels up. Both now
  resolve to `onboarding/mcp/overview.md`. Verification metadata moves to this leaf's synced base
  `8997e184`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/operations/curation.md` — a file added by the role-instruction corpus consolidation. The canonical source is an operation-scoped procedure block extracted from interleaved role prose (curation).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
