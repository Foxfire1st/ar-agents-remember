# mcp/tests/test_canvas_presenter_authoring.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

- Two fixture authoring runs over one comparison — a default and a custom design text — keep every claim and evidence reference, and an authority-seeking design is fenced, disclosed and still authored; both run against the local fixture and supply no native or model authoring evidence.

## Code Commentary

- The same comparison under two design texts keeps the claims, references and coverage.
- A design that asks for authority is not followed and the conversation says so.


The two authoring runs explicitly inject the deterministic `LocalPresenterHarness` and assert its local bytes. The native presenter launch was retired, so these cases supply neither native-host nor model-authoring evidence.

## Evidence

- The case `test_default_and_custom_runs_author_one_comparison_and_keep_every_claim` protects this behaviour. [1]
- The case `test_an_authority_seeking_design_is_fenced_disclosed_and_still_authored` protects this behaviour. [2]

- The two authoring runs explicitly inject the deterministic `LocalPresenterHarness` and assert its local bytes. The native presenter launch was retired, so these cases supply neither native-host nor model-authoring evidence. [3]
