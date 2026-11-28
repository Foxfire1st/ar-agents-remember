# mcp/tests/test_canvas_host.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The host's HTTP and protocol boundary: what a page may load, what a session may ask, and which evidence reference opens — one case per host rule, against the real policy, validator and a published revision.

## Code Commentary

- Every response carries its policy headers; a session serves its own document and assets and refuses anything else.
- Protocol messages are bound, bounded and replay-safe before an effect.
- The malformed-flood case freezes the live session ledger's clock at its start, so its refill-dependent quota assertion is controlled by the test rather than by elapsed host time.

- The header case also checks the policy’s 512 MiB task cap. The default policy declares no per-revision file or byte limit.

## Evidence

- The header case checks document and asset policy, opaque script sandboxing and no cookie header. It also asserts the 512 MiB task cap and the absence of default per-revision asset and byte limits. [3]
