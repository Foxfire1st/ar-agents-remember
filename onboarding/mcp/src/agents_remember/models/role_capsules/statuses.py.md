# mcp/src/agents_remember/models/role_capsules/statuses.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/statuses.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

The stable refusal vocabulary for role-capsule compilation: one code per defect class, in its
own module, so a caller can branch on a code without importing the module that raises it and
so two refusal sites cannot drift into two spellings of the same status. The wording that
accompanies a code is for an operator; **the code is the contract**.

## Code Commentary

### Logic

Thirteen codes are declared as module constants
cit:([`STATUS_UNKNOWN_ROLE`, `STATUS_UNKNOWN_OPERATION`, `STATUS_OPERATION_NOT_APPLICABLE`, `STATUS_MISSING_REQUIRED_INSTRUCTION`, `STATUS_SOURCE_NOT_DECLARED`, `STATUS_SOURCE_ROOT_MISMATCH`], mcp/src/agents_remember/models/role_capsules/statuses.py:11-16),
cit:([`STATUS_DUPLICATE_IDENTITY`, `STATUS_EQUAL_AUTHORITY_CONTRADICTION`, `STATUS_UNKNOWN_SUPERSESSION`, `STATUS_SUPERSESSION_CONFLICT`, `STATUS_SPECIALIZATION_NOT_ADMITTED`, `STATUS_TOOL_REQUEST_NOT_PERMITTED`, `STATUS_TASK_CONTEXT_DIGEST_MISMATCH`], mcp/src/agents_remember/models/role_capsules/statuses.py:17-23), and
cit:([`CAPSULE_STATUSES`], mcp/src/agents_remember/models/role_capsules/statuses.py:27-41) registers every one of them in a single tuple "so a consumer can enumerate the surface and
so a new code added without being registered here is caught by its own test".

Two families hide inside that flat list, and the difference matters operationally:

- **caller-input defects** — `unknown-role`, `unknown-operation`, `operation-not-applicable`,
  `missing-required-instruction`, `source-not-declared`, `source-root-mismatch`,
  `specialization-not-admitted`, `tool-request-not-permitted`. These name something the caller
  or the authored manifest got wrong and can be repaired.
- **integrity defects** — `duplicate-identity`, `equal-authority-contradiction`,
  `unknown-supersession`, `supersession-conflict`, `task-context-digest-mismatch`. These say two
  admitted things disagree; `equal-authority-contradiction` is the **stopped conflict** where
  compilation halts rather than picking a winner by filename, path order, or "last one wins".

The value layer raises a further set of source-admission codes that are deliberately **not** in
this tuple, because they belong to holding or reading a source rather than to compiling a
capsule: `source-root-invalid`, `source-root-missing`, `source-missing`, `source-path-invalid`,
`source-path-escapes-root`, and `duplicate-identity` for a path requested twice in one admission
(`application/role_capsules/sources.py`); plus **`source-not-utf8`**, raised when a source's
bytes do not decode as UTF-8, and the revision/blank-content refusals beside it in
`models/role_capsules/sources.py`.

**Two homes, one caveat.** `duplicate-identity` exists in *both* vocabularies — once as a
registered compiler code (the same obligation stated twice) and once as an admission code (the
same path requested twice). They are different defect classes that happen to share a spelling, so
a branch on that string must say which layer raised it.

### Conventions

Add a code here, register it in `CAPSULE_STATUSES` in the same edit, and let the shipped
completeness test hold the pair together. A prose sentence may change freely; a code string
is a breaking change for every caller that branches on it.

### Invariants And Boundaries

- A status string is a stable branching contract, not a message. Do not reuse a code for a
  second defect class and do not reword an existing one.
- Every code has exactly one home: a code raised in two modules must not drift into two
  spellings.
- `CAPSULE_STATUSES` is the enumerable surface. A code that exists as a constant but is absent
  from the tuple is a registration defect, and the shipped test is what catches it.
- The source-admission codes outside this tuple are intentional; do not "complete" the list by
  importing them, because a compiler refusal and a source refusal are different failure classes
  with different remedies.
- **`source-not-utf8` is a real code** and is raised by `models/role_capsules/sources.py` when a
  source's bytes do not decode; do not record it as nonexistent, and do not look for it in the
  application layer.
- `duplicate-identity` is spelled identically in two layers with two meanings. A caller branching
  on it must distinguish "the same obligation stated twice" (compiler) from "the same path
  requested twice in one admission" (admission).

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The completeness and uniqueness guard over this vocabulary. | `test_every_documented_refusal_code_is_registered_exactly_once` | mcp/tests/test_role_capsule_admission.py:166-184 |
| The typed refusal that carries a status, its detail, a remedy, and structured conflict rows. `CapsuleBindingError` was removed on the A3 candidate and must not be cited. | `CapsuleCompilationError`; `CapsuleManifestError`; `CapsuleSourceError` | mcp/src/agents_remember/errors.py:464-507; mcp/src/agents_remember/errors.py:508-511; mcp/src/agents_remember/errors.py:512-513 |
| The equality-conflict case that stops compilation instead of choosing by accident. | `_require_one_identity`; `_supersessions` | mcp/src/agents_remember/models/role_capsules/resolution.py:221-261; mcp/src/agents_remember/models/role_capsules/resolution.py:262-284 |
| The source-admission codes raised outside this tuple, in the application layer. | `_require_root`; `_read`; `_require_confined_relative` | mcp/src/agents_remember/application/role_capsules/sources.py:107-123; mcp/src/agents_remember/application/role_capsules/sources.py:124-159; mcp/src/agents_remember/application/role_capsules/sources.py:169-196 |
| **`source-not-utf8`** and the revision/blank-content refusals, raised in the value layer rather than the application layer. | `CapsuleSource` | mcp/src/agents_remember/models/role_capsules/sources.py:49-118 |
| The tool-policy refusal raised when a request falls outside the admitted snapshot. | `narrow_tool_requests` | mcp/src/agents_remember/models/role_capsules/tools.py:24-58 |

## Cross-Repo References

No sibling-repository contract consumes these codes; they are internal to the AR capsule
compiler.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, and corrected **my own earlier error**. The created entry below said the outside-the-tuple codes belong to "reading a tree" and did not mention UTF-8; my curation report went further and stated that `source-not-utf8` **does not exist**, based on grepping only the application layer. That was wrong: the code is real and is raised in `models/role_capsules/sources.py` when a source's bytes do not decode, alongside the revision and blank-content refusals. Rewrote the paragraph to name `source-not-utf8` and to place the codes by *layer* (value-layer source admission vs application-layer tree admission) rather than calling them all "application boundary"; added an invariant blocking the nonexistence claim; and recorded the `duplicate-identity` two-homes caveat — the same spelling carries two meanings in two layers, so a branch on it must name the raising layer. Refreshed every range in this card. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the role-capsule refusal
  vocabulary added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  thirteen registered codes, the caller-input versus integrity split, the
  `equal-authority-contradiction` stopped-conflict case, the `CAPSULE_STATUSES` registration
  invariant, and the separate application-layer source-admission codes that are deliberately
  outside the tuple. Verification metadata is left at the leaf base commit because the source is
  uncommitted — the governed closeout stamps the real code commit.
