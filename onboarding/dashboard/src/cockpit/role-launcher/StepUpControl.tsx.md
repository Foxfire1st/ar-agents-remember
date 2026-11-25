# dashboard/src/cockpit/role-launcher/StepUpControl.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The shared configured step-up action and receipt-derived status chips for the existing role-launch row.

## Current Contract

StepUpControl exists only when defaults.stepUp is truthy, respects its supplied disabled flag and prompts for a reason. A trimmed nonblank reply invokes onLaunch with canonical document scope plus stepUp only; current agent overrides are deliberately not copied. Cancel/blank does nothing. StepUpStatus renders when the receipt includes step-up. It shows the reported model or “host default”, with its source in hover. It reads the mode observation from the top-level receipt choice when that choice exists, and reads the nested session-options choice when the top-level choice is absent. The chip text shows the observed host mode. When the mode record has a source, its hover displays the provenance of the requested choice. That source can name user settings even when the host applied a different mode. Without an observation it reads “Mode/features unreported”. Neither component sends a mode or permission choice, counts failures or decides host liveness. The caller owns request recovery and row placement.

## Invariants And Boundaries

This is candidate-source onboarding, not execution, CODE/MEMORY acceptance, serving-build currentness or permission to publish. The owning caller retains transaction, host and role authority.


## Evidence


- Reason admission, threshold and differing-harness/model inheritance boundary. [2]

- Completed typed rounds supply the worker and curator counts. Incomplete history is reported, and a record-only correction revises its existing round. [1]

- The backend checks the explicit reason and the configured failed-review threshold. A step-up reads mode from its own settings row. Other launch fields follow the same-harness and model inheritance rule. [2]



- The launcher model restores the saved taskless request ID, pending flag and override with a trimmed reason. Investigator retains its original storage slot. [3]



- The same start-only reason enters saved retry payload and POST body. [4]
- The configured Step up button sends canonical document scope and a trimmed nonblank reason. The status shows the host’s observed mode when present and uses the requested choice’s provenance in hover. Without an observation it labels the mode unreported. [5]
