# mcp/src/agents_remember/cli/paseo_catalog_names.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Resolves configured choice spellings using host catalog IDs and labels.

## Code Commentary

### Logic

`canonical_fields` canonicalizes provider, model and effort only when their supplied host rows match. `canonical_defaults` applies that rule to defaults and per-field provenance; `canonical_model_choices` resolves the final model and effort. Matching uses named_choices.named, which checks IDs before labels without case. `part_known` separates unanswered parts from known offerings; unknown values are retained for later pass-through.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
