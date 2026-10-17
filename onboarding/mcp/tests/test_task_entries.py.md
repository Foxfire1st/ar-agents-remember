# mcp/tests/test_task_entries.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin the single TaskEntry owner of document stage, host activity, reciprocal membership and counts.

## Code Commentary

Document status maps to planned/started/completed/aborted; only started tasks expose activity. Known host in-turn or permission contributors win as works regardless of agent order; otherwise known idle/ended/no-agent activity is paused and unproved host state is unknown. eventAt comes from a contributing event; missing time stays absent and a future timestamp is retained for the browser to age/clamp. Serialized TaskState has no ageSeconds field. Declared missing children get one placeholder entry and shared counts; authored children replace rather than duplicate them, with scope retained and summary free of duplicated identity/status/progress fields. Addressless rows get opaque identities. Reciprocal declared links, deterministic conflict/cycle handling, root reachability and per-parent/workspace counts use the same entries, never folder containment alone. These are controlled source/fixture assertions.

The suite separately exercises genuinely absent-master fallback, present unresolvable master literals, records bound to another master, duplicate list rows and unlisted records using documented subTask inputs. Those cases are not proof of a non-subTask rejection guard, which neither BASE nor current placement implements. It checks that the forest remains deterministic and single-placement while disagreements are reported once by their complete producer identity. The reciprocal-ownership cases still constrain conflicting explicit bindings; they no longer imply that an absent master may never be adopted.

## Evidence


- Master validation in placement applies only to documented subTasks; other listed kinds retain list placement under existing identity/cycle guards, not a kind-rejection or own-master-validation rule. [8]


- Parameterized fallback/disagreement cases distinguish missing, explicit and unresolvable masters, retain raw literals and suppress duplicate reports. [7]

- Document stage overrides host activity except for started tasks. [1]

- Activity precedence and contributor event time are order-independent; missing times stay absent and future timestamps remain served. [2]
- A missing declared child has one entry, later authored in place, with shared count semantics. [3]
- Only reciprocal declared membership sets parent; all entries remain reachable once. [4]
- A fileless plan has one opaque child identity without invented document/body. [5]
- Two-parent/cycle/missing-parent conflicts remain deterministic, reciprocal and reachable with consistent counts. [6]
