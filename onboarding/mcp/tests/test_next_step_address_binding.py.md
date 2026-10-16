# mcp/tests/test_next_step_address_binding.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin contract-derived landing hints and response-address confinement without a process/session cursor.

## Code Commentary

The module directly calls compute_next_step(contract, tool, guidance=...) on two distinct WorktreeContracts. Their closeout difference produces different hints, each binds its own contract, and neither serialized response contains the other path. No LifecycleState fixture is supplied. The binder drops contradicting hints, retains an own hint by identity, and withholds a hint when TaskDocResponse declares neither contractPath nor enclosurePath. That carrier boundary must not be described as pass-through. These tests do not create a coordination service or restore removed task_doc reads; the old read_steps operation string is only a response-model fixture.

## Evidence

- The module's own statement of D-13 and of the two fixes it pins. [1]
- **The binder's one rule: a hint whose arguments contradict the response's own address is omitted; an ambiguous address is a refusal.** [2]
- The two field tuples the comparison reads. [3]
- **The contract-derived hint, which is why no global cursor can reach a caller.** [4]
- One addressed contract, with the closeout state its hint is derived from. [6]
- The address-carrying envelope of the carrier D-13 was measured on. [7]
- **The contradicting-address case: the hint is omitted, not forwarded.** [8]
- The positive control: the omission is a contradiction check, not blanket suppression. [9]
- **The plan's case, driven as a sequence: two addressed contracts yield two different hints and neither body carries the other's path.** [10]
- **The stated reach: the one carrier that declares no address — `TaskDocResponse` — has its hint WITHHELD, asserted against the model's own fields. `260918-TSIP-L10` renamed this case because it asserted the opposite until that leaf; the row is corrected with it.** [11]
- The lane catalog declares this module; registration does not prove invocation. [12]

- A foreign address is omitted, not forwarded. [13]
- An own-address hint is retained by identity. [14]
- Two contract-addressed calls yield distinct isolated hints. [15]
- An addressless response withholds guidance rather than passing it unchecked. [16]
