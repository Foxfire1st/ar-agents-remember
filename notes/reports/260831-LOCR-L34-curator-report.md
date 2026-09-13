# 260831-LOCR-L34 Curator Coherence Report

| Field | Value |
| --- | --- |
| Master / leaf | `260831_lifecycle-owned-completion-relay` / `260831-LOCR-L34` |
| Role | curator |
| Code worktree | `ar/260831-locr-l34` at base `723fd2f1becc130d85d7a6b285b93115be0df852` |
| Memory worktree | `ar/260831-locr-l34` at base `5a3e54035f410d04b011c9715d03b2a32de8ef5c` |
| Coherence record | `858c1afcbd3e168d4a284ef6fb15d9597e3f377d97589bc1241b89bf612a69f4` |
| Final checklist | `ready-for-closeout`, `closeoutReady: true`, `curatorActionableCount: 0` |
| Coherence status | `current` (valid across all nine axes) |

## Citation adjudication

The contract-scoped `memory_quality_check` opened with 61 enforced
`style.citations.claim_reopen` findings and closed with 0. The enforcement
split into three patterns, not 61 one-offs.

**Projected ranges (33).** A CCR-R10 mechanical anchor-range projection had
rewritten these claims' cited ranges, and the generated Update History bullet
that records the rewrite is what raised the item from report-only to enforced.
The clearing mechanism is therefore re-anchoring: `claim_reopen.surfaced_finding`
only escalates to `error` while a `Generated citation repair` bullet names one of
the claim's own anchors, so rebinding the claim on the exact declaration literal
at the cited location both records the curator's assertion and stops the machine's
rewrite from standing as this claim's provenance. Clearing needs no commit and no
stamp. Each range was verified against the code worktree first; 28 were supported
as projected and changed in anchor form only.

**Ambiguous provenance (19).** Anchors that resolved five to eight times (the
`nextAction`/`nextTool`/`nextArgs` triple, `SeriesCheckpointRefs`, the repeated
test-path literals in the `evidence-lifecycle.toml` consumer lists) were rebound
on unique literal anchors. Note the format constraint: a quoted anchor may not
contain a `|` in a table row, because an unescaped pipe is a cell divider and an
escaped `\|` stays escaped in the anchor text and never matches source.

**Stale ranges (9).** Citations left behind by a line shift (93-108 vs 92-106 and
similar) were re-cited to the construct's current extent.

## Real onboarding defects the read surfaced

1. **KNOWN COVERAGE GAP.** `mcp/src/agents_remember/models/terminal.py` declares
   `VALID_SPAWN_AGENT_SESSION_STATUSES` (line 86),
   `VALID_SESSION_RETIRE_STATUSES` (line 172) and `VALID_SESSION_RENAME_STATUSES`
   (line 198). The three produced-equals-declared cases that pinned them
   (`test_every_spawn_status_the_tool_can_return_validates` and its retire/rename
   siblings) were deleted by `d3610903` — the same commit these cards are stamped
   at — and **no test in the repository now references any of the three sets.**
   The affected card was re-worded to state this rather than to keep citing a
   deleted class; the loss is recorded here because a re-worded citation is not a
   durable enough home for an invariant loss.
2. `providers/degradation.py.md` attributed an "unreproducible percentages"
   disclaimer to the durability suite's docstring. That disclaimer no longer
   exists anywhere in the repository; the claim now states the zero-loss
   assertions the cited range actually establishes.
3. `kernel/sidecar_pairing.py.md` is the textbook declaration-elsewhere case: a
   claim about the `meaningful_body` extractor *applied here* was cited to the
   extractor's definition in `onboarding_doc.py`. Re-cited to the call site at
   `sidecar_pairing.py:147`.
4. `serving/terminal_liveness.py.md` enumerated cases spanning the whole
   `TerminalCatalogLivenessTests` class while the projected range stopped at 345;
   extended to the class's full 127-570.

## Coherence authority

Sixty-four candidates (6 entity-rows, 49 file-sidecars, 9 route-overviews) were
disposed: 24 `reconciled` for the cards whose content was updated to the leaf's
landed code or whose claim wording this pass corrected, and 40
`no-content-impact` for the cards whose only change is citation form or range.
Every judgment carries the card itself as its `memory:` evidence reference, so the
authority revalidates against the exact bytes it judged.

## Scope and stamps

All 62 claim/citation edits and the 57 accompanying curation records are inside
`onboarding/`. No `lastVerifiedCommitHash` or `lastVerifiedCommitDate` was
advanced in any document; verification stamps remain closeout-owned. This report
is the only artifact outside `onboarding/`.
