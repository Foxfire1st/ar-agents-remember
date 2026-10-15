# mcp/src/agents_remember/application/knowledge_gate/predicates.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

Dispatch every worklist kind to its own satisfying predicate over parsed leaf history, candidate knowledge and actual code currentness. Missing predicates and unreadable observations are not generic-row passes. A Git read failure or timeout raises `GitReadFailed` and makes the whole gate run `incomplete`; a persistently unavailable object or unsupported grammar is instead an ordinary not-current observation that leaves its item open.

## Code Commentary

Invariant rows must cover the required touched/moved/stale entries and every declared addition, retirement or reanchor; their recorded revision must match the candidate invariant, and surviving covered entries must be current at C. A leaf-owned record change retains its governing changed/deleted disposition while it differs from the parent line. That governing-disposition check precedes missing-cover and revision diagnostics; when it fails, the reason also lists any missing covers. Family rows separately check own-revision drift, hidden guarantee changes, the exact examined member union, member revisions and uncovered invariant obligations. These predicates are structural/currentness admission, not an independent review of whether reasons or effects are true.

Ordinary onboarding admission now consumes a typed `OnboardingTraceRow`, the winning row's own history-file closed flag, exact `sourceBlobs`, and counted-change facts. A current `updated` row needs a counted change; `no_impact` needs the current source binding; sourceless rows answer only from their closed historical file. Counted Markdown alone is not a new ordinary answer. Missing blobs, changed sources, sourceless open rows and unsupported update claims each have their own named repair reason. [1]

Unexplained covered changes keep the existing `no_invariant` requirement. An uncovered change instead consumes its own onboarding-trace facts and applies the same typed onboarding/currentness rule; mere presence in a subject-to-ID map is insufficient. [2]

The new `unassigned_invariant` predicate requires a typed membership row and compares its recorded revision with the subject invariant in K_C. `touched_record` requires a typed record row at the item's revision, with disposition derived from record facts: newly retired wins, otherwise an increased revision needs `changed`, otherwise `no_impact`. These are distinct row classes, not substitutions for invariant/family changes or an authorization to write through an unsupported producer. [3]

The following retained registration summary is historical: its reconsideration wording must be read
with the current candidate/code-aware dispatch and link-target predicate described below, not as an
assertion that the old row-only reconsideration adapter remains in use.

Registration covers the membership and touched-record kinds as well as the prior invariant, family, route, onboarding, unexplained, planned and reconsideration kinds. Family-route conditions remain addressed by subject, and planned/reconsideration kinds retain their registered rules. [3]

The earlier amended R53 rollout exception was task-scoped, not a general relaxation of these
candidate-code predicates. Its former deferred-work statement is not a current implementation
contract: family admission here continues to check own revision, guarantee disposition, examined
members, member revisions and open invariant obligations.

### Governing changes, reconsideration and removed link targets

Invariant-row diagnosis first protects the changed/deleted row that governs a leaf-owned meaning change.
If that check fails, its restatement remedy is returned before an independent missing-cover or revision
mismatch, with missing cover IDs appended when present. Only after the governing row is valid does the
predicate separately reject missing covers, revision drift and non-current surviving entries.

`reconsideration_candidate` now calls `reconsideration_gate_reason` with the item, candidate knowledge,
opened code tree and the subject-to-row map. A `CodeReadError` from that call becomes `GitReadFailed`, so
the gate handles it as an incomplete read rather than an ordinary answered item. This call-site contract
does not make a row-map lookup alone sufficient.

`link_target` does not admit a history-row answer. It consults `holds_target` for the item facts' record
and target key in K_C: while the removed target's link remains, the remedy is to remove or restate that
link through the writer. Once K_C no longer holds that target, the predicate returns no open reason.


## Evidence

### Repo-Internal References

- Row-own closed provenance and source/count currency. [1]
- Covered versus uncovered unexplained admission. [2]
- Membership/record revision and disposition predicates with registrations. [3]

- Governing changed-row violations take diagnostic precedence and retain missing-cover details. [4]
- Reconsideration delegates with candidate knowledge and code, translating CodeReadError into GitReadFailed. [5]
- Link-target items are answered by absence of the target in candidate knowledge, never by a history row. [6]

### Docs References

The earlier amended rollout rule and deferred-work scope are historical external task context, not
evidence of current scheduling or completion. These statements do not claim fresh test execution
or independent MEMORY acceptance.
