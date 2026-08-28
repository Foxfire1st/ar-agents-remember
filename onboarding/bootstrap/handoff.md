# PDLS Verification-Ownership Onboarding Maintenance Handoff

## Status

This handoff supersedes the earlier pre-review claim that PDLS onboarding was structurally final.
The independent review reopened the implementation, and the source ownership model changed during
remediation. Verification provenance remains intentionally blank until the candidate is committed
and closeout can stamp the real code commit.

## Applied Delta

Python quality and pytest infrastructure moved from operational product authority at
`mcp/src/agents_remember/{code_quality,testing}` to the explicit verification package at
`mcp/test_support/agents_remember_test_support`. The certifying pytest bootstrap moved with it.
No compatibility sidecars or duplicate route overviews remain at the retired source route.

Three route-local overviews now govern the verification root, quality producer, and test/evidence
infrastructure. Their file cards document:

- exhaustive product-versus-verification package authority;
- static checks over both authorities and behavioral scoring over product only;
- explicit exhaustive evidence lanes with no unmarked-unit default;
- source-derived dependency/plugin/consumer facts with lifecycle declarations as a cross-check;
- a 34-artifact lifecycle catalog with real owner/node contracts;
- exact-node causal suppression with same-file independent execution;
- persistent, integrity-bound retry proof in the locked Dagger cache on the actual CI route; and
- diagnostic, cadence, retry, causal, and route-measurement evidence as non-accepting.

The Dagger quality graph now separates reusable candidate construction from attempt state. Pinned
image/dependency setup, exact candidate reconstruction, and the editable install form the stable
base; retry cache, nonce, attestation, and report destinations bind only afterward. A focused graph
test refuses any attempt-specific cache or environment input before the editable install, preventing
identical evidence candidates from rebuilding multi-gigabyte setup layers for each nonce.

## Structural Census

The moved route contains 50 current Python source files and exactly 50 file-level onboarding
sidecars. The retired product routes contain zero matching source files and zero onboarding
sidecars. Wave 005 also supplies the six previously missing focused test sidecars and file cards
for cadence, causal localization/preflight, evidence lanes/lifecycle, and route measurement. The
deterministic route-index generator must be refreshed after that delta, and a repeat dry run must
report zero stale indexes before closeout.

## Remaining Candidate Boundary

This maintenance pass does not assert that the master is accepted. v21 is historical because two
stale source comments were corrected during cold read; the successor identity is frozen only after
this memory pass is clean. Candidate-specific measurements,
rollback proof, the frozen-finding delta review, and the final exact-candidate Dagger gate remain in
the PDLS task reports. Closeout must stamp the resulting code commit, run the memory-quality gate,
align the ledger, and preserve the review's historical process violations rather than rewriting
them as green.

## Update History

- 2026-08-28T06:40+02:00 — Corrected the lifecycle inventory to 34 artifacts, completed the six
  missing focused test cards, and recorded v21 as historical pending the successor freeze.
- 2026-08-28T02:38+02:00 — Added the verified Dagger candidate-base/attempt-binding boundary that
  stopped nonce-specific evidence runs from invalidating identical dependency and source setup.
- 2026-08-27T11:14+02:00 — Replaced the obsolete pre-review handoff with the explicit
  verification-ownership, lane, retry, lifecycle, causal, and generated-index delta.
