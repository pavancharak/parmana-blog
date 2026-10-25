---
layout: post
categories: [Operations]
title: "Part 2: The .env file and the settings that matter"
date: 2026-10-25 05:01:00 +0000
series: "Operations in practice"
series_part: 2
description: "Which settings the local .env file needs, which values each one accepts, and how production values differ from local ones."
---

This is part 2 of the series Operations in practice. Part 1 set up a clean local machine. This part covers the settings file that machine needs to run the server.

The environment file runbook lists which settings are required, the values each one accepts, and what the production values mean. Every claim in it was checked against the code.

Three places read the file, and they do not read it the same way. The runbook says which place does what, so check it before you change a setting.

## What it does not do

The file holds configuration, not secrets. Never commit it, and never paste its values into chat or a ticket.

## How we checked it

Source: [docs/runbooks/ENV-FILE.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/ENV-FILE.md).
