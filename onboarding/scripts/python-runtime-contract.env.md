# scripts/python-runtime-contract.env

## Governing Overview

[repository overview](../overview.md)

## Purpose

The single POSIX-shell-readable contract for the uv-managed Python minor line, package Python requirement range, and uv minor line consumed by host setup, Git hooks, GitHub workflows, and Dagger.

## Code Commentary

Declares `AR_PYTHON_MINOR=3.14`, `AR_PYTHON_REQUIRES='>=3.14,<3.15'`, and `AR_UV_VERSION=0.13` with no exact patch pins or source-build fields. Host bootstrap treats `AR_UV_VERSION` as a numeric minimum and uses a qualifying PATH uv without installing one. CI workflows (`astral-sh/setup-uv` with `${AR_UV_VERSION}.x`) and the Dagger candidate image (`ghcr.io/astral-sh/uv:${AR_UV_VERSION}`) install the newest patch in that uv minor line and record the exact uv obtained.

## Evidence

- One contract supplies the Python minor line, package requirement range, and uv minor line, distinguishing the host uv minimum from CI and Dagger installing the newest patch in that line. [1]
