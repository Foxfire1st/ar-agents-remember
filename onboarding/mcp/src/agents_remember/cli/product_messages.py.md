# mcp/src/agents_remember/cli/product_messages.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

Sends notices under the fixed Agents Remember product identity.

## Code Commentary

The operation resolves the recipient by task references, checks the task message limit and files the message before delivery. It uses the standard hold route for a recipient whose start is incomplete when the workspace is known.

## Evidence


- The sender uses the shared filing, delivery and hold steps with the product identity. [1]
