# mcp/tests/test_closeout_kept_rules_pins.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_kept_rules_pins.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2` |
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The enabled plan and message checks cover code and memory only. | L61-L69; L72-L94; L97-L111; L114-L138 | [mcp/tests/test_closeout_kept_rules_pins.py](mcp/tests/test_closeout_kept_rules_pins.py) |
| Both content messages are required without a ledger leg. | L141-L167 | [mcp/tests/test_closeout_kept_rules_pins.py](mcp/tests/test_closeout_kept_rules_pins.py) |
| Real ancestry covers base, checkpoint head, and unrelated movement. | L203-L211; L214-L234; L237-L247 | [mcp/tests/test_closeout_kept_rules_pins.py](mcp/tests/test_closeout_kept_rules_pins.py) |
| Replay uses Git facts and the retired recovery API remains absent. | L250-L269; L272-L286 | [mcp/tests/test_closeout_kept_rules_pins.py](mcp/tests/test_closeout_kept_rules_pins.py) |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15T01:02 UTC — Replaced the code-memory-ledger trifecta with explicit intent for the two enabled content outputs; retained normalization, all-missing-message reporting, checkpoint/source ancestry, and replay assertions. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 2 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "def _integration_replay_requirements(contract: WorktreeContract) -> IntegrationSources:" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "contract.integration_status in {\"completed\", \"checkpointed\"} and integrated" repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_integration_replay_requirements` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:255-275. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T04:10+02:00 — Created by the 260831-LOCR-L30 follow-up curator pass. Documents the R1-R4
  rule pins, the two hermetic / two real-repository fixture split, and the new
  `test_r3_closeout_accepts_the_source_head_a_checkpoint_landed` case with its
  `test_r3_closeout_refuses_when_the_source_branch_moved` companion. Verification metadata is pinned
  to the leaf base commit and remains closeout-owned.
