---
layout: post
categories: [Engineering]
title: "Part 7: Write tests that prove a control works"
date: 2026-10-25 05:30:00 +0000
series: "Working on Parmana"
series_part: 7
description: "Why a passing test is not enough for a security control, and how mutation testing checks that the tests would catch a broken control."
---

This is part 7 of the series Working on Parmana. Part 6 covered the checks a change must pass before release. This part covers whether those tests would notice a broken control.

Mutation testing breaks the security code on purpose, one change at a time, and runs the tests against each change. A change the tests catch is caught, and a change they miss survives.

A high score shows that the tests notice the mutations that were tried, which tells you where the tests are strong and where they are not.

## What it does not do

A mutation score is not a proof of correctness. It measures the tests against the changes that were made, not against every possible bug.

## How we checked it

Source: [docs/MUTATION-TESTING.md](https://github.com/pavancharak/parmana-core/blob/main/docs/MUTATION-TESTING.md).
