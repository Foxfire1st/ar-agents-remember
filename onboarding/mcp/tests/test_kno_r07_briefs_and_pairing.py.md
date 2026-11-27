# mcp/tests/test_kno_r07_briefs_and_pairing.py

## Governing Overview

[tests](overview.md)

## Purpose

Focused unit test suite proving KNO-R07 rules 1–7: post-landing advisory brief refresh and `briefsProblem` projection, honest `read_ar_files` brief-freshness notices, readable clause fallback titles, the `memory-briefs` CLI, and automatic code-tree pairing including dirty working-tree pagination.

## Code Commentary

- Verifies `LANDING_KEPT_KEYS` retains `"briefsProblem"` on `worktree_integrate`, `worktree_checkpoint_landing`, and `worktree_record_landing`, that `refresh_integrated_memory_briefs` skips ledger-only commits and returns advisory errors on failure, and that `refresh_recorded_landing_memory_briefs` refreshes only matching-`HEAD` checkouts while reporting unpulled guidance otherwise.
- Verifies `short_answer` (`whole`, `without_rule_texts`, `counts_notice`) omits `"Read the current brief"` wording when `BriefLocation.current` is `False`, and `clause_title`/`rule_title` cover sentence, clause, and word-boundary fallbacks without mutating stored records.
- Exercises `cli_main(["memory-briefs", ...])` for both converted refresh (exit `0`) and legacy refusal (`state == "legacy-format"`, exit `2`).
- Exercises `knowledge_read_payload` on non-Git Projects mounts, proving zero-unverifiable auto-pairing across two-page `source_context` continuations, leaf-worktree precedence over configured `main`, dirty working-tree observation (`object_directory`), and refusal when a dirty working tree changes between pages.

## Relationships

- Tests `worktrees/landing_briefs.py`, `cli/memory_briefs.py`, `application/knowledge_code_pairing.py`, `application/file_briefs/{short_answer,titles}.py`, `application/landing_answer_shapes.py`, and `mcp/tools/knowledge.py`.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit` lane) and `mcp/tests/evidence-lifecycle.toml`; sibling of `mcp/tests/test_kno_r07_knowledge_queries.py`.

## Evidence

- Verifies `refresh_integrated_memory_briefs` skips ledger-only commits and refreshes on non-ledger content changes. [1]
- Verifies `refresh_recorded_landing_memory_briefs` refreshes matching `HEAD` checkouts and returns explicit pull/CLI guidance when unpulled. [2]
- Verifies `memory-briefs` CLI refreshes converted checkouts (exit 0) and refuses unconverted checkouts as `legacy-format` (exit 2). [3]
- Verifies leaf sibling worktree precedence over configured `main` and dirty working-tree observation with 0 unverifiable rows. [4]
- Verifies dirty working-tree two-page continuation resumes unchanged and refuses after working-tree mutation. [5]
