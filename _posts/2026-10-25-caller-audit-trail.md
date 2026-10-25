---
layout: post
categories: [Compliance]
title: "Part 5: The audit trail of who called"
date: 2026-10-25 05:14:00 +0000
series: "Compliance in practice"
series_part: 5
description: "Why each caller authentication event is recorded, signed and chained, so a deleted event would show."
---

This is part 5 of the series Compliance in practice. Part 4 covered finding actions with no record. This part covers the record of who asked, before any decision is made.

Each caller authentication event, whether it succeeds, is denied, or is rejected for its structure, is recorded. Each event is signed and chained to the caller's earlier events.

Because each event links to the one before it, a deleted event breaks the chain.

## What it does not do

The trail shows who attempted a call. It does not show that the person behind the key was the person they claimed to be.

## How we checked it

Source: [docs/site/concepts/caller-audit-trail.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/concepts/caller-audit-trail.mdx).
