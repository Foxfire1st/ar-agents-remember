# dashboard/src/cockpit/RoleChats.modelOptions.test.tsx

## Governing Overview

[Dashboard source](../overview.md)

## Purpose

Exercises the mounted launcher’s metadata and shown-model request contract with a mocked fetch transport.

## Code Commentary

Cases check model selection and cache reuse, Refresh ordering and generation changes, and selection during a pending response. The suite also checks omitted feature overrides on a new Start and preservation of a saved Retry payload.

## Evidence

- The mounted cases assert request bodies and visible launcher state across opening, selection, Refresh, Start and Retry. [1]
