# mcp/src/agents_remember/application/tool_answer_log.py

## Governing Overview

[overview](overview.md)

## Purpose

The daily tool-call log (MIK-R108 rule 3): one line per admitted call plus the whole result beside it, enclosure logs versus coordination-root logs, byte budgets with oldest-first whole-day eviction, and credential redaction. Writes that cannot be admitted — budget conflict, oversize detail, unwritable location — are dropped and counted, never failing the call. The server boundary calls in; this module owns the record.

## Code Commentary

### Logic

- Destinations: `resolve_log_roots` routes enclosure-bound role calls to `<enclosure>/logs/` and every other call (controllers, chat, CLI, pre-enclosure agents) to the resolved transcript root; terminating operations (cleanup, abandon, finalize) always route to the root and never recreate a removed enclosure folder. `ensure_enclosure_logs_dir` makes the enclosure folder at enclosure creation.
- Lines and details: `append_call_line` appends one whole UTC-day JSONL line (time, tool, caller, outcome, duration, answer tokens, bytes, guard-cut flag, detail name, arguments with long values shortened) with an exclusion-guarded byte append that counts short writes on the next persisted line; `record_tool_call` files the whole result as an indented detail JSON beside the log. A failed write never fails the call: the answer carries `logError` instead.
- Budgets: `prune_old_tool_logs` / `_evict_older_days` keep each folder within its byte budget (256 MiB transcript root, 64 MiB per enclosure when absent — both configurable — 8 MiB per detail, fixed) against one coherent folder census with 60-second listings. Age sweeping removes whole oldest days first, at most 31 per call with continuation at the next call; pressure eviction separately removes whole oldest prior days until the write fits, and drops counted writes when only the current day is left; only confirmed reclaimed bytes leave the census. `prepare_log_folder` carries successful sweep continuation across same-day calls. Enclosure logs have no age pruning: the budget is the only pre-cleanup removal, with no marker.
- Redaction: `_redact_value` drops credential-naming keys at any depth and scrubs values of credential-naming environment variables (KEY, TOKEN, SECRET, PASSWORD, PASSWD, CREDENTIAL, AUTH, COOKIE, any case) wherever they occur from six characters on; every other environment value, including home-folder paths, is ordinary text and stays whole.
- `tool_call_context` brackets one production call with its arguments, start time and config for the answer boundary; raised calls are logged at the dispatch site and re-raised.
- `write_diff_report` retains a caller's complete document diff as a separate `.diff.md` file beside the day's details. Its own 1 MiB cap or an unwritable destination returns `None`, so the response can distinguish an available report from a lost detail. Whole-day eviction can remove this report with the day; its existence is not a promise of permanent custody or a successful detail write.

### Invariants And Boundaries

- The system comes before the record: on any conflict the record is dropped, and a dropped write never fails the call.
- An enclosure's log goes with the enclosure: cleanup and abandon remove it whole, with nothing archived, copied or left as a marker, and never a reason to wait or refuse.
- Several servers may write one folder; the stated census/listing margin is the admitted overshoot bound.

## Evidence

- Admitted calls append one whole day line and file their whole result beside it; writes that cannot be admitted are dropped and counted. [1]

- A live ambient enclosure contract selects the enclosure log folder; terminating calls always select the resolved transcript root. [2]
- Over-budget folders evict whole oldest days against one coherent census. [3]
- Credential keys and credential-variable values are omitted; ordinary values stay whole. [4]

- A caller diff has its own bounded readable report, or no report when oversize or unwritable; it is independent of detail retention. [5]
