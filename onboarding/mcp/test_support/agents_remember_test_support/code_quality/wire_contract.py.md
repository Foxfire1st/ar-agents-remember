# mcp/test_support/agents_remember_test_support/code_quality/wire_contract.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Reject post-``model_dump`` mutations that escape model validation (L6-R10).

## Code Commentary

### Logic

Module-level surface:

- `Taint` (class, lines 84-92) — Local names known to hold a dumped dict, or a container holding one.
- `Producers` (class, lines 96-105) — The two ways a call can hand back a dumped dict, discovered package-wide.
- `_is_dump_call` (function, lines 112-117)
- `_callee_name` (function, lines 120-126) — The terminal name of a call target -- ``f``/``x.f``/``a.b.f`` all give ``f``.
- `_is_copy_of` (function, lines 129-137) — ``dict(x)``, ``x.copy()``, ``copy.deepcopy(x)`` -- a copy of a dump is still one.
- `_passes_through_a_dump` (function, lines 140-144) — A pass-through called on a dump returns that dump -- see :func:`returns_a_parameter`.
- `produces_dump` (function, lines 147-158) — Whether this expression evaluates to a dict that came out of a model.
- `_wrapper_produces_dump` (function, lines 161-175) — The forms that wrap another expression: a container index, a spread, a merge.
- `_holds_dump` (function, lines 178-182) — A tuple/list literal with a dump inside it -- how ``_ProjectionBodyCache`` memoizes.
- `_bindings` (function, lines 185-193) — ``(target, value)`` for every single-target assignment in this scope.
- `scope_taint` (function, lines 196-218) — Local names holding a dumped dict, to a fixed point over the scope's assignments.
- `returns_dump` (function, lines 221-228) — Whether this function hands a dumped dict back to its caller.
- `returns_a_parameter` (function, lines 231-248) — Whether this function hands one of its own arguments back.
- `_functions` (function, lines 251-254)
- `dump_returning_names` (function, lines 257-285) — Functions that hand a dumped dict back to their caller, to a fixed point.
- `validating_names` (function, lines 288-300) — Names of functions that hand a parameter to ``model_validate``.
- `_calls` (function, lines 303-304)
- `_validates_one_of` (function, lines 307-310)
- `_mutation` (function, lines 313-331) — ``(name, line, how)`` when this statement changes a tainted dict in place.
- `_subscript_name` (function, lines 334-337)
- `_method_mutation` (function, lines 340-348)
- `_is_owner_merge` (function, lines 351-359) — ``x.update(served_state_tail(...))`` -- the one sanctioned serve-time tail merge.
- `_validated_after` (function, lines 362-372) — Whether ``name`` is handed back to a model below ``line``.
- `module_mutation_offenders` (function, lines 375-389) — Every dumped dict mutated and then let out of its function, in one parsed module.
- `_function_offenders` (function, lines 392-411)
- `_parse_package` (function, lines 414-419)
- `post_dump_mutation_offenders` (function, lines 422-432) — Every place the package changes a payload after its model stopped describing it.
- `served_tail_merges` (function, lines 435-454) — Where the sanctioned serve-time tail owner is actually called.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Taint` (lines 84-92) — Local names known to hold a dumped dict, or a container holding one.. [1]
- Defines the class `Producers` (lines 96-105) — The two ways a call can hand back a dumped dict, discovered package-wide.. [2]
- Defines the function `_is_dump_call` (lines 112-117). [3]
- Defines the function `_callee_name` (lines 120-126) — The terminal name of a call target -- ``f``/``x.f``/``a.b.f`` all give ``f``.. [4]
- Defines the function `_is_copy_of` (lines 129-137) — ``dict(x)``, ``x.copy()``, ``copy.deepcopy(x)`` -- a copy of a dump is still one.. [5]
- Defines the function `_passes_through_a_dump` (lines 140-144) — A pass-through called on a dump returns that dump -- see :func:`returns_a_parameter`.. [6]
- Defines the function `produces_dump` (lines 147-158) — Whether this expression evaluates to a dict that came out of a model.. [7]
- Defines the function `_wrapper_produces_dump` (lines 161-175) — The forms that wrap another expression: a container index, a spread, a merge.. [8]
- Defines the function `_holds_dump` (lines 178-182) — A tuple/list literal with a dump inside it -- how ``_ProjectionBodyCache`` memoizes.. [9]
- Defines the function `_bindings` (lines 185-193) — ``(target, value)`` for every single-target assignment in this scope.. [10]
- Defines the function `scope_taint` (lines 196-218) — Local names holding a dumped dict, to a fixed point over the scope's assignments.. [11]
- Defines the function `returns_dump` (lines 221-228) — Whether this function hands a dumped dict back to its caller.. [12]
- Defines the function `returns_a_parameter` (lines 231-248) — Whether this function hands one of its own arguments back.. [13]
- Defines the function `_functions` (lines 251-254). [14]
- Defines the function `dump_returning_names` (lines 257-285) — Functions that hand a dumped dict back to their caller, to a fixed point.. [15]
- Defines the function `validating_names` (lines 288-300) — Names of functions that hand a parameter to ``model_validate``.. [16]
- Defines the function `_calls` (lines 303-304). [17]
- Defines the function `_validates_one_of` (lines 307-310). [18]
- Defines the function `_mutation` (lines 313-331) — ``(name, line, how)`` when this statement changes a tainted dict in place.. [19]
- Defines the function `_subscript_name` (lines 334-337). [20]
- Defines the function `_method_mutation` (lines 340-348). [21]
- Defines the function `_is_owner_merge` (lines 351-359) — ``x.update(served_state_tail(...))`` -- the one sanctioned serve-time tail merge.. [22]
- Defines the function `_validated_after` (lines 362-372) — Whether ``name`` is handed back to a model below ``line``.. [23]
- Defines the function `module_mutation_offenders` (lines 375-389) — Every dumped dict mutated and then let out of its function, in one parsed module.. [24]
- Defines the function `_function_offenders` (lines 392-411). [25]
- Defines the function `_parse_package` (lines 414-419). [26]
- Defines the function `post_dump_mutation_offenders` (lines 422-432) — Every place the package changes a payload after its model stopped describing it.. [27]
- Defines the function `served_tail_merges` (lines 435-454) — Where the sanctioned serve-time tail owner is actually called.. [28]

## 260815-DAG Master Full-Gate Repair

The `validating_names` docstring path updated for the moved `application/task_docs/task_doc_tools.py` module; the conformance rule is unchanged.
