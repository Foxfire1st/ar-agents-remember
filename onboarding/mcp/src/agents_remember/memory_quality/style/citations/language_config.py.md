# mcp/src/agents_remember/memory_quality/style/citations/language_config.py

## Governing Overview

[Memory quality](../../overview.md)

## Purpose

Load, validate, and merge repository-root `languages.json` and user-settings `languages` overrides into immutable `LanguageOverrides` and `CustomLanguageSpec` records while enforcing the local-only security boundary.

## Code Commentary

`load_language_overrides` reads optional user defaults (`_load_user_languages_block` from `settings.json` under the `languages` key) and optional repository overrides (`load_repo_languages_file` from `<repo>/languages.json`), merging them with `_merge_overrides` so repository declarations take precedence over user defaults.

`parse_language_overrides` strictly validates top-level keys (`globs`, `suffixes`, `enable`, `disable`, `custom`) and custom-language keys (`id`, `suffixes`, `globs`, `libraryPath`, `symbol`, `tagsQueryPath`, `testsQueryPath`, `wrappers`, `destructuring`). `_refuse_unknown_and_url_keys` and `_refuse_remote_url` enforce the security boundary: any unknown key, forbidden URL key (`url`, `downloadUrl`, `wheelUrl`, `remoteUrl`, `sourceUrl`), or remote URL scheme (`scheme://` or `//`) in `libraryPath`, `tagsQueryPath`, or `testsQueryPath` raises `LanguageConfigError` (defined here as an `AgentsRememberError` subclass). Custom languages must supply existing local filesystem paths resolved relative to the repository/config base directory (`_resolve_local_path`).

`_refuse_reserved_suffix` and `_refuse_reserved_glob` protect `.lean` (and any catalog-reserved suffix) from being claimed by `suffixes`, `globs`, or custom language selectors. `_parse_custom_selectors` requires at least one suffix or glob per custom language, validates lowercase dot-prefixed suffixes and glob syntax, and parses optional `wrappers` and `DestructuringSpec` rules.

## Relationships

`language_scanner.py` calls `load_language_overrides` when building repository-scoped `LanguageSet` instances and validates that `enable`/`disable`/`suffixes`/`globs` reference known catalog or custom IDs and that custom IDs do not shadow catalog entries. `errors.py` defines the base `AgentsRememberError`. `language_set.py` owns `RESERVED_SUFFIXES`.

## Evidence

- `CustomLanguageSpec` and `LanguageOverrides` hold immutable parsed custom-language definitions and enable/disable/suffix override maps. [1]
- `load_language_overrides`, `load_repo_languages_file`, and `parse_language_overrides` read user and repository config files and merge repository precedence over user defaults. [2]
- `_refuse_unknown_and_url_keys` and `_refuse_remote_url` reject unknown fields, forbidden URL keys, and remote URLs in `languages.json` and user settings. [3]
- `_refuse_reserved_suffix` and `_refuse_reserved_glob` prevent overrides or custom languages from claiming reserved suffixes such as `.lean`. [4]
- `_parse_one_custom_language` resolves local library and query paths and validates selectors, wrappers, and destructuring rules. [5]
