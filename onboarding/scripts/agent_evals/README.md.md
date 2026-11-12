# scripts/agent_evals/README.md

## Governing Overview

[governing overview](overview.md)

## Purpose

Documents the native Curator evaluation commands, trial setup, evidence capture, grading and retained-attempt workflows. Tooling smoke runs and model measurements have separate purposes and accounting. 

## Code Commentary

### Invariants And Boundaries

The documented non-GPT Hermes auth observation compares whole-file bytes. The GPT branch compares only the canonical selected `openai-codex` provider and credential-pool entries; equality makes no claim about other providers or top-level metadata. Neither comparison identifies a writer or establishes a clean-run verdict.  The implementation preserves this distinction. 

Preflight validates the supplied case trees; native quality intake and captured before/after grading remain separate checks. Eval attribution distinguishes newly introduced or actor-written blocking findings from unchanged inherited findings, while the product writer and commit/landing validators retain their whole-tree guarantees. 

Command examples, retained fixtures and documented test coverage do not establish a completed native trial, measurement, review or landing acceptance. Retained-attempt census and regrading do not rerun the actor.

## Evidence

- Development ownership and CLI trial, tooling-check and measurement boundaries. [1]

- Documented non-GPT whole-file versus GPT selected-entry auth observations and their limits. \[2] [2]
- Selected-entry canonicalization and single-use whole-file/selected-subject comparison implementation. \[3] [3]
- Case preflight, native quality intake and before/after eval attribution preserve the product whole-tree validators. \[4] [4]

- Usage documentation distinguishes command hooks and focused tests from measurements, and census/regrade from actor reruns. [5]
