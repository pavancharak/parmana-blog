---
layout: post
categories: [Engineering]
title: "Part 9: Keep the claims in step with the code"
date: 2026-10-25 05:32:00 +0000
series: "Working on Parmana"
series_part: 9
description: "Why the claims register changes in the same pull request as the code, and how a claim is written in the present tense only when the tests back it."
---

This is part 9 of the series Working on Parmana. Part 8 covered fuzz testing. This part covers the record of what the system claims, and how it stays accurate.

The claims register states each claim at the scope its evidence supports. A claim is written in the present tense only when code and tests back it.

When a change alters a claim, the register changes in the same pull request. The contribution rules require it.

## What it does not do

The register lists what is claimed. It does not check that the claims are important, or that the tests are complete.

## How we checked it

Source: [docs/CLAIMS.md](https://github.com/pavancharak/parmana-core/blob/main/docs/CLAIMS.md).
