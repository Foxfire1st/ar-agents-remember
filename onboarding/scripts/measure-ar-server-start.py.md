# scripts/measure-ar-server-start.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Measures one AR server start on the host it runs on, from process spawn to the completed `tools/list` answer, and reports that wall-clock number against a 5.0 s bound taken at one-minute load of at most 40. It records the conditions that make the number readable instead of presenting a bare duration.

## Code Commentary

- It launches the command a seat launches — the running interpreter with `-m agents_remember.mcp --config <settings>` — inside a throwaway coordination world, with `AR_EXPLAINER_BINDING` present for explainer mode and absent otherwise, and calls no tool.
- The clock starts before the spawn; `initialize` and `tools/list` arrival are timed separately, so the reported figure is the spawn-to-discovery span that includes `initialize` and the server's own tool-call-free start-up path.
- The bound is judged against the fastest run of `--repeat`, so `best_tool_list_seconds` is a best case and not a mean, and the record says so by naming the field.
- A run whose starting one-minute load exceeds the stated 40 is reported as unrepresentative rather than dropped: `load_representative` goes false and the timing is still disclosed, which is why an out-of-starting-load number is not silently kept as representative. The recorded `load_after` does not enter the `load_representative` predicate.
- The environment block pins interpreter, platform, logical CPU count, dependency versions, source root, source head, dirty-file count and bytecode-cache condition; the claim is a bounded wall-clock witness on this host, not a promise at any load.

## Evidence

- The requirement's bound is stated as 5.0 s at a one-minute load of at most 40. [1]
- The measured span starts before the process is spawned and ends when the tool list arrives. [2]
- Each run records its own launch command, tool count and load before and after. [3]
- The reported bound is judged against the fastest of the repeated runs. [4]

- A starting load above the stated limit marks the aggregate unrepresentative; load_after remains disclosed without entering this predicate. [5]
