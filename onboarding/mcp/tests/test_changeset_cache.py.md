# mcp/tests/test_changeset_cache.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin byte-identical native change-set HTTP reads, conditional reuse and fresh invalidation without mutating the Git index.

## Code Commentary

The real Git/contract fixture serves task, file-diff and master routes. Unchanged reads and ETag 304s count zero Git children; native-input mutations, same-size/restored-mtime edits, object corruption/removal/restoration, attributes and ignore/config sources invalidate retained proofs. Sidecar presence stays live around retained Git lists. Unreadable or racing input generations compute uncached. Result, repository/object, and in-flight observation retention is bounded; unrelated sibling commits and ignored trees do not become relevant inputs. These are fixture-scoped counts and byte comparisons, not installed throughput or universal filesystem freshness.


## Current Behavior

the module now pins the L174 rules. A working view is computed natively on every read with no cache and no freshness-only reuse (`test_a_working_view_has_no_cache_and_no_freshness_check`); a same-letter content edit is seen (`test_working_content_edit_with_the_same_status_letter_is_seen`); an id-keyed hit takes no observation and starts no Git (`test_commit_range_reuse_observes_nothing_and_starts_no_git`, `test_a_commit_pair_hit_survives_object_loss_and_starts_no_git`, `test_an_id_keyed_hit_does_not_observe_changed_object_bytes`, `test_lost_recorded_commit_is_not_observed_on_a_hit_and_a_cold_refusal_recovers`); the request object memo is bounded (`test_the_request_object_memo_is_bounded`); an unreadable status admits no successful result (`test_a_failed_status_makes_no_successful_result_reusable`); one read does not wait on another (`test_one_read_does_not_wait_on_another_cache_read`). The `_reading_children` helper filters the status/census freshness children from the `no change-set Git` assertions. This supersedes 'Unchanged reads and ETag 304s count zero Git children' as an unqualified claim: an unchanged working read now runs one status child, and the test states that distinction.

## Evidence


- Task/file/master routes retain exact native bytes and conditional responses without repeat Git children. [1]


- Working reads detect restored-mtime edits and leave native index bytes and identity unchanged. [2]


- Rename/delete/replace/add/index/HEAD/symlink mutations force fresh native equality. [3]


- Missing commits preserve refusal and later restoration becomes visible. [4]


- Sidecar appearance/disappearance updates live without rerunning Git. [5]

- Unstable or unavailable observations are not retained. [6]
- Growing result histories retain the configured bound and evict least-recent results. [7]
- One long read also bounds pending values and input observations. [8]

- Worktree/info/XDG attributes affect committed native results. [9]


- Unrelated sibling activity and packed-ref removal preserve relevant cached results. [10]
