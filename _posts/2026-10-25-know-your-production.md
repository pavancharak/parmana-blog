---
layout: post
categories: [Operations]
title: "Part 5: Know what runs in production"
date: 2026-10-25 05:04:00 +0000
series: "Operations in practice"
series_part: 5
description: "What the production environment consists of, which settings are live, and where each one is set, so you can answer an incident question quickly."
---

This is part 5 of the series Operations in practice. Part 4 covered deploying and rolling back. This part describes what a deployment is made of, so you know what to check.

The production environment runbook lists the live settings, where each is set, and what each one controls. Keeping this list current is part of operating the system.

When something changes, update the list in the same change, so the next person does not work from an old picture.

## What it does not do

The runbook does not hold secret values, and it must not. It describes where settings live, not what they contain.

## How we checked it

Source: [docs/runbooks/PRODUCTION-ENVIRONMENT.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/PRODUCTION-ENVIRONMENT.md).
