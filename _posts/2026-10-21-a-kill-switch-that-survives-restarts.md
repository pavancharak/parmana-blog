---
layout: post
categories: [Security, Operations]
title: "A kill switch that survives restarts"
date: 2026-10-21
description: "How Parmana's operator kill switch refuses new actions at once, keeps its state in Postgres, and is checked by a probe that runs every 15 minutes."
---

When an AI agent misbehaves, the first question is how fast you can stop it. Parmana now has an operator kill switch. This post explains what it does, what it doesn't do, and how we check it.

## What a trip does

An operator trips the switch with a reason. From then on, new execution, transaction, policy-change approval and sandbox approval requests are refused with `503 KILL_SWITCH_ACTIVE`, before any policy runs. Status, trip, reset and probe endpoints stay reachable, so the switch can always be checked and cleared.

The state lives in Postgres, not in memory. A restart does not clear a trip. If the state cannot be read, the switch counts as tripped, so a database fault fails closed.

## Two people to reset

In production, a reset needs two different operators. The first request is held as pending, and a second operator confirms it. The same operator cannot confirm their own request. A trip cancels any pending reset.

## What it does not do

We are explicit about the limits:

- A call admitted before the trip can still complete. The switch does not recall it.
- A tool that an agent calls directly, bypassing Parmana, is not stopped. Deployments must route tool calls through Parmana.
- The status response is not signed yet. It shows the switch state, but a signature tied to the running build is still open work.

## Checking the switch from outside

A GitHub Actions workflow sends a request to the production API every 15 minutes, with a key that can only probe. It records whether the refusal matched the switch state, and fails the run if they disagree. The results are kept in a table. Nothing deletes them, so the one-year minimum holds.

That is a check, not a guarantee. It shows the switch worked at the moment it ran. A schedule of checks gives ongoing evidence, which is what the probe provides.

If you run Parmana, the operations runbook covers trip, reset and probe rotation.
