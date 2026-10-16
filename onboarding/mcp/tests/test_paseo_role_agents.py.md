# Role-agent fact publication tests

[Governing tests overview](overview.md)

## Contract

Filesystem tests exercise publisher facts for the event-driven plugin: round-trip role/task/report records, no rewrite of an identical plain record without a host publication, merging other agents, and filtering incomplete or missing inputs. Registration under a host publication is an event boundary even when identity facts are unchanged; it supersedes the old ended occurrence rather than following the plain-record no-op rule. Start-hook fixtures exercise successful publication and omission when runtime/report facts are absent. These are isolated publisher/start-hook assertions, not evidence of live turn-end registration, permission events or native parent delivery.

At two ended-history sizes, complete host publications reclaim only explicitly ended roles, retain idle/in-turn parent/child facts, and keep output bounded. Re-registering an ended ID protects it from stale end events and unrelated/concurrent publications; a newer end or a new host boot can reclaim it. Concurrent registrations preserve every agent fact. Start-hook ownership moves to cli.role_activity; the missing-runtime/report and repeat-without-publication predicates remain.

## Evidence

- Only authoritative ended occurrences reclaim registration; revival supersedes older ends at both fixture sizes. [3]
- Concurrent registrations retain every published agent fact. [4]


- Round-trip and unchanged republish preserve fact data and file mtime. [1]
- Start hooks publish only when required runtime/report facts exist. [2]
