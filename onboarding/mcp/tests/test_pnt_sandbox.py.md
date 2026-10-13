# mcp/tests/test_pnt_sandbox.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

The safety suite judges outside, missing and defaulted AR roots, exact sandbox values and resolving-build identity. Build-input cases preserve unmarked directories, marker replacement, repeatable incomplete reset, generated layout/settings and exact environment scrub. Port and environment checks use real child processes; failed-rmdir recovery includes a mock. The resolver-success control executes the real `build_roots.py` command and checks the JSON rather than exit zero alone: errors are empty, roots have exactly the expected keys and all values are non-null, including the five repository resolver roots. This protects the existing sandbox script; it does not claim that script was repaired here.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## 260928-MIK-L96 The public install route and product Node roots

The sandbox tests gained the public install route receipts and admission cases, the foreign-package refusal, the cut/timeout/malformed receipt retirement, and the product Node and cache-root safety cases; their cards' safety and environment rules keep their obligations.

- The safety case for the product Node and cache roots. [2]
- The public install receipt cases. [3]
- The foreign-package admission case. [4]

- The real resolver command must return empty errors, every expected non-null root and five resolver keys. [5]
