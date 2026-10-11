# scripts/python-runtime-contract.env

## Governing Overview

[repository overview](../overview.md)

## Purpose

The single sourced contract for the managed Python runtime and the uv version consumed by host setup and the certified container.

## Code Commentary

The exact Python release, minor line, supported package range, verified source and builder identities stay distinct. Host bootstrap treats `AR_UV_VERSION` as a numeric minimum and uses a qualifying PATH uv without installing one. The certified container installs exactly that same assignment, not an independently duplicated version. Raising or lowering the host acceptance policy does not change the Python pin or package range.

## Evidence

- One contract supplies the runtime identities and distinguishes the host uv minimum from the container's exact install. [1]
