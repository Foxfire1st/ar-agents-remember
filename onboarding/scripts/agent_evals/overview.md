# Native-agent evaluation tooling

## Governing Overview

[repository overview](../../overview.md)

## Purpose

This development slice constructs private native-agent trials and retains the evidence needed to judge them. It supplies case admission, disposable trial setup, native capture, deterministic observations, independent rubric requests and attempt accounting. Case bundles and output roots are caller-owned inputs rather than a runtime registration surface.

## Construction

`run_curator.py` dispatches the CLI and calls `trials.run_trials` for concrete trials. Setup binds the fixture host, private actor state, serving build, native repositories and task-server definition before actor launch. Adapters bind actions to native session and source identities; graders keep deterministic faults separate from semantic questions. Judge packaging retains byte-exact evidence and validates the actual final send limits.

The separate hook-based API in `runner.py` has test callers and is not the CLI trial implementation. The disposable citation-write probe in `trial_native_setup.py` is likewise a separate capability API, not an every-trial action. Grade-source closure, the broader source/runtime snapshot and observed execution are distinct evidence classes.

## Invariants And Boundaries

Tooling checks do not enter measurement arithmetic. Missing capture, ambiguous bindings and semantic unknowns retain their own causes. Native exit success, actor success wording, a compiled text signature and a published verdict file do not independently establish review or landing acceptance. Retained fixtures are regression inputs, not fresh native runs.

Private actor homes and cleanup have declared ownership boundaries; their selected credential seeds do not establish an unrestricted secrecy guarantee. Eval look-back tooling has been removed. Product memory-baseline functionality is a different surface and remains outside that removal.

## Hot Path Summary

Start with `run_curator.py` and `trials.py` for a concrete command, `trial_setup.py` for provisioning, `adapters/` for native evidence, `graders/` for deterministic/rubric boundaries, and `accounting.py` or `regrade.py` for retained outcomes. Inspect source bindings before interpreting any result.

## Evidence

- CLI dispatch and concrete trial orchestration retain separate command, setup, capture and grading responsibilities. [1]

- Disposable setup binds host, actor state, source authority and native repositories before actor launch. [2]

- Captures and grades retain explicit evidence identities and semantic unknowns. [3]
- Accounting and regrading retain observed attempts and separate tooling checks from measurement results. [4]
