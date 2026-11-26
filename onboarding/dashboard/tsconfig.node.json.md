# dashboard/tsconfig.node.json

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The TypeScript project configuration for the dashboard's Node-side source. It extends the dashboard's shared compiler options over that project's inputs.

## Code Commentary

The project sets `noEmit` and `incremental: true` with `tsBuildInfoFile: ./tsconfig.node.tsbuildinfo`, so `tsc -b` can reuse its previous result for the Node project. The build-info file is ignored by `dashboard/.gitignore`; it is a local cache, not a published artifact or a source of type truth.

## Relationships

`dashboard/package.json` runs the typecheck through `tsc -b` over the referenced projects. The app and driver projects carry the same incremental setting. `.githooks/_gate.sh` runs the dashboard typecheck in the fast and targeted tiers, so the cache changes the hook's cost without changing its verdict.

## Evidence

- The node project enables incremental checking with an explicit gitignored build-info file. [1]
- The dashboard ignore rules exclude TypeScript build caches. [2]
