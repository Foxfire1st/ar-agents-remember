# mcp/tests/test_activation_admission_registered.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

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
unreadable-contract case also proves that a malformed parser's 9099-character reason remains bounded in
top-level and nested refusal detail while its source bytes remain unchanged. The fixture is disposable;
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
worker evidence rather than Gate 5 certification. Cases assert on the public JSON payload rather than
importing projection helpers, so a payload key that regains a foreign-master concept is caught here.

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
- Oversized unreadable detail is bounded in both status and sync projections without changing source bytes. [4]
- Startup edge mismatch retains expected and observed branch evidence. [5]
- Authoritative startup reread preserves edge evidence when the contract drifts after upstream refresh. [6]
- Unreadable startup contracts retain the concrete parser reason in refusal and observed evidence, including bounded oversized parser detail and unchanged source bytes. [7]
- The shared admission explainer no longer emits `classification`/`blocking`, and keys the refusal to the observed contract fingerprint. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for this disposable registered fixture.

The fixture does not establish a live external integration.
