# mcp/src/agents_remember/serving/daemon_processes.py

## Governing Overview

[overview](overview.md)

## Purpose

Platform-native inspection of which process listens on a dashboard socket and what its command line is, for dashboard supervision.

## Code Commentary

- `listening_dashboard_pid(host, port)` answers the pid of a product dashboard process that holds a listening TCP socket for that address and port, or `None`. On Linux it reads the listening socket inodes from `/proc/net/tcp` and `/proc/net/tcp6` (an exact address match or a wildcard bind), then finds a dashboard process whose `/proc/<pid>/fd` links to one of them. On macOS it asks `/usr/sbin/lsof` for the listeners (2 s limit) and returns the first whose arguments name a dashboard. Any other platform raises `OSError(ENOSYS)`.
- `process_arguments(pid)` returns the exact argv: `/proc/<pid>/cmdline` on Linux, the `KERN_PROCARGS2` sysctl on macOS (arguments with spaces stay whole). Other platforms raise `OSError(ENOSYS)`.
- `pid_is_dashboard(pid)` is true only when the command line contains `dashboard` and an `agents_remember` or `agents-remember` marker; an unreadable process (gone, zombie, foreign user) is false. `serving/daemon.py` uses it as the identity half of liveness.

The module answers facts only; it sends no signal. A failure to inspect is an `OSError` that `daemon_identity.observe_dashboard` turns into an unknown identity.

## Evidence

- Linux and macOS listener lookup; other platforms are unavailable. [1]
- Exact argv on Linux and macOS. [2]
- The macOS listener query through lsof with a time limit. [3]
- A Linux socket owner must be a dashboard process holding one of the listening inodes. [4]
- The dashboard command-line markers. [5]
- Listening inodes for an exact or wildcard address. [6]
