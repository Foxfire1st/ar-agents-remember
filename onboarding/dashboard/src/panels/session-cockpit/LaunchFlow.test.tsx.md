# dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The LaunchFlow jsdom matrix (260715-FEUI-L3 S2/S3/S6): dynamic-only pickers, miss/refresh
cost-naming parity, complete-pair gating with default re-gating, advertised-order rendering, all
four open-response paths, and the F9 unknown-outcome catalog reconciliation — including the two
fix-round regression nets (dismiss ends the watch; reopen starts clean).

## Code Commentary

### Logic

- **Dynamic-only (R1/R4)** (L85-L165) — the gated-promise case proves ZERO model options exist
  BEFORE the daemon answers (the capability response is held behind an unresolved promise while
  the loading state is asserted), then the released envelope populates the five Claude rows in
  advertised order; an undetected harness is disabled AND its adapter word renders as visible
  text (review finding 6, L119-L129); a hidden codex row never renders (L131-L138); a 503 renders
  the VERBATIM `control-unavailable: …` detail with a working retry (L140-L164).
- **Cost honesty (R2)** (L167-L190) — miss-loading and the explicit refresh carry the SAME
  `capabilityCostNote` naming; the loaded state names the cache truth ("cache miss …same
  short-lived native discovery as a refresh").
- **Complete-pair rules (R4)** (L192-L250) — model selection re-gates effort to THAT row's
  advertised default and re-gates again on switch (sol=low → spark=high); a model with no
  advertised launch default disables submit until an explicit effort choice; efforts render in
  advertised native order (`low…ultra`, asserted as an ordered array); the effortless Haiku row
  states no pair can be formed and submit stays disabled; vendor defaults sends NEITHER knob —
  asserted by key ABSENCE in the parsed POST body (L236-L249).
- **Response paths (R5)** (L252-L337) — 200 ⇒ retained pair recorded at tier `'pending'` in
  `sessionCockpitStore`, new session focused, flow closed; 400 `launch-selection-invalid` ⇒ the
  verbatim detail, nothing retried; 409 leaf-taken ⇒ names the owning session + focus-owner
  action; 409 conflict ⇒ live retained pair vs attempted rendered side by side AND the store is
  asserted to hold NO evidence for the live session; transport loss ⇒ "open outcome unknown —
  checking the catalog", resolved WITHOUT re-POST when the caller-minted id appears in a
  rerendered `sessions` prop (F9).
- **Fix-round regression nets** (L339-L424) — "an explicit dismiss ENDS the unknown-outcome
  watch" (review finding 1): dismiss, then the row surfaces while `open=false` — `onFocusSession`
  never fires and `onClose` stays at one call; "REOPEN after a dismissed unknown outcome starts
  clean" (the delta-verify residual): the row lands while closed, the flow reopens — the stale id
  must not fire on the first effect pass.

### Conventions

`stubFetch(router)` stubs a URL-routing global fetch (L28-L57; `defaultRouter` wires the harness
list, claude/codex envelopes, and a parameterized open response); `renderFlow` pins
`mintSessionId={() => "launch-1"}` so the F9 assertions can address the minted id; both stores
reset in `beforeEach`. Test-only.

### Invariants And Boundaries

The gated-promise case is the dynamic-only regression net (it fails if ANY option is invented
before the daemon answers, not merely if options eventually differ); the vendor-defaults case
pins wire-level key ABSENCE; the two F9 cases are the fix-round nets and fail against pre-fix
code in exactly the reviewed failure modes.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The dialog under test. | L165-L613 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| The envelope fixtures the routers serve. | L1-L273 | [../../test/fixtures/capabilityEnvelopes.ts](../../test/fixtures/capabilityEnvelopes.ts) |
| The open-response fixtures (200/400/409×2). | L1-L178 | [../../test/fixtures/openResponses.ts](../../test/fixtures/openResponses.ts) |
| The shared row builder used for the F9 appeared-row rerenders. | L10-L27 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The store the 200-path evidence assertion reads. | — | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 S6 (R1/R2/R4/R5, extended in fix rounds 1-2
  with the dismiss-ends-watch and reopen-starts-clean F9 regression cases and the visible
  adapter-status assertion): the full jsdom matrix over dynamic-only pickers, cost parity, pair
  rules, and every open-response path. Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
