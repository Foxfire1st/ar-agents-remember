# mcp/test_support/agents_remember_test_support/testing/curation_doctrine.py

## Governing Overview

[Python Test Evidence Infrastructure Overview](overview.md)

## Purpose

The reading half of the shipped curation-instruction guard: normalized exact retired-wording
scans remain separate from the positive policy check for the two compact native curation
sources. The normal MIK authoring policy requires complete memory quality and coherence;
report-only admission does not claim that authoring pass complete. The module is free of
pytest. Its projection census is derived from the canonical repository declaration; callers still supply staged or synthetic trees for the scans.

## Current source account

The positive policy table names only operations/curation.md and roles/curator.md and is read through missing_curation_policy_statements. It retains the normalized exact retired-wording and loop-gate scanners. Each retired row keeps the base surface that shipped its statement in `sources`, with a distinctive probe that matches no kept live wording and a reason naming the sentence’s specific obsolete duty. This is an exact wording guard; novel semantic contradictions are outside that scan.

## Code Commentary

### Logic

`RETIRED_CURATION_STATEMENTS` is the registry of exact retired sentences, including the
prototype wording that made the normal complete operation developer-request-only. Each row carries the exact
`statement`, the `sources` tuple naming the files that actually shipped it, a short `probe`, and a
`reason` naming which packet fragment it was. `sources` is load-bearing in both directions: it is the set
in which the sentence is a defect **when it returns**, and it keeps a retained doctrine — an explicit
developer request still governs full code quality and full tests — from reading as a regression.

`CURATION_POLICY_STATEMENTS` names only `operations/curation.md` and `roles/curator.md`.
The operation tuple declares its complete-curation rule, the `prepare`, `publish`, `validate` order, the complete check set with a per-check result, the full `memory_quality_check` operation, repair or escalation of every Curator-actionable finding, the repeat-until-ready condition and the coherence continuation. The Curator role tuple declares two pointer sentences that send the reader to the operation's complete-curation-checks and authority-gates sections before it acts, each naming the tool it asks for (`memory_quality_check` and `curator_coherence` on `agents-remember-task`).
`missing_curation_policy_statements` reports a missing file or a file that lacks any one of its
declared clauses; a source passes only when every declared clause is present.
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
every one of its declared policy clauses.
`GENERATED_SKILL_COPIES` and `CURATION_DOCTRINE_SURFACES` define the sweep: the canonical `skills` tree
plus every skills target declared by generated-copies.json, currently the single packaged runtime tree. A stale served copy remains a defect.

### Conventions

- The registry is a **census of surfaces**, not a single-file check: a statement is reported only on a
  file that shipped it.
- The module reads bytes and reports strings without importing pytest. At import it reads the module-owned repository declaration through `DECLARATION_PATH`/`parse_generated_copies` to derive generated skill targets; this is not a no-repository-input module. Callers still choose the tree they scan.
- Extending coverage means adding a registry row with its real `sources`, never widening a matcher.

### Invariants And Boundaries

- **This is not a semantic check, and the module says so.** A corpus that denied the rule in fresh
  vocabulary this registry has never seen would pass. What it buys is that the exact retired sentences
  cannot come back; the compact positive check is likewise an exact clause-presence check.
- A restatement of the defect in new words is out of reach of the matcher; the guard does not claim to
  read meaning.
- The module owns the reading half only. The falsifiability half — the seeded re-insertion proving the
  guard can fail — lives in the test module that calls it.

## Retired leaf-handover wording

The curation-doctrine registry keeps its single owner and matcher for retired curation sentences and field facts. The retired leaf-handover wording lives in its own data module (`retired_leaf_handover_wording.py`); this module turns each of its source/sentence pairs into an independent source-addressed row with an exact carrier and probe.

## Developer-question and forwarding rows

`RETIRED_CURATION_STATEMENTS` holds independently source-addressed rows for the replaced role and operation developer-question sentences, the exact Manager/Orchestrator forwarding prohibition on both carriers, and the SKILL own-chat directive separated from the old coordinator exception. Each row carries its exact carrier, a distinctive probe and its specific reason. `test_developer_question_wording.py::test_exact_retired_directives_are_detected_as_independent_sentences` is the focused four-case control: each of the four named carrier/sentence pairs alone is reported while the undeclared current carrier stays clean. The every-row/per-carrier proof is the existing `mcp/tests/test_role_instruction_corpus.py::CurationGuardTeethTests::test_reinserting_each_retired_statement_is_detected_on_its_own_surface` loop over the registered statements.

## Leaf-set and held-delivery retired wording

The retired registry additionally names the actual shipped sentences replaced by sibling set preparation, the single-live-leaf-seat resolver, direct Worker freeze delivery and product-owned permission waiting. Their source-confined probes protect the old wording without changing the matcher into a semantic review. The positive stage-start duties belong to `leaf_instruction_wording.py`; no test-support function starts a role or writes knowledge.

## Current scoped contract

The Curator positive entry requires both of its pointer sentences, each naming its section anchor in `operations/curation.md` and its tool; the operation entry requires all seven of its clauses. This is an exact clause-presence check, not a wider retirement matcher or an automatic meaning check; retired matching stays source-confined.

## Evidence




### Docs References

No external or domain documentation governs this repository-local test-support module; it encodes the
shipped instruction corpus and the ruling that retired those sentences.

No relevant documentation found after checking live sources.

### Repo-Internal References

The module is the census the shipped-corpus guard reads. Its registry is the **retired** side and
`CURATION_POLICY_STATEMENTS` the **compact positive-policy** side; the canonical every-marker
case, generated-copy marker reader and seeded retired-wording controls live in
`mcp/tests/test_role_instruction_corpus.py`. The marker reader requires every declared clause.






- The readers answer the per-surface and per-tree questions separately, and the completeness reader is the required-rule half, requiring every declared clause. [4]

- The consuming cases and the seeded re-insertion that proves the guard can fail. [5]
- The repository sync script checks the declared package projection against canonical skills. [6]
### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.




- The retired-sentence registry carries the exact statement, its shipped sources, its probe and its reason. [1]

- The required-rule table names the exact clauses each compact curation source must state, keyed by shipped path. [2]

- The operation tuple carries `COMPLETE_CURATION_RULE` and the six other curation clauses; the Curator tuple carries two pointer sentences into the operation's sections. [8]
- A compact source passes only when every declared clause is present. [9]


- The sweep adds canonical skills to every target from the generated-copy declaration, currently the single packaged runtime tree. [3]

- The generated skill census is derived from the canonical declaration through its parser rather than a duplicated tuple. [7]
