---
layout: post
categories: [Engineering]
title: "Map the packages before you change anything"
date: 2026-10-25 02:00:00 +0000
series: "Working on Parmana"
series_part: 2
description: "A map of Parmana's packages, what each one owns, and the ownership rules the build enforces, so you know where a change belongs before you make it."
---

This is part 2 of the series Working on Parmana. Part 1 got a clean checkout building and testing. This part explains what is in the repository, so you know where to look before you change anything.

## What it does

The repository is an npm workspaces monorepo. Everything under `packages/` is built and tested on its own, and the packages depend on each other in one direction. The main ones are:

| Package | What it owns |
| ------- | ------------ |
| `@parmana/shared` | The core types, such as the business transaction and the trust record. It holds contracts, not behavior. |
| `@parmana/crypto` | Signing, verifying and hashing. |
| `@parmana/policy` | The policy engine. It turns signals and rules into an approve or reject decision. |
| `@parmana/runtime` | Orchestrates the pipeline: policy, signal checks, authorization, then the call to execution. |
| `@parmana/execution-control` | Credentials and the controlled path to a connector. |
| `@parmana/execution-gateway` | The only owner of production execution. |
| `@parmana/connector-sdk` and `@parmana/connector-hubspot` | Connector contracts and connector definitions. They perform no production execution. |
| `@parmana/api` | The HTTP server. It wires the packages together, and its routes never run a business action directly. |

Three ownership rules matter most. Only `execution-gateway` may implement the connector interface. Connector packages own no production execution. API routes and bootstrap code never execute a business action directly. The build checks these rules on every change.

## What it does not do

This is a map, not a reference. Read the code for the exact behavior of each package. The package list can change, so check the architecture document for the current version.

## How we checked it

The ownership rules are written down as numbered invariants in [repository-invariants.md](https://github.com/pavancharak/parmana-core/blob/main/docs/architecture/repository-invariants.md), and each one names the test that enforces it. You can run the repository-level checks on their own:

```bash
npx vitest run tests/architecture/execution-boundary.test.ts
```

## What is still open

The system architecture document says it was verified against the source at a named phase. Compare its date with the code you are reading, and treat any difference as a reason to look again.
