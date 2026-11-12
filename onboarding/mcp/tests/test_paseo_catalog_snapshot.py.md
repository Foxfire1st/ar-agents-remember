# mcp/tests/test_paseo_catalog_snapshot.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks the read-only saved-catalog endpoint independently of a fresh question or a start decision.

## Code Commentary

The case registers the real saved-catalog route on a small application. Before any snapshot exists, the answer is unknown and creates no files or bridge calls. After a successful catalog read, the endpoint returns saved agents and the original read time with no additional call or file change. Neither answer fabricates a discovery error, and the saved response contains no roleDefaults or execution.

## Invariants And Boundaries

The route exposes previously saved offers; it does not validate a launch or decide whether Start is available. The test uses temporary files and a fake bridge and does not claim a live-host execution.

## Evidence

### Repo-Internal References

- Unknown and saved responses preserve files, make no bridge call, invent no error and carry no start decision. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
