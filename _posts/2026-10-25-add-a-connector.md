---
layout: post
categories: [Engineering]
title: "Part 5: Add a connector, one step at a time"
date: 2026-10-25 02:30:00 +0000
series: "Working on Parmana"
series_part: 5
description: "The order to build a connector, from the policy to the live tests, and the checks that show a denied request never reaches the business system."
---

This is part 5 of the series Working on Parmana. Part 4 covered the policy, which every connector depends on. This part adds a connector, which performs the real action once a request is approved, and builds it in the order the repository expects.

## What it does

A connector needs four pieces. Only the first three are always required:

1. **A policy** bound to the capability, which decides whether a request is allowed.
2. **A caller with a scoped key**, which says who may ask.
3. **A connector**, which performs the action once it is approved.
4. **A signal verifier**, only when a false claim about the real world is a real risk.

Build them in that order. Once the policy and a caller key exist, you can test authorization before any connector code is written. An approved request with no connector returns `503 CONNECTOR_NOT_REGISTERED`, and that is expected at this stage. It shows that authorization works and that execution is not connected yet.

The code is split in two. A passive package, `packages/connector-<name>/`, holds the contracts and definitions, and performs no calls. The adapter, a `Gateway*Adapter` in `packages/execution-gateway/src/connector-execution/`, is the only code that performs the call. The adapter is wired in the bootstrap code under `packages/api/src/bootstrap/`.

## What it does not do

This post does not set up live credentials, and it does not cover the signal verifier in depth. Live tests run only when they are explicitly enabled, and they need a test credential that you supply.

## How we checked it

Write the tests in the order the connector guide gives:

1. **Hermetic tests** against a mock server, with no network access. They cover the policy, the adapter's guards, and failures, which must fail closed.
2. **A denied request makes zero calls.** Check this at the adapter and at the HTTP boundary.
3. **A gated live suite**, last, that runs only when the live flag is set. Prefer a reversible action, so the suite can be run again.

Do not re-test credential isolation for each connector. The execution control package already tests it for every connector.

```bash
npx vitest run packages/execution-gateway
```

## What is still open

Each new connector is a new record of what Parmana can claim. Update the claims register for the connector before you merge, so the record matches what the tests now prove.
