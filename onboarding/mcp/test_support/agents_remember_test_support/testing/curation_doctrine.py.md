# mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py

## Governing Overview

[Python Test Evidence Infrastructure Overview](overview.md)

## Purpose

The reading half of the shipped curation-instruction guard: normalized exact retired-wording
scans remain separate from the positive policy check for the two compact native curation
sources. The normal MIK authoring policy requires complete memory quality and coherence;
report-only admission does not claim that authoring pass complete. The module is free of
pytest and repository constants so its callers can inspect staged or synthetic trees.

## Current source account

The positive policy table now names only operations/curation.md and roles/curator.md and is read through missing_curation_policy_statements. It retains the normalized exact retired-wording and loop-gate scanners. MIK-R72@v2 rebuilt the retired set on the shipped-sentence contract: rows whose statement shipped on a named base surface are kept with that surface in `sources`, each with a distinctive probe that matches no kept live wording and a v2 reason naming the sentence’s specific obsolete duty; rows built only from this leaf’s unlanded drafts were removed, and the four adopted manifest descriptions are registered. This is an exact wording guard; novel semantic contradictions are outside that scan.

## Code Commentary

### Logic

`RETIRED_CURATION_STATEMENTS` is the registry of exact retired sentences, including the
prototype wording that made the normal complete operation developer-request-only. Each row carries the exact
`statement`, the `sources` tuple naming the files that actually shipped it, a short `probe`, and a
`reason` naming which packet fragment it was. `sources` is load-bearing in both directions: it is the set
in which the sentence is a defect **when it returns**, and it keeps a retained doctrine — an explicit
developer request still governs full code quality and full tests — from reading as a regression.

`CURATION_POLICY_STATEMENTS` names only `operations/curation.md` and `roles/curator.md`.
Each declares its complete-curation rule and `prepare → publish → validate` marker.
`missing_curation_policy_statements` reports a missing file or a file carrying none of its
declared markers; its `any` check alone does not establish that both markers survive.
The canonical test checks every marker, while exact generated-copy byte equality is the
stronger delivery proof.

Matching is on a **normalized reading** — `normalize_statement` strips markdown emphasis and collapses
line wrapping — and against the **whole** retired sentence, so a statement re-inserted with different
emphasis or at a different column is still the same statement, while doctrine that legitimately survives
cannot read as a regression. The `probe` is what a report and a failure message name the row by; it is
deliberately **not** the matcher.

The readers split by question: `retired_statement_findings(reading, surface_relative_path)` answers "is
this one retired sentence present on this one surface", `doctrine_files` and `retired_curation_findings`
sweep a tree, and `missing_curation_policy_statements` answers whether each declared compact source carries
at least one current policy marker.
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
  cannot come back; the compact positive check has the explicit marker-presence limit above.
- A restatement of the defect in new words is out of reach of the matcher; the guard does not claim to
  read meaning.
- The module owns the reading half only. The falsifiability half — the seeded re-insertion proving the
  guard can fail — lives in the test module that calls it.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The curation-doctrine registry keeps its single owner and matcher for retired curation sentences and field facts. The retired leaf-handover wording moved into its own data module (`retired_leaf_handover_wording.py`), the register now holds only actually retired sentences with exact carriers and probes, and compound preserved-plus-obsolete text was split into independent source-addressed rows.

## Evidence

### Docs References

No external or domain documentation governs this repository-local test-support module; it encodes the
shipped instruction corpus and the ruling that retired those sentences.

No relevant documentation found after checking live sources.

### Repo-Internal References

The module is the census the shipped-corpus guard reads. Its registry is the **retired** side and
`CURATION_POLICY_STATEMENTS` the **compact positive-policy** side; the canonical every-marker
case, generated-copy marker reader and seeded retired-wording controls live in
`mcp/tests/test_role_instruction_corpus.py`. The marker reader retains the `any` limit
described above.

- The retired-sentence registry carries the exact statement, its shipped sources, its probe and its packet fragment. [1]

- The required-rule table names the exact form each canonical surface must state, keyed by shipped path. [2]

- The nine generated copies are the sweep targets, and the canonical tree is sweep target zero. [3]

- The readers answer the per-surface and per-tree questions separately, and the completeness reader is the required-rule half. [4]

- The consuming cases and the seeded re-insertion that proves the guard can fail. [5]
- The nine copies are produced from the canonical tree by the generator whose `--check` proves currency. [6]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
