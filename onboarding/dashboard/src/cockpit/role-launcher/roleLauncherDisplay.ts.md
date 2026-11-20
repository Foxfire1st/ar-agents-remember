# dashboard/src/cockpit/role-launcher/roleLauncherDisplay.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Resolve offered agent, model and effort choices and compute selector labels and mode defaults.

## Code Commentary

Pure lookups match offered IDs or labels without case and preserve chosen-versus-role-default labels and provenance inputs. A configured model name survives an unavailable model listing; unknown model offers label it unchecked rather than replacing it. Shared empty arrays represent absent rows, not a successful empty host answer. The mode helper lists the selected agent’s offers. It takes the applicable host-profile default first, then the mode of the settings row when that row names the selected harness. It uses the resolved role default on the role agent, then the selected agent’s advertised default or an empty value.

## Boundaries

Presentation, not selection repair, options loading, backend permission or final Start readiness.

## Evidence

- resolveAgentChoice is a current owner of the behavior described above. [1]

- displayedModelLabel is a current owner of the behavior described above. [2]

- The empty mode-selection option derives its value and provenance from the selected harness and resolved role defaults. [3]

