# dashboard/src/panels/review/hunkMarkers.classifier.captured.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retained test input for the review consumers, recording its own response identities, states and bounded populations.

## Code Commentary

This file is fixture data, not current project knowledge or a new selection authority. Its literal response states and counts belong to the recorded input. Reading it does not execute its producer, validate an installed dashboard, reproduce the capture or grade the present candidate. A provenance field is a recorded custody statement, not an independent observation made by this card.

### Current input shape

- Root keys: `["after_unread", "before_unread", "both_unread", "curated", "partial", "precuration"]`
- Root collection sizes (physical JSON containers, not gate verdicts): `{"after_unread": {"kind": "dict", "count": 1}, "before_unread": {"kind": "dict", "count": 2}, "both_unread": {"kind": "dict", "count": 1}, "curated": {"kind": "dict", "count": 2}, "partial": {"kind": "dict", "count": 1}, "precuration": {"kind": "dict", "count": 5}}`
- Structured state blocks (a state beside payload, operation, comparison, cards, worklist, entries or items): 12; the bounded inventory below shows 6. This is a structural inventory, not a producer count. Other values remain available through the whole-file citation.

#### Recorded state block 1

```json
{
  "jsonPath": "$[\"after_unread\"][\"pkg/a.py\"]",
  "state": "trees",
  "comparison": {
    "leaf_id": "260101-TRV-L1",
    "number": 1,
    "code_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "08ff0d2d89d770ea9eab5ee0bd98955d05e8cf72"
    },
    "code_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "c8af799c585a685b1abd5eb795047f422600c693"
    },
    "memory_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "50846ab6b0d1d7c758736f9e10dcb9c404c535e1"
    },
    "memory_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "0000000000000000000000000000000000000000"
    }
  },
  "entries.count": 0
}
```

#### Recorded state block 2

```json
{
  "jsonPath": "$[\"before_unread\"][\"pkg/a.py\"]",
  "state": "trees",
  "comparison": {
    "leaf_id": "260101-TRV-L1",
    "number": 1,
    "code_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "08ff0d2d89d770ea9eab5ee0bd98955d05e8cf72"
    },
    "code_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "c8af799c585a685b1abd5eb795047f422600c693"
    },
    "memory_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "0000000000000000000000000000000000000000"
    },
    "memory_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "1ece4e9293ce7838dfe6e20481aa20377f3122a5"
    }
  },
  "entries.count": 0
}
```

#### Recorded state block 3

```json
{
  "jsonPath": "$[\"before_unread\"][\"pkg/lines.txt\"]",
  "state": "trees",
  "comparison": {
    "leaf_id": "260101-TRV-L1",
    "number": 1,
    "code_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "08ff0d2d89d770ea9eab5ee0bd98955d05e8cf72"
    },
    "code_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "c8af799c585a685b1abd5eb795047f422600c693"
    },
    "memory_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "0000000000000000000000000000000000000000"
    },
    "memory_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "1ece4e9293ce7838dfe6e20481aa20377f3122a5"
    }
  },
  "entries.count": 0
}
```

#### Recorded state block 4

```json
{
  "jsonPath": "$[\"both_unread\"][\"pkg/a.py\"]",
  "state": "trees",
  "comparison": {
    "leaf_id": "260101-TRV-L1",
    "number": 1,
    "code_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "08ff0d2d89d770ea9eab5ee0bd98955d05e8cf72"
    },
    "code_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "c8af799c585a685b1abd5eb795047f422600c693"
    },
    "memory_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "0000000000000000000000000000000000000000"
    },
    "memory_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "0000000000000000000000000000000000000000"
    }
  },
  "entries.count": 0
}
```

#### Recorded state block 5

```json
{
  "jsonPath": "$[\"curated\"][\"pkg/a.py\"]",
  "state": "trees",
  "comparison": {
    "leaf_id": "260101-TRV-L1",
    "number": 1,
    "code_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "08ff0d2d89d770ea9eab5ee0bd98955d05e8cf72"
    },
    "code_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "c8af799c585a685b1abd5eb795047f422600c693"
    },
    "memory_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "3d9c200493d4cc4c326cf4fbe587ba61a182a2d5"
    },
    "memory_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "1ece4e9293ce7838dfe6e20481aa20377f3122a5"
    }
  },
  "entries.count": 0
}
```

#### Recorded state block 6

```json
{
  "jsonPath": "$[\"curated\"][\"pkg/lines.txt\"]",
  "state": "trees",
  "comparison": {
    "leaf_id": "260101-TRV-L1",
    "number": 1,
    "code_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "08ff0d2d89d770ea9eab5ee0bd98955d05e8cf72"
    },
    "code_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/code",
      "tree": "c8af799c585a685b1abd5eb795047f422600c693"
    },
    "memory_base": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "3d9c200493d4cc4c326cf4fbe587ba61a182a2d5"
    },
    "memory_candidate": {
      "repository": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/capture-helper/classifier-01/tmp/tmp4lj04mvw/memory",
      "tree": "1ece4e9293ce7838dfe6e20481aa20377f3122a5"
    }
  },
  "entries.count": 0
}
```

### Reading boundary

Missing fields are not converted into zero counts. Present state, measured population, carried page and continuation-field presence remain separate observations; an opaque cursor is not decoded or called admitted here. Synthetic overlays in consuming tests require their own disclosure and do not turn this recorded body into fresh native or browser acceptance. Regeneration belongs to the source/capture owner; old fixture descriptions below are not instructions to fabricate successful response bytes.

## Previous Input Account — Historical Only

The following account describes the preceding fixture bytes, receipts and consuming-test scope. Its present-tense clauses, measurements and numeric reference labels are historical, not current guarantees or live citations. The actual current input shape is recorded above; general design context is retained here rather than discarded.

> # dashboard/src/panels/review/hunkMarkers.classifier.captured.json
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> **Eleven real per-file classifications of MIK-L32's lane fixture world in six scenarios** (55,216 bytes; test evidence
> for `hunkMarkers.test.ts` and `IntentMarkers.test.tsx`). Each body is `{ file_classification, texts }`: the served
> response and, fixture-only, the exact side blob texts.
>
> ## Code Commentary
>
> ### Logic
>
> - `precuration`: `lines.txt` (a replace linked to INV-BBBBBB with no family, a replace of attribution unknown on the
>   after side, an unexplained deletion), `a.py` (a replace linked to INV-AAAAAA through the before side with its three
>   occurrences, and an insertion of attribution unknown), `tests/test_a.py` (a proof link), `new.py` (bucket
>   `unexplained`: the file-level mark) and `stale.py` (attribution unknown on both sides).
> - `curated`: the same files after the scratch-authored realizations, `lines.txt` L2 linked to INV-AAAAAA (member,
>   removed or reassigned in after, before-only) and INV-BBBBBB (confirmed no family), `a.py`'s insertion linked to
>   INV-CCCCCC (confirmed no family).
> - `before_unread` and `after_unread`: one memory side unavailable, so the readable side's links stay and the unread
>   side's lines are unknown, or every family occurrence is `membership_unknown`; `both_unread`: bucket
>   `attribution_unknown`, the file-level note; `partial`: an index read in part, INV-BBBBBB `membership_unknown`.
>
> ### Conventions
>
> Keep the captured bytes and their receipt intact; a recapture rewrites both.
>
> ### Invariants And Boundaries
>
> The bodies describe MIK-L32's test fixture world, not current project knowledge.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> - The first scenario's body: a linked hunk whose occurrences are all `membership_unknown` because the after side is unread. (historical reference 1)
> - The unread-before scenario (the review R1 F1 excerpt case) and the file with no readable side. (historical reference 2)
> - The curated and partial scenarios. (historical reference 3)
> - The pre-curation scenario, with the proof and the unregistered file. (historical reference 4)
> - The receipt row for this body. (historical reference 5)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.

## Evidence

### Repo-Internal References

- The current retained JSON input supplies the literal identities, response states and populations summarized above; these are fixture facts, not live project knowledge or fresh execution evidence. [6]
