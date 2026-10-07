# mcp/src/agents_remember/models/knowledge/review.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The wire vocabulary of the Intent Reviewer: the request, the three panes (knowledge, source, evidence), the
payload around them, the entry list, and the typed refusal every review route answers with. The module
defines no record kind. Each value renders records another owner stores, or states that there is none.
The models carry their own consistency rules as validators, so an inconsistent display cannot be
constructed.

## Code Commentary

### Constants and closed vocabularies

- `KNOWLEDGE_REVIEW_SURFACE_VERSION` is `knowledge-review-surface/1`. `REVIEW_PANE_NAMES` is
  `("knowledge", "source", "evidence")`. `PROPOSED_ASSESSMENT_DISPOSITIONS` is `concern_found`,
  `no_concern_found`, `unresolved`.
- `ReviewRefusalCode` is the closed set of refusal codes: `candidate_unresolved`, `candidate_not_live`,
  `candidate_dataset_absent`, `subject_unresolved`, `comparison_refused`, `comparison_page_reset`,
  `comparison_page_unreadable`, `source_content_unresolved`, `review_adapter_unavailable`, `reviewer_busy`
  and `inputs_changing`. The last two are answered only by the leaf-wide tree view: `reviewer_busy` when
  its worklist computation could not start, because the bound on computations was reached or the
  request's deadline passed while it waited for a child, and `inputs_changing` when an input the view
  read moved again while the view was computed a second time.
- `ReviewPagedCollection` names the three collections a cursor can address: `knowledge`, `records` and
  `family_members`. `MAXIMUM_REVIEW_PAGE_SIZE` is the view owner's `MAX_VIEW_ROWS`.
  `REVIEW_PAGE_RESET_NEXT_ACTION` is the action text of a `comparison_page_reset`.
- `ReviewSubjectKind` is `invariant` or `family`. `ReviewSubjectPresence` is `before_only`, `after_only` or
  `both`. `ReviewSideState` is `present`, `absent`, `binary` or `unresolved`. `ReviewHistoryRef` has the
  one value `recorded`. `ReviewFileStatus` and `ReviewFileContent` name a changed file's status and
  renderability, each with an `unknown` member. `ReviewRemainingCountName` names the six counts of the
  source pane.

### Request, identity and refusal

- `ReviewSurfaceRequest` names the task context (`repository_id`, `master`, `leaf_id`), an optional
  selector, the page being asked for, an optional history reference and a previous binding digest. A
  continuation without the collection it continues is refused.
- `ReviewCandidateRef` carries task identities only and no file-system path.
- `ComparisonIdentity` carries the comparison's reference, policy version, binding digest, selector and
  snapshot digests and the two code tree IDs. With `knowledge_compared` the selector digest and both
  snapshot digests must be present; without it all three must be absent.
- `ReviewRefusal` is one typed refusal: `code`, `detail`, `next_action`, and optionally
  `offending_input`, `expected` and `observed`.
- `ReviewCollectionPage` states one page. Returned plus remaining must equal the total; a cursor is
  present exactly when rows remain; a `reset` page carries its refusal; a `continued` page names the
  cursor it continued.

### The panes

- `ReviewSideContent` carries text exactly when its state is `present`.
- `ReviewKnowledgePane` holds identities, both statements and conditions, revision groups, field changes,
  authored effects, signals, assessments, context and applicability. Its single `assessment` must be one
  of its `assessments`. `selection_detail` is present exactly for the `task_context` state, and a
  recorded revision selection requires `subject_selected`. Authored effects (`ReviewAuthoredEffect`) and
  mechanical signals (`ReviewSignal`) are separate types; a signal has no author, severity or verdict
  field.
- `ReviewAssessmentDisplay` must carry a non-blank author and at least one examined input.
- `ReviewSourcePane` holds the inventory, the selected locations, the relationship movements, the
  remaining counts, the expansion reference and command, and the three lists of attributed, confirmed
  unattributed and undetermined changed paths. `ReviewRemainingCount` has a value or a reason, never both
  and never neither.
- `ReviewSourceInventory` is `measured` or `unavailable`. `listed_total` must equal the number of entries;
  an unavailable inventory lists nothing and is not partial; unrepresentable paths require a measured,
  partial inventory. `ReviewChangedFile` carries a `detail` exactly when its content is `unknown`.
- `ReviewEvidencePane` holds evidence links, observations, assessments and the record channels.
  `evidence_state` must be `recorded` exactly when links or observations exist, and `assessment_state`
  must be `assessed` exactly when assessments exist.

### Payload and results

- `KnowledgeReviewPayload` joins the candidate, the optional comparison identity, the three panes, the
  family context, staleness, submission, movements, the page or its refusal, and the limitations.
  Submission is `disabled_stale` exactly when staleness is `stale`; published dispositions must be among
  the three proposed ones; a page and a page refusal never appear together; the comparison identity is
  absent exactly when staleness is `not_compared`; and the identity's `knowledge_compared` must agree with
  the knowledge pane's `subject_selected` state.
- `KnowledgeReviewResult` is a `review` with a payload or `refused` with a refusal.
- `ReviewEntryListResult` is `entries` or `refused`. A refused read carries its refusal, no entries and
  zero totals. `total_subjects` must equal `invariant_total` plus `family_total` and be at least the
  number of entries returned.

## Evidence

- The module docstring: no record kind, and the five prohibitions of the display. [35]
- The closed set of refusal codes, with the two codes of the leaf-wide tree view. [36]
- The three proposed dispositions. [37]
- The three paged collections. [38]
- A side carries text exactly when present. [39]
- The request and its cursor rule. [40]
- The comparison identity and its all-or-nothing knowledge half. [41]
- The typed refusal. [42]
- One page and its four consistency rules. [43]
- An assessment travels with its author and examined inputs. [44]
- A count is a value or a reason. [45]
- The knowledge pane and its three rules. [46]
- The inventory and its count rules. [47]
- The source pane. [48]
- The evidence pane's states match its collections. [49]
- The payload and its three rules. [50]
- The review result is a payload or a refusal. [51]
- The entry list and its totals. [52]
- The leaf-wide view answers reviewer_busy with its own action text. [53]
- The leaf-wide view answers inputs_changing after a second moved input. [54]
