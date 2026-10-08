# mcp/tests/test_paseo_host_environment.py

## Governing Overview

[overview](overview.md)

## Purpose

The session-identity cases: the daemon runner drops every listed session name while keeping a login and a home selector, process observation reports only the names, the filter matches exact harness names and the two prefixes, and only the npm child gets the product Node's PATH without losing logins.

## Code Commentary

The module exercises `host_environment`, the real command runner with a fake subprocess and the process-record reader against synthetic /proc data.

## Evidence

- The runner scrub-and-keep case. [1]
- The name-only observation case. [2]
- The exact-name filter case. [3]
