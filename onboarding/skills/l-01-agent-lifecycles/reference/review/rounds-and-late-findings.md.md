# skills/l-01-agent-lifecycles/reference/review/rounds-and-late-findings.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Tier-2 review detail governing round-limit verification, unchanged-candidate record rechecks, sanctioned post-seal findings, protocol refusals and forged states, omission, whole-set, and memory-change (`OM-6`) checks, and review stops.

## Code Commentary

Covers six sections: verifying repaired findings at or beyond the settings round limit (approval required beyond the limit; advisory extra rounds granted by Architect); checking a repaired Worker record on the last recorded round without `begin_review` only while the candidate is byte-identical (otherwise `review-candidate-invalid` or `review-kind-invalid`); the three sanctioned post-seal routes (Curator code finding, Architect-forwarded advisory finding, failed final check) recorded via `addedFindings` without spending a round; protocol refusals routed via the developer-question route, malformed attempt rejection, stale candidate/version rejection, and forged-state non-guard policy; omission-repair full-diff listing, whole-set scan scripting, proportional review (assuming honest agents where a finding names the operation or honest step reaching its starting state, and requiring a requirement or developer request for harder adversarial review), and memory-review inspection of `cutCards`, `addedFiles`, pre-base-stale dependent confirmations, and `deferral_lifted` rows per `OM-6` (requiring signed checks and base plus candidate `knowledge_read(view="dependent", staleOnly=true)` receipts); and review stops, unfinished-turn notices, and step marking.

## Relationships

Target of all four Family-2 `refusal_references.py` pointers (`#verify-repaired-findings-at-the-round-limit`, `#recheck-a-repaired-worker-record`, `#post-seal-routes`). Absorbs retired `review-memory-changes.md`, `review-omission-repairs.md`, and `review-whole-set-findings.md` (verified by `test_l84_unique_detail_pointers_rules.py`). Registered in `composition-manifest.json` (`step_detail: true`), mirrored under `package_data/runtime/skills/`, and links `../curator/exceptions-and-recovery.md` and `../../criteria/onboarding-memory.md`.

## Evidence

- Round-limit verification, unchanged-candidate record rechecks, and the three sanctioned `addedFindings` post-seal routes define exact `task_doc` admission and refusal boundaries. [1]


- Protocol refusals, forged-state boundaries, proportional review (honest-agent starting-state and adversarial-review gate), omission/whole-set verification, `OM-6` memory-review checks (`cutCards`, `addedFiles`, `deferral_lifted`), and stop rules govern review conduct. [2]
