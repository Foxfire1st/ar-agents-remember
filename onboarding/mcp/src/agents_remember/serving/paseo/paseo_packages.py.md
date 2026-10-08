# mcp/src/agents_remember/serving/paseo/paseo_packages.py

## Governing Overview

[overview](../overview.md)

## Purpose

The immutable npm package tree shipped with this build.

## Code Commentary

`installed_lock_matches` compares the installed prefix's `package-lock.json` bytes with the packaged one, so an install whose tree was resolved on another day is not accepted as this build's host.

## Evidence

- The lock equality check against the packaged lock. [1]
