# Role-agent fact publication tests

[Governing tests overview](overview.md)

## Contract

Filesystem tests exercise publisher facts for the event-driven plugin: round-trip role/task/report records, no rewrite of an identical record, merging other agents, and filtering incomplete or missing inputs. Start-hook fixtures exercise successful publication and omission when runtime/report facts are absent. These are isolated publisher/start-hook assertions, not evidence of live turn-end registration, permission events or native parent delivery.

## Evidence

- Round-trip and unchanged republish preserve fact data and file mtime. [1]
- Start hooks publish only when required runtime/report facts exist. [2]
