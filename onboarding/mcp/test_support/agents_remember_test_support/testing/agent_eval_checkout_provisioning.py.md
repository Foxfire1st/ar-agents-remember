# mcp/test_support/agents_remember_test_support/testing/agent_eval_checkout_provisioning.py

## Governing Overview

[overview](overview.md)

## Purpose

The module holds two regression assertions for agent-eval trial provisioning, called by `mcp/tests/test_agent_eval_trial_setup.py` with a trial-setup test case and an actor profile. They check that native leaf publication declares test execution mode itself and that the scratch command-line child loads the trial's own settings file.

## Code Commentary

For both the primary and the linked checkout kinds, the native-leaf check clears the declared execution mode, replaces checkout resolution and forbids `BatchHost.start`, then provisions a trial. Provisioning must declare test mode, write the leaf contract and publication locator inside the trial project root, and create no coordination root at the checkout location.

The scratch command-line check intercepts the batch host's `provision` command at `agent_evals.trial_setup.subprocess.run`. It asserts the child's interpreter, `-P -c` arguments, working directory, environment and `--config` path, then runs the captured bootstrap verbatim in a fresh Python child. In that child the probe substitutes only the selected Paseo runtime operation; the CLI entry, parser, configuration loader and bootstrap run unchanged. The child must report test mode, the trial's settings path, its coordination root and the sandbox home. No actor or native host starts.

The probe's interpreter command line is an allowed literal in the Paseo single-path scan's allowance table (`mcp/tests/paseo_allowance_table.py`).

## Evidence

- The child probe substitutes only the selected host operation and executes the captured bootstrap unchanged. [1]
- Provisioning declares test mode, writes contract and locator in the project root and creates no checkout coordination root, with host start forbidden. [2]
- The scratch CLI child is checked for its argv, cwd, environment and loaded settings for both checkout kinds. [3]
