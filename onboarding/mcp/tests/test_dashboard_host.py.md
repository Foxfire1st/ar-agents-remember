# mcp/tests/test_dashboard_host.py

## Governing Overview

[overview](overview.md)

## Purpose

The dashboard/host composition cases: the three status exit codes print both lines and start nothing, adoption and autoStart call ensure_host while dashboard stop does not, the foreground serves without waiting for the host and --sim skips it, the real background function serves before the host outcome and logs, a supervised child does not start the host again, and a discovered config path is named in normal and transition outcomes.

## Code Commentary

The module drives the dashboard's dispatch, the serving daemon's supervision and the real background starter through fakes.

## Evidence

- The status exit codes and no-start case. [1]
- The stop-does-not-stop case. [2]
- The real background wiring case. [3]
