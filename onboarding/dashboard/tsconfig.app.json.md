# dashboard/tsconfig.app.json

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The TypeScript project configuration for the dashboard application source. It extends the dashboard's shared compiler options and bounds the app project's inputs.

## Code Commentary

The project sets `types: ["node"]` (explicit ambient Node types required under TypeScript 7), `noEmit`, and `incremental: true` with `tsBuildInfoFile: ./tsconfig.app.tsbuildinfo`, so `tsc -b` can reuse its previous result while checking the app project. The build-info file is ignored by `dashboard/.gitignore`; it is a local cache, not a published artifact or a source of type truth.

## Relationships

`dashboard/package.json` runs the typecheck through `tsc -b` (TypeScript 7) over the referenced projects. The node and driver projects carry the same `types: ["node"]` and incremental settings for their own inputs. `.githooks/_gate.sh` runs the dashboard typecheck in the fast and targeted tiers, so a stale or disabled cache would change the hook's cost without changing its verdict.

## Evidence

- The app project declares `types: ["node"]` for TypeScript 7 and enables incremental checking with an explicit gitignored build-info file. [1]
- The dashboard ignore rules exclude TypeScript build caches. [2]
