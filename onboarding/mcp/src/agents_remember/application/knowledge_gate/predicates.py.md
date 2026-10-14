# mcp/src/agents_remember/application/knowledge_gate/predicates.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

Dispatch every worklist kind to its own satisfying predicate over parsed leaf history, candidate knowledge and actual code currentness. Missing predicates and unreadable observations are not generic-row passes. A Git read failure or timeout raises `GitReadFailed` and makes the whole gate run `incomplete`; a persistently unavailable object or unsupported grammar is instead an ordinary not-current observation that leaves its item open.

## Code Commentary

Invariant rows must cover the required touched/moved/stale entries and every declared addition, retirement or reanchor; their recorded revision must match the candidate invariant, and surviving covered entries must be current at C. A leaf-owned record change retains its governing changed/deleted disposition while it differs from the parent line. Family rows separately check own-revision drift, hidden guarantee changes, the exact examined member union, member revisions and uncovered invariant obligations. These predicates are structural/currentness admission, not an independent review of whether reasons or effects are true.

Ordinary onboarding admission now consumes a typed `OnboardingTraceRow`, the winning row's own history-file closed flag, exact `sourceBlobs`, and counted-change facts. A current `updated` row needs a counted change; `no_impact` needs the current source binding; sourceless rows answer only from their closed historical file. Counted Markdown alone is not a new ordinary answer. Missing blobs, changed sources, sourceless open rows and unsupported update claims each have their own named repair reason. [1]

Unexplained covered changes keep the existing `no_invariant` requirement. An uncovered change instead consumes its own onboarding-trace facts and applies the same typed onboarding/currentness rule; mere presence in a subject-to-ID map is insufficient. [2]

The new `unassigned_invariant` predicate requires a typed membership row and compares its recorded revision with the subject invariant in K_C. `touched_record` requires a typed record row at the item's revision, with disposition derived from record facts: newly retired wins, otherwise an increased revision needs `changed`, otherwise `no_impact`. These are distinct row classes, not substitutions for invariant/family changes or an authorization to write through an unsupported producer. [3]

Registration covers the membership and touched-record kinds as well as the prior invariant, family, route, onboarding, unexplained, planned and reconsideration kinds. Family-route conditions remain addressed by subject, and planned/reconsideration kinds retain their registered rules. [3]

Amended R53 rule 1 is the bounded pre-landing changed-card exception for this leaf, not a general relaxation of these candidate-code predicates. The nine deferred Family-examination obligations remain L54 work.

## Evidence

### Repo-Internal References

- Row-own closed provenance and source/count currency. [1]
- Covered versus uncovered unexplained admission. [2]
- Membership/record revision and disposition predicates with registrations. [3]

### Docs References

The amended rollout rule and deferred L54 scope are external task authorities; these statements do not claim fresh test execution or independent MEMORY acceptance.
