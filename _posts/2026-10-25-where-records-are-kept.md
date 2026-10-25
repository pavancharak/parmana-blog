---
layout: post
categories: [Compliance]
title: "Part 3: Where the records are kept"
date: 2026-10-25 05:12:00 +0000
series: "Compliance in practice"
series_part: 3
description: "How the storage layer keeps records, the schema behind them, and what it means for a team that runs the server itself."
---

This is part 3 of the series Compliance in practice. Part 2 covered the four verification checks. This part covers where the records those checks read are stored.

The storage overview describes the repositories that keep each kind of record, and the schema reference lists the fields in each one.

Knowing where a record lives tells you where to back it up and who can read it.

## What it does not do

The storage pages describe the design. They do not set your retention period or your backup schedule, which are your decisions.

## How we checked it

Source: [docs/site/storage/overview.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/storage/overview.mdx).
