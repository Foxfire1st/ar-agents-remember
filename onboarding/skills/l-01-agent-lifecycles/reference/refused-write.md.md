# skills/l-01-agent-lifecycles/reference/refused-write.md

## Governing Overview

[overview](../overview.md)

## Purpose

Owns the narrow recovery procedure for an admitted tool refusing a correct write.

## Code Commentary

### Invariants And Boundaries

The procedure retains the refusal, corrects faulty input through the same tool, checks build and admitted route, and requires owner notification plus declared manual provenance for any covered manual recovery. Missing capability, permissions, guards, validation and transaction gates retain their stops. It covers only the refused tool and input class and grants no new role or target authority; the Curator's command-line binding is read from `knowledge/serving-build.md`. The stops also require every validator and gate finding to be repaired at once, allow `--no-verify` only on the developer's word for one occasion, and send a denied or unanswered harness request to the orientation operation's permission rules.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]

- The stops section keeps every refusal and gate, requires immediate repair of findings and limits `--no-verify` to a developer-allowed occasion. [2]
