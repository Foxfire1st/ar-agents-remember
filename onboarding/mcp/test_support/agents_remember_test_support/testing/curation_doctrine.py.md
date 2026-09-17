# mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T12:30+02:00 |
| lastVerifiedCommitHash | `304de8e272fd9128d035b805f317da5f3090865c` |
| lastVerifiedCommitDate | 2026-09-17T12:34:11+02:00|
| governingOverview      | `overview.md` |

## Governing Overview

[Python Test Evidence Infrastructure Overview](overview.md)

## Purpose

The **reading half** of the shipped-corpus guard for `CAPS-R18@v1` — the rule that curation is complete
on every leaf. A shipped instruction sentence is product: a spawned curator reads its brief literally, so
a sentence presenting the memory-quality operation as a developer-request-only diagnostic, or as
something a named scoped check may stand in for, tells that seat that complete curation is somebody
else's decision. No per-file test can catch that defect, because each individual sentence is plausible
alone; what has to hold is the agreement of the **whole shipped corpus** with the rule. This module owns
the data and the readers for that census, and deliberately nothing else: it is free of pytest and of any
repository constant so a case can point it at a staged or synthetic tree.

## Code Commentary

### Logic

`RETIRED_CURATION_STATEMENTS` is the registry of the ten retired sentences. Each row carries the exact
`statement`, the `sources` tuple naming the files that actually shipped it, a short `probe`, and a
`reason` naming which packet fragment it was. `sources` is load-bearing in both directions: it is the set
in which the sentence is a defect **when it returns**, and it keeps a retained doctrine — an explicit
developer request still governs full code quality and full tests — from reading as a regression.

`CURATION_COMPLETENESS_STATEMENTS` is the other half: the exact form each canonical surface must state
the rule in, keyed by its shipped path, with `COMPLETE_CURATION_RULE` (`"Curation is always complete"`)
as the sentence every one of those surfaces carries.

Matching is on a **normalized reading** — `normalize_statement` strips markdown emphasis and collapses
line wrapping — and against the **whole** retired sentence, so a statement re-inserted with different
emphasis or at a different column is still the same statement, while doctrine that legitimately survives
cannot read as a regression. The `probe` is what a report and a failure message name the row by; it is
deliberately **not** the matcher.

The readers split by question: `retired_statement_findings(reading, surface_relative_path)` answers "is
this one retired sentence present on this one surface", `doctrine_files` and `retired_curation_findings`
sweep a tree, and `missing_completeness_statements` answers "does this surface still state the rule".
`GENERATED_SKILL_COPIES` and `CURATION_DOCTRINE_SURFACES` define the sweep: the canonical `skills` tree
plus the nine copies `scripts/sync-skills.py` owns — a stale copy is a real defect, because a seat on that
harness reads the old sentence.

### Conventions

- The registry is a **census of surfaces**, not a single-file check: a statement is reported only on a
  file that shipped it.
- The module reads bytes and reports strings; it asserts nothing and imports no repository constant.
- Extending coverage means adding a registry row with its real `sources`, never widening a matcher.

### Invariants And Boundaries

- **This is not a semantic check, and the module says so.** A corpus that denied the rule in fresh
  vocabulary this registry has never seen would pass. What it buys is that the exact retired sentences
  cannot come back and that the shipped corpus keeps the sentence stating the rule.
- A restatement of the defect in new words is out of reach of the matcher; the guard does not claim to
  read meaning.
- The module owns the reading half only. The falsifiability half — the seeded re-insertion proving the
  guard can fail — lives in the test module that calls it.

## Docs References

No external or domain documentation governs this repository-local test-support module; it encodes the
shipped instruction corpus and the ruling that retired those sentences.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

The module is the census the shipped-corpus guard reads. Its registry is the **retired** side and
`CURATION_COMPLETENESS_STATEMENTS` the **required** side; the cases that consume both, and the seeded run
that proves the guard can red, are in `mcp/tests/test_role_instruction_corpus.py`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The retired-sentence registry carries the exact statement, its shipped sources, its probe and its packet fragment. | `RETIRED_CURATION_STATEMENTS` | mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py:76-205 |
| The required-rule table names the exact form each canonical surface must state, keyed by shipped path. | `CURATION_COMPLETENESS_STATEMENTS`; `COMPLETE_CURATION_RULE` | mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py:34-34; mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py:207-254 |
| The nine generated copies are the sweep targets, and the canonical tree is sweep target zero. | `GENERATED_SKILL_COPIES`; `CURATION_DOCTRINE_SURFACES` | mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py:38-51 |
| The readers answer the per-surface and per-tree questions separately, and the completeness reader is the required-rule half. | `retired_statement_findings`; `doctrine_files`; `retired_curation_findings`; `missing_completeness_statements` | mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py:261-333 |
| The consuming cases and the seeded re-insertion that proves the guard can fail. | `CurationIsCompleteOnEveryLeafTests`; `CurationGuardTeethTests` | mcp/tests/test_role_instruction_corpus.py:640-773 |
| The nine copies are produced from the canonical tree by the generator whose `--check` proves currency. | `TARGETS`; `sync_targets` | scripts/sync-skills.py:43-50; scripts/sync-skills.py:204-228 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: created this card for
  `mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py`, the new untracked
  support module this leaf added. It carries the retired-sentence registry and the required-rule table
  the shipped-corpus guard reads, and its own declared limit (it is a census of surfaces, not a semantic
  check). Verification metadata is left at the leaf base commit because the source is uncommitted — the
  governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
