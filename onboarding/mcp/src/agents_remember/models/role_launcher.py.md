# mcp/src/agents_remember/models/role_launcher.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines canonical role selections and HTTP launcher call models.

## Code Commentary

RoleSelection carries exact sprint/master/leaf references; request aliases keep the current role/Paseo vocabulary. RoleAgentOverride separates agent/model/effort/feature values with an optional agent id; service tier is inherited native configuration and its capability projections rather than a Boolean fast transport alias. `featureValues` carries strict booleans or option ids, and the override states no mode. RoleDispatchRequest distinguishes start/revive under the saved request UUID and carries optional replacesAgentId plus replacesInterruptTurn. Replacement remains an explicit request; the model does not authorize retirement or free an occupied seat. The default-false `chatStarted` field records a parentless start from a chat without a role under R113 rule6; dashboard/role-agent starts do not use it. This wire marker is not authority to start, attach a parent or bypass replacement admission.

## Evidence

- Parentless chat-start marker is default false wire data, not launch or replacement authority. [5]




- Frozen implementation of RoleAgentOverride supporting the stated file behavior. [2]
- Frozen implementation of RoleDispatchRequest supporting the stated file behavior. [3]

## Investigator scope and request identity

Investigator is canonical in new selection output. The parsed selection retains whether the one earlier role spelling was supplied so API answers can carry the exact notice. Per-request receipt cardinality is independent of Projects versus selected-task altitude; neither creates caller permission.


- The current source implements this file’s stated Investigator boundary. [4]


## Refreshed current evidence

- Frozen implementation of RoleSelection supporting the stated file behavior. [1]
