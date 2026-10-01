# mcp/test_support/agents_remember_test_support/testing/causal_failures.py

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Implements pytest-side exact-node causal suppression, observed failure-family classification, and
durable non-accepting causal reports.

## Code Commentary

### Logic

Hooks load and structurally validate the owner-preflight report, classify retry semantics, and
index blocked status by exact pytest node id. Only a collected node that appears in a source-proved
dependency chain receives a skip marker. Other nodes in the same file still execute. Retry family
is derived from the actual observed exception chain—not imports present in the test file—and keeps
async, process, multiprocessing, subprocess, socket, timeout, and residual environment/OSError
owners distinct. The most-specific match wins, so a connection or timeout does not also become a
generic environment failure. Runtime evidence carries the actual serial/xdist process topology,
seed, worker, timing, and retry semantics. Unknown observed assertions stay independent. JSON and
Markdown render from the same bounded payload.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Blocked status requires a failed owner preflight plus a valid owner-to-exact-node chain;
  file membership is never sufficient.
- Independent and same-file sibling nodes remain observable, including process-sensitive failures.
- Each observed exception belongs to one most-specific runtime family; umbrella OSError matching
  cannot erase its socket, timeout, or child-process owner.
- Causal output is explanatory and non-accepting; an invalid causal artifact disables suppression
  and the quality owner runs the complete selected population.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Collection blocks only exact node ids present in the validated causal report and records serial/xdist topology for every collected item. [2]
- Runtime evidence separates observed blocked nodes from independent failures while retaining worker, seed, topology, and timing. [3]
- Observed exception chains map each exception to one most-specific async, multiprocessing, subprocess, process, socket, timeout, or environment family. [4]
- Validation refuses missing owners, unknown exact nodes, conflicting identity, invalid chains, and incomplete runtime evidence. [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [6]
