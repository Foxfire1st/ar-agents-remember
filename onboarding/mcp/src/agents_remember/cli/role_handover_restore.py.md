# mcp/src/agents_remember/cli/role_handover_restore.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Restores a saved launch's hand-over files before its first message is sent again, from the receipt alone, and puts every refusal in one type the three callers already understand.

## Code Commentary

restore_launch_files checks every reference and every target before the first byte is written, so a refusal leaves the receipt and all its files exactly as they were and says what has to be put right. A missing request locator is rebuilt at the folder the receipt recorded by the artifact check before the frozen instruction details are validated. The validation therefore sees the same locator the launch published, and an altered or rebound detail still refuses before either file is restored. HandoverFileRefusal is a ValueError on purpose: the held-seat opener turns a ValueError into a plain cannot-open answer and releases its delivery claim, so a refusal type it did not know would escape the opener and keep the claim. The retry route turns the same type into its 409 answer, while an unrelated refusal stays what it was. saved_handover_file reads the receipt's recorded reference for one path and reports nothing when the receipt holds none, which is how a launch from before the second file keeps its old rules.

## Evidence

- Every refusal of a saved launch's files is one ValueError the held opener and the retry route both recognise. [1]

- The saved launch's files are restored together, checked before the first write. [2]

- A receipt without the second file's reference reports none rather than inventing one. [3]
