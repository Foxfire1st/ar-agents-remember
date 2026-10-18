# mcp/tests/test_intent_summary_cache.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin exact native intent-summary HTTP reuse, typed refusal freshness and bounded dependency observation.

## Code Commentary

Real Git/converted-memory fixtures call the composed summary route and compare responses to the native reader. Unchanged conditional reads skip Git and recomputation; code, memory, index, HEAD and comparison-record changes invalidate. Missing/restored objects keep the native unavailable/count semantics, including restoration racing a refusal read. Derived index timestamp-only touches reuse while changed bytes reopen. Unreadable observations stay uncached; dependency/result histories are bounded and unrelated master notes are not walked. A deliberately slow summary port cannot serialize task/file/master reads. These are in-process fixture assertions, not a live aggregate latency benchmark.


## Current Behavior

the suite now filters the freshness-only Git children (`_reads`: the status and `count-objects` children are not summary computation) and exercises the unknown-status refusal path: a refused summary may be served again from its retained proof while a counted summary may not. The existing counted/unavailable, derived-index, object-loss and blocked-port cases remain. This supersedes the unqualified 'zero Git' phrasing in the earlier account: a working view's status child and the object census are freshness checks, not a summary recomputation.

## Evidence

- Exact native counted bytes and ETag 304 reuse do not recount or spawn repeat Git. [1]
- Native code/memory/index/HEAD/record inputs invalidate and then settle. [2]
- Derived-index timestamp and content changes are distinguished. [3]
- Unobservable index inputs fall back to native reads every time. [4]
- Dependency manifests and retained values share a finite bound. [5]
- Unchanged refusals revalidate without Git and restored objects regain counted native answers. [6]
- A restoration during refusal composition cannot bind that refusal to new inputs. [7]
- A blocked summary fixture does not block task/file/master HTTP reads. [8]