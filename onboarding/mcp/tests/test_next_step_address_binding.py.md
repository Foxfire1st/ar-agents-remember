# mcp/tests/test_next_step_address_binding.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin contract-derived landing hints and response-address confinement without a process/session cursor.

## Code Commentary

The module directly calls compute_next_step(contract, tool, guidance=...) on two distinct WorktreeContracts. Their closeout difference produces different hints, each binds its own contract, and neither serialized response contains the other path. No LifecycleState fixture is supplied. The binder drops contradicting hints, retains an own hint by identity, and withholds a hint when TaskDocResponse declares neither contractPath nor enclosurePath. That carrier boundary must not be described as pass-through. These tests do not create a coordination service or restore removed task_doc reads; the old read_steps operation string is only a response-model fixture.

## Retained Full-Card Audit Context

The following distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe that recorded epoch. They add no fresh execution, mutation result or acceptance. Historical numeric reference labels are custody text and do not select live sidecar anchors.

### Addressless-carrier correction and citation custody

> - **The stated reach: the one carrier that declares no address — `TaskDocResponse` — has its hint WITHHELD, asserted against the model's own fields. `260918-TSIP-L10` renamed this case because it asserted the opposite until that leaf; the row is corrected with it.** [Past-epoch source caption, detached from live reference 11. Recorded citation custody: mcp/tests/test_next_step_address_binding.py blob d1d22b20b04b8f4ae8fe80c1bbeb5e5d125616c9 (available); mcp/src/agents_remember/models/task_doc.py blob e7d80ed372402d196e9af03c6aa40d32a018d7e2 (available); historical event commit not identified. No historical event or intent inferred.]

The current source docstring independently records the L10 correction. The two available blobs are retained citation custody, not newly inferred event commits, execution or acceptance. The repeated standalone custody line in the base adds no distinct fact beyond this complete caption.

## Evidence

- The module's own statement of D-13 and of the two fixes it pins. [1]

- **The binder's one rule: a hint whose arguments contradict the response's own address is omitted, and a response that declares no address has its hint withheld.** [2]

- The two field tuples the comparison reads. [3]

- **The contract-derived hint, which is why no global cursor can reach a caller.** [4]


- One addressed contract, with the closeout state its hint is derived from. [6]

- The address-carrying envelope of the carrier D-13 was measured on. [7]
- **The contradicting-address case: the hint is omitted, not forwarded.** [8]
- The positive control: the omission is a contradiction check, not blanket suppression. [9]

- **The plan's case, driven as a sequence: two addressed contracts yield two different hints and neither body carries the other's path.** [10]

Anchor: `test_an_envelope_with_no_address_has_its_hint_withheld` `TaskDocResponse`

Current source: The current test asserts TaskDocResponse declares neither contractPath nor enclosurePath and bound_next_step returns None for a foreign-address hint on that response. These source assertions establish no new execution or historical repair event.

- A foreign address is omitted, not forwarded. [13]
- An own-address hint is retained by identity. [14]
- Two contract-addressed calls yield distinct isolated hints. [15]
- An addressless response withholds guidance rather than passing it unchecked. [16]


- The current test asserts TaskDocResponse declares neither contractPath nor enclosurePath and bound_next_step returns None for a foreign-address hint on that response. These source assertions establish no new execution or historical repair event. [11]

- The `unit-regression` lane selects `mcp/tests/test_next_step_address_binding.py`. [12]
