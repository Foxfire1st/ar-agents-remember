# mcp/tests/test_activation_admission_registered.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

### STOP-delta current source contract

Registered-adapter readiness/admission facts are recovered from the answer log. Foreign-master exclusion, bounded parser reason, fingerprints and addressed action assertions remain. A compact answer and its retained detailed result are different carriers.

These are current source/assertion-carrier meanings. The qualified attempt14 CODE verdict is inherited, not a Curator test run, native freeze-currentness certification or independent MEMORY acceptance. Earlier contrary accounts are historical only; unaffected contracts and typed provenance remain.

Registered FastMCP proof for actionable atomic-series activation admission and read-only status
evidence. The admission payload is contract-scoped: it explains the addressed contract's own state and
never names a foreign master as the blocker.

## Code Commentary

### Logic

`RegisteredActivationAdmissionTests` builds temporary code/coordination roots and calls the real
registered `worktree_status`, `worktree_sync`, and `worktree_start` tools. It reuses
`ActivationFixture`'s two sprint-commanded masters, so the fixture's two contracts share one protected
source pair — the shape that used to make the second selection name the first master as
`atomic-series-paused-by:`.

The cases prove that status exposes an active contract's own activation fact without mutating record
bytes, that the sync refusal addresses **only the addressed contract's own state**, that vacant and
unreadable activation snapshots remain distinct corrective evidence, that oversized unreadable
diagnostics retain a bounded parser-error prefix, and that persisted master edge mismatches retain
expected/observed branch facts across both the initial and authoritative reread paths. The
unreadable-contract case derives the malformed parser reason's length from the 9000-character
invalid kind and the actual contract path. Oversized parser/admission diagnostics stay in that call's whole-result log; the ordinary delivered refusal itself must fit the unchanged answer
bound without overflow, with code, summary and an executable next step, no error field
and no admission/redundant guidance table. The malformed input, concrete parser prefix,
contract identity, original admission facts and retry arguments remain separately checked.
The malformed source bytes remain unchanged. The fixture is disposable;
it does not prove a live control-plane run or acceptance.

The refusal case is the contract-scoping forcing test. With contract A vacant and contract B live, the
`worktree_sync` refusal for A asserts that the admission carries no `classification`, `blocking`,
`sourcePair` or `sourcePairFingerprint` key, that `admission["contractFingerprint"]` equals A's own
fingerprint and differs from B's, that the status action binds A's contract path, that the retry
precondition is A's own "not sufficient to continue", that B's task path never appears in the response
text, and that A's record bytes are unchanged. A foreign live master is therefore never a retry
precondition or a scheduling block. The redirected-reread and unreadable-contract helpers assert the
same absence directly on the admission dict.

### Conventions

This file is integration evidence because it crosses the registered MCP transport. Its assertions
describe response shape and byte-preservation boundaries; collected counts and focused passes remain
worker evidence rather than Gate 5 certification. Cases assert the delivered public outcome and the file-backed whole refusal rather than
importing projection helpers. Oversized nested diagnostics need not appear in the delivered short
answer; their exact contract ownership is checked in its logged result.

### Invariants And Boundaries

- Selector/status projections remain read-only in the status and refusal paths.
- An admission refusal describes the addressed contract only: it carries no `classification`,
  `blocking` or `sourcePair*` key and never names another master as blocker or precondition.
- A logical `active` or `reconciling` selection is not treated as proof of a live process.
- Temporary fixture state cannot establish production scheduler, Dagger, or master-aggregate behavior.

## Evidence

### Docs References

No Domain Documentation entries are configured for this repository-owned integration fixture
(`system/sources.md` declares no entries).

No external domain evidence applies.

### Repo-Internal References

- Registered status projects activation without mutation. [1]
- The sync refusal addresses only the addressed contract's own state: no `classification`/`blocking`/`sourcePair*` key, this contract's fingerprint and status action, and a foreign live master named nowhere. [2]
- Vacant and unreadable snapshots remain distinct and unchanged. [3]

- Oversized status and sync refusals keep bounded whole-result diagnostics in their logs and preserve malformed source bytes. [4]

- Startup edge mismatch retains expected and observed branch evidence. [5]
- Authoritative startup reread preserves edge evidence when the contract drifts after upstream refresh. [6]

- Unreadable startup contracts retain concrete bounded parser reason and admission in the logged whole refusal; delivered overflow identity and retry guidance are checked separately. [7]

- The shared admission explainer no longer emits `classification`/`blocking`, and keys the refusal to the observed contract fingerprint. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for this disposable registered fixture.

The fixture does not establish a live external integration.

- Registered-adapter readiness/admission facts are recovered from the answer log. Foreign-master exclusion, bounded parser reason, fingerprints and addressed action assertions remain. A compact answer and its retained detailed result are different carriers. [9]


- Registered refusal assertions require bounded no-overflow code/summary/next operation and retain detailed admission/parser evidence in the log. [10]
