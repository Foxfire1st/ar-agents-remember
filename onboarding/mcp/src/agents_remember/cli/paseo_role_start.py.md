# mcp/src/agents_remember/cli/paseo_role_start.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns role and leaf-set start policy behind the role-tool facade.

## Code Commentary

### Logic

`start_rule_violation` checks the caller/target matrix and task containment. `start_role` and `start_leaf_set` share one current-operation catalog question, then use the existing dispatch and receipt owners. `_start_role` carries caller-harness identity, configured step-up and agent overrides into the typed request; it validates a bound free-agent override before configured-host dispatch. Leaf-set starts remain restricted to the owning Manager. Start answers retain existing explicit runtime/refusal outcomes.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
