# dashboard/src/cockpit/role-launcher/roleLauncherDisplay.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Resolve offered agent/model/effort choices and complete selector display labels.

## Code Commentary

Pure lookups and shared empty-array defaults preserve chosen-versus-role-default labels and provenance inputs. Foreign-agent mode/default behavior remains a caller decision; these helpers do not silently replace the role defaults supplied to them.

## Boundaries

Presentation, not selection repair, options loading, backend permission or final Start readiness.

## Evidence

- resolveAgentChoice is a current owner of the behavior described above. [1]
- displayedModelLabel is a current owner of the behavior described above. [2]
