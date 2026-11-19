# mcp/src/agents_remember/package_data/paseo_host/contract.json

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The release-owned host contract specifies the exact host package version and the Node release, archive URL and SHA-256 for linux-x64. See the [Node pin history](#node-pin-history) for the dated selection and checksum recheck.

## Code Commentary

`paseo_host_contract.py` loads this file for its consumers. The release concordance script checks agreement between the host manifest, lock root, host lock entry and plugin SDK pin. It also requires a version, integrity field and HTTPS resolution for each locked package. For Node, it requires only the linux-x64 platform, the canonical release archive URL and a 64-character lowercase hexadecimal digest. The Node provisioner separately hashes the downloaded archive and refuses a mismatch before extraction.


## Node pin history

MIK-R107 v1 rule 1 chose the newest Node 26.x.y release listed on the build day and required the official archive URL and SHA-256. On 2026-10-08 the selection was Node 26.11.1. The build-day code record is `3f6829878ba8457761c6fe8886f050f232cc892c:mcp/src/agents_remember/package_data/paseo_host/contract.json`.

The 2026-10-28 06:12 UTC recheck recorded that the release index then listed 26.12.1 and that the official 26.11.1 checksum still matched the pinned archive. The dated memory record is `dec52b25e9fdc73a1ec41e609d7f0cea883d2fba:onboarding/mcp/src/agents_remember/package_data/paseo_host/contract.json.md`, with its paired `contract.json.json` references [2] and [3]. The archived index, checksum and independent review evidence are catalogued in `notes/reports/curator/97d24f38-ebc1-43f7-a5bf-9acba9c46b14/role-launch/W6-M567-node-pin-provenance.md` (SHA-256 `a33e1329ddb6fb3f0cb92421f1f987376d999f3fd5ddc576cd1a5f0137a3020e`).

## Evidence



- The contract selects `@getpaseo/cli` 0.16.2 and Node 26.11.1 for linux-x64. [1]


- Official Node v26.11.1 distribution checksums identify the linux-x64 archive digest. The 2026-10-28 06:12 UTC recheck records 3883bfc73f9a680ca4eab04b196068aaaab1373ffa77d8fc1a4408222495b651 for node-v26.11.1-linux-x64.tar.xz, which matches the pinned digest. [2]

- The dated release-index recheck recorded 26.11.1 as the 2026-10-08 build-day selection and 26.12.1 as the latest 26.x release at the 2026-10-28 06:12 UTC recheck. [3]
- Release concordance checks the package and lock pins, the sole supported platform, the canonical archive URL and the configured digest format. [4]
- The Node provisioner computes SHA-256 from the downloaded archive and rejects a mismatch before opening it for extraction. [5]
