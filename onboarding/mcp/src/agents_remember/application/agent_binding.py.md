# mcp/src/agents_remember/application/agent_binding.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Owns the launch identity that one role agent receives through its task-server environment.

## Code Commentary

AgentBinding.environment emits all seven binding variables and clears hosted-seat identities, including empty references. read_agent_binding treats no agent ID as unbound; a present ID requires canonical UUIDs, a known role, an absolute report path and exactly that role class reference pattern. Binding is reported identity, not an ambient replacement for per-call reader admission.

## Evidence

- Frozen implementation of AgentBinding supporting the stated file behavior. [1]

- Checks interpreter, -P module invocation, source, selected settings and single canonical server definition. [3]
- Starts generated stdio server and checks serving build package root and binding from selected source. [4]
- Checks emitted binding and explicitly empty absent references and seat identities before round-trip. [5]

## Investigator scope and request identity

The earlier system-specialist spelling is normalized to Investigator on reads while the recorded role value and addresses remain intact. Investigator accepts exactly Projects, sprint or sprint/master reference patterns; minted actor/request UUIDs, absolute report path and readable canonical topology remain mandatory. A role name or folder never supplies missing references.


- The current source implements this file’s stated Investigator boundary. [6]


## Refreshed current evidence

- Frozen implementation of read_agent_binding supporting the stated file behavior. [2]
