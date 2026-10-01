# mcp/src/agents_remember/models/role_capsules/statuses.py

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

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The completeness and uniqueness guard over this vocabulary. [1]
- The typed refusal that carries a status, its detail, a remedy, and structured conflict rows. `CapsuleBindingError` was removed on the A3 candidate and must not be cited. [2]
- The equality-conflict case that stops compilation instead of choosing by accident. [3]
- The source-admission codes raised outside this tuple, in the application layer. [4]
- **`source-not-utf8`** and the revision/blank-content refusals, raised in the value layer rather than the application layer. [5]
- The tool-policy refusal raised when a request falls outside the admitted snapshot. [6]

### Cross-Repo References

No sibling-repository contract consumes these codes; they are internal to the AR capsule
compiler.

No meaningful cross-repo references found.
