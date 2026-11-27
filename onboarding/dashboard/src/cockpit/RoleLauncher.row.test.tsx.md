# dashboard/src/cockpit/RoleLauncher.row.test.tsx

## Governing Overview

[Dashboard source overview](../overview.md)

## Purpose

Mounted launcher presentation regressions: compact controls preserve accessible names, selected labels and default provenance while using the cockpit view tabs' shared look.

## Code Commentary

The suite mounts the real RoleChatsPane against controlled options replies. It rejects the former defaults sentence and visible selector titles; verifies accessible names and hover text; checks the mode selector’s offered values, empty first option and source, alongside settings-row and host-profile precedence and reset on an agent change; and checks complete displayed labels for defaults, explicit agent/model/effort/feature overrides and selected document titles. The Sprint selector's empty choice is asserted as “No sprint”, the real no-sprint option the standalone-master launcher offers. Permission-bearing features remain non-editable settings-owned chips; Instructions is present only with notes and its hover identifies the source. The existing service-tier disclosure retains its test id, text and hover as a shared chip.

The shared-definition case compares actual rendered classes for ModeBar, every launcher selector, Start, Refresh and the Instructions chip, then inspects raw consumer source to prevent a copied tab definition. The overfull case retains every extra feature, rejects an overflow menu and rejects wide-nowrap source. Fixture defaults include provenance and notes, and a long second-model label deliberately exercises override-hover recovery. The row-control, hover-provenance, and shared-selector cases await the asynchronously fetched `Speed override` control via `findByLabelText('Speed override')` before asserting its presence, hover text, or override interaction.

## Boundaries

These DOM/class/source assertions are not browser width or computed-layout measurements, native agent creation, permission enforcement or full certification. The actual ordinary 1440px and excess-feature viewport witnesses remain task evidence; this test source does not measure their pixel heights. Vitest callbacks are not named TypeScript symbols, so evidence here is a whole-test-file reference, not an invented named proof anchor.

## Current scoped contract

The reasoned step-up case mounts `RoleLauncher`, asserts `{role, stepUp}` at `onLaunch`, and checks `RoleExecutionStatus` and `StepUpStatus` first show host default and then the observed model. This is component behavior with supplied status objects and a mocked launch callback; the separate `RoleChats.stepUp.integration.test.tsx` owns storage/retry and cross-harness pane folding.

## Evidence




- Mounted row tests cover the shared control structure, fixture-projected choices and action readiness. [1]







- Fixtures supply offered modes, choice provenance and instruction metadata. Model-specific replies reuse the requested model’s fixture data. [2]









- Source and mounted assertions cover the compact control row and the configured Step up reason and actions. [3]
