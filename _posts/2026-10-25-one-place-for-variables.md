---
layout: post
categories: [Operations]
title: "Part 3: Find every environment variable in one place"
date: 2026-10-25 05:02:00 +0000
series: "Operations in practice"
series_part: 3
description: "Where to look up each environment variable the server reads, whether it is required, and what it does."
---

This is part 3 of the series Operations in practice. Part 2 explained the settings file. This part gives the full list those settings come from.

The environment variable reference is the single list of variables the server reads. For each one it says whether the variable is required, what the default is, and what the variable does.

Use the reference when a setting is missing, rather than searching the code. It is the list the team checks against.

## What it does not do

The reference describes what each variable does. It does not tell you what value your environment should use, which depends on your deployment.

## How we checked it

Source: [docs/runbooks/ENV-VARIABLE-REFERENCE.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/ENV-VARIABLE-REFERENCE.md).
