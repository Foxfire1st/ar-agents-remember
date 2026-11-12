# mcp/tests/test_closeout_certification_recovery.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Protects retained code-report transport with schema-valid plan/result/certificate compilers. It refuses undeclared or wrong-producer paths, oversize artifacts, inventory mismatches and conflicting producer paths before source reads or destination creation.

## Code Commentary

### Logic

`_inventory_snapshot` builds digest-valid untrusted manifest metadata. `_retained_inventory_case` starts from `selected_execution`, rebuilds rail/result/certificate authority through real compilers and validates the repaired prefix. The parametrized case reaches the actual snapshot guard without replacing selection validation or filesystem resolution.

### Invariants And Boundaries

- Retained inventories must match exact frozen producer publication and byte bounds.
- Schema-valid compiler-issued evidence still refuses conflicts and mismatches.
- Refusal precedes source resolution and destination creation.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.


- Schema-valid retained-report evidence refuses wrong inventory before source reads or destination creation. [1]


### Repo-Internal References


- Digest-valid untrusted manifests and rebuilt result/certificate prefixes reach the real retained-report guard. [2]


- Retained inventories refuse undeclared/wrong-producer paths, oversize artifacts, mismatches and conflicts before source reads. [4]


### Cross-Repo References

None; the tests use local certification owners.
