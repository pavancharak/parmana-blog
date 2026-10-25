---
layout: post
categories: [Engineering]
title: "Follow one request through the code"
date: 2026-10-25 02:10:00 +0000
series: "Working on Parmana"
series_part: 3
description: "Trace one execution request from the HTTP route to the business system and the signed record, stage by stage, so you can read and change the pipeline with confidence."
---

This is part 3 of the series Working on Parmana. Part 2 mapped the packages. This part follows a single request through them, from the HTTP route to the business system and the signed record. Once you can trace one request, you can read the rest of the code.

## What it does

An execution request enters through the route in `packages/api/src/routes/`. The request then passes through these stages, in this order:

1. **The application layer** (`ExecutionTrustApplication`) receives the request and hands it to the runtime.
2. **The runtime** (`RuntimeEngine`) evaluates the policy, checks the signals, and signs the authorization. A request that is not approved stops here.
3. **The pipeline** runs the trust chain checks, then the execution step.
4. **The execution system** is the seam the pipeline calls. The gateway implements it.
5. **The gateway** (`ExecutionGateway`) verifies the signed envelope, then calls the execution control service.
6. **Execution control** resolves a short-lived credential for the call, and passes the request to the connector adapter.
7. **The adapter** calls the business system.
8. **The trust record** is built from the result and signed.

The exact chain, with the file for each stage, is in [the execution pipeline section](https://github.com/pavancharak/parmana-core/blob/main/docs/architecture/system-architecture.md). Read the stages in that order, and check each handoff in the code.

## What it does not do

This post describes the shape of the pipeline, not every branch in it. Failure paths, such as a missing configuration or a failed check, refuse at the stage where they fail. Read those paths in the code, and in the tests, before you rely on them.

## How we checked it

The order of these stages is enforced by tests in the repository. A change that sends a request around the gateway fails the boundary test, so you will know early if a change breaks the path.

```bash
npx vitest run tests/architecture/execution-boundary.test.ts
```

## What is still open

The pipeline above is the production path. Some test helpers and examples use shorter paths, so a test that passes does not always exercise the full chain. Check which path a test uses before you rely on its result.
