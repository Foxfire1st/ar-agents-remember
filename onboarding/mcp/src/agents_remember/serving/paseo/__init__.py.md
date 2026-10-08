# mcp/src/agents_remember/serving/paseo/__init__.py

## Governing Overview

[overview](../overview.md)

## Purpose

The shared host-runtime package used by the install step and dashboard supervision. The move of the host modules from `cli/` into this package is what let both the install rank and the serving rank reach them without a forbidden import.

## Code Commentary

The package docstring names its scope: shared host runtime operations used by install and dashboard supervision. It holds no behavior of its own.

## Evidence

- The package marker and its stated scope. [1]
