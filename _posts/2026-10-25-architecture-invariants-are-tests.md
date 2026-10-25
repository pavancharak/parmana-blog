---
layout: post
categories: [Engineering]
title: "Part 10: Architecture rules that are tests"
date: 2026-10-25 05:33:00 +0000
series: "Working on Parmana"
series_part: 10
description: "How the repository's architectural rules are written as numbered invariants, and each one is enforced by a named test."
---

This is part 10, the last part of Working on Parmana. Part 9 covered keeping claims in step with the code. This part covers the architectural rules the build enforces.

The repository invariants list each architectural rule as a numbered invariant, with the test that enforces it. Examples include that only the gateway may implement the connector interface, and that API routes never execute an action directly.

Run the invariant tests with the rest of the suite. A change that breaks a rule fails the build.

## What it does not do

The invariants cover the rules that were written down. A rule that is not listed is not enforced by these tests.

## How we checked it

Source: [docs/architecture/repository-invariants.md](https://github.com/pavancharak/parmana-core/blob/main/docs/architecture/repository-invariants.md).
