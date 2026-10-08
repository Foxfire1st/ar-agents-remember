# scripts/pnt_sandbox/render_starter_settings.py

## Governing Overview

[overview](../../overview.md)

## Purpose

The borrowed public renderer helper the sandbox tooling calls with the sandbox's root and ports.

## Code Commentary

`render` invokes the frozen tooling's own public renderer for one harness input and records the rendered settings, so the sandbox consumes a file the renderer itself wrote instead of a hand-built second topology; the caller still supplies the product's SDK and the sandbox's recorded root and ports.

## Evidence

- The renderer invocation the sandbox uses. [1]
