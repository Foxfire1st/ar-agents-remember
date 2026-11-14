# mcp/src/agents_remember/serving/diff_side.py

## Governing Overview

[overview](overview.md)

## Purpose

Classifies each present diff side as text, supported media or other binary content.

## Code Commentary

An absent side stays absent. Supported media returns type and size metadata without first loading its payload. Other content is checked for binary data before text decoding. Working and committed sources keep their own selected identities.

## Relationships

Change-set JSON routes use this classification. Media bytes travel through the selected-side bytes route; metadata is not an implicit payload read.

## Evidence

- Classifies each present diff side as text, supported media or other binary content. [1]
