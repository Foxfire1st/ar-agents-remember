# mcp/src/agents_remember/serving/media_sources.py

## Governing Overview

[overview](overview.md)

## Purpose

Reads served media from immutable Git revisions or blob IDs.

## Code Commentary

git_media validates the revision and readable repository path before its object reads. blob_media validates the blob ID and uses the supplied path to choose the media type. Blob size is measured before payload loading. Each Git read loads the bounded blob and returns its requested slice; it does not perform a partial object-store read. Historical reads bind the object and path directly rather than following current filesystem symlinks.

## Relationships

media supplies the fixed type list, size limit and response contract. Route-specific resolvers decide which source the request is allowed to read.

## Evidence

- Reads served media from immutable Git revisions or blob IDs. [1]
