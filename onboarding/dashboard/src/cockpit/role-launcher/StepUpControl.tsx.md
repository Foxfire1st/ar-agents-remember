# dashboard/src/cockpit/role-launcher/StepUpControl.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The shared configured step-up action and receipt-derived status chips for the existing role-launch row.

## Current Contract

StepUpControl exists only when defaults.stepUp is truthy, respects its supplied disabled flag and prompts for a reason. A trimmed nonblank reply invokes onLaunch with canonical document scope plus stepUp only; current agent overrides are deliberately not copied. Cancel/blank does nothing. StepUpStatus exists only when execution.stepUp is truthy and renders Stepped-up plus reported model (or host default), with source in hover, and Mode/features unreported. Neither component sends a mode or permission choice, counts failures or decides host liveness. The caller owns request recovery and row placement.

## Invariants And Boundaries

This is candidate-source onboarding, not execution, CODE/MEMORY acceptance, serving-build currentness or permission to publish. The owning caller retains transaction, host and role authority.


## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [1]
- Reason admission, threshold and differing-harness/model inheritance boundary. [2]

- Saved taskless UUID/pending plus trimmed reason/override restoration keeps the legacy Investigator storage slot. [3]

- The same start-only reason enters saved retry payload and POST body. [4]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [5]
