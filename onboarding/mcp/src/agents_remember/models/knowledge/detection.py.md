# mcp/src/agents_remember/models/knowledge/detection.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Carries mechanically observed detection signal values with closed conditions, recorded inputs and explicit scope limitations.

## Code Commentary

`DetectionSignalPayload` requires the condition vocabulary version, actual input set, observed changes, relationship paths, extractor/policy versions, scope manifest, unmapped paths and limitations. Its validators require the no-semantic-assessment limitation and consistency of truncation, unmapped paths and probe omissions. `detail` must equal the rendering of recorded basis; a trigger-side-only input cannot claim a two-sided comparison or counterpart absence. The canonical DetectionRun request/result/currentness/reproduction record and writer models are retired. A retained signal value is not a stored detection-run channel or a verdict.

## Evidence

### Repo-Internal References

- `DetectionSignalPayload` owns the current boundary described above. [30]
- `DetectionRecordedInputSet` owns the current boundary described above. [31]
- `DetectionScopeManifest` owns the current boundary described above. [32]
- `observed_basis_detail` owns the current boundary described above. [33]
