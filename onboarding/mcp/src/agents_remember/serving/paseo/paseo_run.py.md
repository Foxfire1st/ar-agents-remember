# mcp/src/agents_remember/serving/paseo/paseo_run.py

## Governing Overview

[overview](../overview.md)

## Purpose

The provision context and the read-only admission for an install that must preserve a live host.

## Code Commentary

`_check_install_restart` reads the home's process record, the running Node, an unfinished provider write, the daemon status and the pending start-only settings before any write; the reasons it returns become `restartRequired`. `preserve_live_install` re-checks a live supervisor at the irreversible sites so admission never authorizes replacing or stopping a subsequently observed live host.

## Evidence

- The pre-write admission and its restart reasons. [1]
- The irreversible-site guard for an install. [2]
