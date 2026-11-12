# mcp/tests/test_watched_writer_composition.py

## Governing Overview

[governing overview](overview.md)

## Purpose

F08: native events from actual serving producers converge without self wakes.

## Code Commentary

The retained composition runs the real Projector/watch owner with native task documents, blocked-start progress and a retained dismissal log. A lock-ignoring dismissal append is interposed after the owned append flush at descriptor capture. Its echo remains quiet, then full healing removes the acknowledged blocked-start item from both in-memory and disk attention queues within the configured full-refresh bound while retaining the dismissal. A subsequent real write_task_doc outside update wakes the composition and publishes its changed task title in memory and on disk. The clock and interposed append are controlled test inputs. The removed terminal-relay, notifier, death-watch and gate composition is not current coverage; generic capacity protections remain in the own-write suite. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Quiet native own writes settle; dismissal capture-window healing and genuine outside task writes reach memory/disk projections. [2]
