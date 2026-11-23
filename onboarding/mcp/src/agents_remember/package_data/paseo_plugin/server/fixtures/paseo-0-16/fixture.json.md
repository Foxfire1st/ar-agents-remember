# mcp/src/agents_remember/package_data/paseo_plugin/server/fixtures/paseo-0-16/fixture.json

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The provenance manifest records the copied distribution and every fixture input.

## Code Commentary

It records Paseo 0.16.2 and the source installation separately from the default prefix. Each of its 19 file records gives the copied path, byte count and SHA-256 digest. The ACP test checks the version and complete file set against the recorded sizes and digests without needing the original installation.

## Evidence

- The manifest names the source and version and lists each copied file with its size and digest. [1]
- The fixture integrity case checks the version, file inventory, sizes and digests. [2]
