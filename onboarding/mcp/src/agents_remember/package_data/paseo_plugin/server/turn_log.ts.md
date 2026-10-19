# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_log.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

The plugin's own turn-end files: the log its decisions are written to, the single archive it keeps, and the file a failed write is named in.

## Code Commentary

`createTurnEndLog` builds a write-only sink from `PASEO_HOME` under `agents-remember/`: each row — time with offset, agent, role, task, kind, count and reason — is one JSON object on one line of `turn-ends.jsonl`. Before a row is appended the file's size is checked, and once the next row would take it past 2 MiB the file is renamed over `turn-ends.1.jsonl`, so exactly one archive is kept and a new file begins. A write that fails is named once in `turn-ends.error.json` with its time and error, and the rule goes on without it; `host-activity.json` is never touched, its readers forbid extra keys. Without a `PASEO_HOME` the sink is a no-op and the decision still runs. The turnover size and the clock are injectable so a test need not write 2 MiB.

## Boundaries

This is the plugin's own diagnostic file, not product state: no reader in the product parses it, it records decisions and writes rather than confirmed host delivery, and it holds no line that is still owed to a parent.

## Evidence

- The plugin keeps its own bounded, rotating log and separate failure file, leaving `host-activity.json` untouched. [1]
