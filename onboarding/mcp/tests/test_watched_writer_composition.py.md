# mcp/tests/test_watched_writer_composition.py

## Governing Overview

[governing overview](overview.md)

## Purpose

F08: native events from actual serving producers converge without self wakes.

## Code Commentary

The retained composition runs the real Projector and EventStore at the durable lifecycle append boundary. It checks quiet own writes, capture-window healing within the configured 300-second full-refresh bound, and a prompt genuine outside-write wake, with lifecycle phase equality in the in-memory and disk projections. The clock and interposed outside append are test inputs. The removed terminal-relay, notifier, death-watch and gate composition is not current coverage; generic capacity protections remain in the own-write suite. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- The retained whole-projection witness asserts quiet own writes, bounded capture-window healing and genuine outside-write wake using lifecycle phase equality; no retired terminal/notifier/gate composition is claimed. [1]
