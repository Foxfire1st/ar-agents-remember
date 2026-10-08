# dashboard/src/test/loadIndependence.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

A source guard against reintroducing local wait ceilings, unmarked real timer sleeps and elapsed wall-clock correctness assertions into dashboard tests.

## Code Commentary

`scan` masks literal data with the existing TypeScript parser before removing comments, preserving source lines and quoted timeout property keys. It reports timeout properties, local `vi.setConfig` bounds, literal trailing test/hook bounds (including exponent notation), nonzero `setTimeout` delays and clock-based less/greater-than assertions. Clock assignments may span ordinary lines. A nonempty `// load-independent: <reason>` comment on the finding line or preceding line exempts that finding; marker text inside literal data is not an exemption. Zero-delay event-loop turns and ordinary clock data are accepted.

The population walk covers `.test`/`.test-utils` TS/TSX/MJS files under dashboard `src` and `scripts`, plus TypeScript/TSX/MJS files under `src/test`. The suite scans itself as well as synthetic positive, marker and literal/comment controls and expects an empty reported worklist.

## Invariants And Boundaries

This is a bounded source-pattern guard, not a proof that every test is load independent. It does not resolve arbitrary aliases or data flow, and its trailing-bound check covers numeric literals rather than arbitrary computed test/hook limits. An exemption records its written reason; the scan does not prove that reason. Shared guards remain owned by `setup.ts` and `vitest.config.ts`; product-timer and negative assertions still need their own controlled opportunities.

## Evidence

No Domain Documentation source is configured. The direct source below defines this repository-local test guard, without claiming a test rerun or browser evidence.

- Literal masking precedes comment and reason-marker recognition while preserving lines. [1]
- The scanner reports local bounds, nonzero sleeps and direct/assigned clock inequalities. [2]
- Synthetic positive and marker controls include multiline/exponent/literal-delimiter regressions. [3]
- The actual dashboard test-support population is scanned and must return an empty worklist. [4]
