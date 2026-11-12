# mcp/tests/test_task_entries.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin the single TaskEntry owner of document stage, host activity, reciprocal membership and counts.

## Code Commentary

Document status maps to planned/started/completed/aborted; only started tasks expose activity. Known host in-turn or permission contributors win as works regardless of agent order; otherwise known idle/ended/no-agent activity is paused, unless a seat's declared wait still has its check to come, and unproved host state is unknown. eventAt comes from a contributing event; missing time stays absent and a future timestamp is retained for the browser to age/clamp. Serialized TaskState has no ageSeconds field. Declared missing children get one placeholder entry and shared counts; authored children replace rather than duplicate them, with scope retained and summary free of duplicated identity/status/progress fields. Addressless rows get opaque identities. Reciprocal declared links, deterministic conflict/cycle handling, root reachability and per-parent/workspace counts use the same entries, never folder containment alone. The declared-wait cases (:498-549) pin that a started task none of whose agents works, but one of whose idle seats carries a declared wait with its check still to come, is `waiting` with `eventAt` at the wait's `since`, its `waitingSeats` naming the seat and no provider limit; that a wait past its check, a wait with no check armed and a wait on an ended seat leave the task paused, that a check only just past due (inside the 60-second grace) still shows waiting, and that a working agent wins and serves no `waitingSeats`; that `task_counts` counts a waiting task as waiting alone; and that the published wait is validated, refusing a naive `since`, an empty or unknown `waitsFor`, any other key and a `detail` over 300 characters. These are controlled source/fixture assertions.

The suite separately exercises genuinely absent-master fallback, present unresolvable master literals, records bound to another master, duplicate list rows and unlisted records using documented subTask inputs. Those cases are not proof of a non-subTask rejection guard, which placement does not implement. It checks that the forest remains deterministic and single-placement while disagreements are reported once by their complete producer identity. The reciprocal-ownership cases constrain conflicting explicit bindings; they do not imply that an absent master may never be adopted.

## Evidence



- Master validation in placement applies only to documented subTasks; other listed kinds retain list placement under existing identity/cycle guards, not a kind-rejection or own-master-validation rule. [8]



- Parameterized fallback/disagreement cases distinguish missing, explicit and unresolvable masters, retain raw literals and suppress duplicate reports. [7]

- Document stage overrides host activity except for started tasks. [1]

- Activity precedence and contributor event time are order-independent; missing times stay absent and future timestamps remain served. [2]

- A missing declared child has one entry, later authored in place, with shared count semantics. [3]


- Only reciprocal declared membership sets parent; all entries remain reachable once. [4]


- A fileless plan has one opaque child identity without invented document/body. [5]


- Two-parent/cycle/missing-parent conflicts remain deterministic, reciprocal and reachable with consistent counts. [6]
