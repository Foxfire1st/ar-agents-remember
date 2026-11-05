# scripts/agent_evals/reference_epochs/g1-20261030/epoch.json

## Governing Overview

[governing overview](../../overview.md)

## Purpose

Pins the retained G1 grading-reference epoch: its original source path, byte identity and size, scoped lines, source tree/blob, runtime evidence-copy path and backing authority documents. The manifest explicitly labels this as an evidence copy rather than a current instruction source. 

## Code Commentary

### Invariants And Boundaries

The grading-policy loader checks this manifest's fixed hash, the declared policy scope and the retained reference's bytes before returning that reference. A changed binding is refused. 

The epoch's historical source identity establishes which grading reference is retained; it does not make that historical procedure the current role instructions or establish any trial's outcome.

## Evidence

- Historical evidence-copy identity, scope and runtime source path, explicitly not current instructions. \[1] [1]
- The loader verifies the fixed epoch manifest hash, policy binding, scope and retained-reference size/hash. \[2] [2]
