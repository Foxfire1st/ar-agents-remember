# mcp/tests/test_closeout_kept_rules_pins.py

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Pins the retained closeout rules: required intent for enabled code/memory outputs, normalized
nonblank messages, source ancestry, and Git-based integration replay requirements.

## Code Commentary

### Logic

R1 and R2 now operate on the enabled content pair. The blank-message matrix covers `code` and
`memory`; absence and whitespace are reported for every enabled leg. Supplying code intent alone
still refuses for the missing memory intent, while supplying both succeeds without a ledger leg.
Normalized effective input preserves the two messages and has no serialized ledger member.

R3 uses real commits to distinguish a source still at its recorded base, a source at a checkpoint's
recorded integrated head, and unrelated source movement. The accepting checkpoint case retains its
moved-source refusal companion.

R4 reads integration replay requirements from actual Git ancestry. Its retired-recovery assertion
keeps the removed torn-ref recovery entry points absent; it does not require a ledger row or a
separate operation record to prove ancestry.

### Conventions

Rule-labelled pytest functions keep each retained requirement visible. Message cases are hermetic;
ancestry cases create real temporary repositories. The function inventory is separate from expanded
parameter counts and from execution/acceptance evidence.

### Invariants And Boundaries

- Every enabled real output still requires explicit nonblank intent.
- The derived cache adds no third commit-message requirement.
- Accepting a checkpoint's admitted head cannot hide unrelated source movement.
- Actual Git ancestry, not cached rows or retired records, supplies replay facts.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- The enabled plan and message checks cover code and memory only. [1]
- Both content messages are required without a ledger leg. [2]
- Real ancestry covers base, checkpoint head, and unrelated movement. [3]
- Replay uses Git facts and the retired recovery API remains absent. [4]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
