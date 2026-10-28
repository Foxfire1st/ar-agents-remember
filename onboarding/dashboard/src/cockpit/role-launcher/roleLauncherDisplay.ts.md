# dashboard/src/cockpit/role-launcher/roleLauncherDisplay.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Resolve offered agent/model/effort choices and complete selector display labels.

## Code Commentary

Pure lookups match offered IDs or labels without case and preserve chosen-versus-role-default labels and provenance inputs. A configured model name survives an unavailable model listing; unknown model offers label it unchecked rather than replacing it. Shared empty arrays represent absent rows, not a successful empty host answer. Foreign-agent mode/default behavior remains a caller decision; these helpers do not silently replace the role defaults supplied to them.

## Boundaries

Presentation, not selection repair, options loading, backend permission or final Start readiness.

## Evidence

- resolveAgentChoice is a current owner of the behavior described above. [1]

- displayedModelLabel is a current owner of the behavior described above. [2]

