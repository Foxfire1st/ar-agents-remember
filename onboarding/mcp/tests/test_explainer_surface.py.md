# mcp/tests/test_explainer_surface.py

## Governing Overview

[Tests](overview.md)

## Purpose

Check the normal server's general tools plus the four launch-bound explainer tools and their seat binding.

## Code Commentary

A bound server advertises AR's general tools and exactly `render`, `define_category`, `remove_category` and `grade` as its explainer additions. Calling a general AR tool is not refused merely because the caller is an explainer.

An invalid, non-JSON or empty binding refuses service. An ordinary server with neither marker nor binding keeps the general roster. A launched seat that loses its binding cannot take that ordinary branch. A binding without configuration still validates itself.

The four explainer tools refuse a forged seat and serve their launched seat. A new generation refuses the old server's explainer calls, and a marker pointing to another environment refuses. These tests establish binding and advertisement; page delivery and workspace removal belong to their own tests.

## Evidence


- A bound server advertises general tools and exactly four explainer additions. [5]
- General tools answer an explainer under their normal admission. [6]
- The four bound tools refuse a forged launched seat. [7]

- A launched seat with a lost binding refuses service instead of taking the ordinary branch. [3]
- An old server's explainer calls refuse after a new generation. [4]
