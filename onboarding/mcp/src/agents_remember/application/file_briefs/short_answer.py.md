# mcp/src/agents_remember/application/file_briefs/short_answer.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Fits assembled file-brief facts into the bounded read_ar_files reply.

## Code Commentary

The fitter reserves a row for every requested path before expanding rows in request order. When the first candidate's whole row fails to fit, it keeps as many leading rule statements as possible. If a later whole row fails, it leaves that row and the remaining candidates counts-only. The caller switches to compact rows if the minimum projection overflows.

## Evidence

- The fitter reserves minimum rows, adds whole rows in request order and clips rule text only in the first candidate. [1]
