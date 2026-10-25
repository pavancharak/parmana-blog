---
layout: post
categories: [Compliance]
title: "Part 6: Replay a past decision"
date: 2026-10-25 05:15:00 +0000
series: "Compliance in practice"
series_part: 6
description: "How replay rebuilds a past execution from its trust record, so a reviewer can see what the system would have decided."
---

This is part 6 of the series Compliance in practice. Part 5 covered the trail of callers. This part covers rebuilding a past decision from its record.

Replay reconstructs a past execution from its trust record. A reviewer can see the decision that was made, and check it against the same inputs.

The replay overview explains the steps and what each one checks.

## What it does not do

Replay reproduces a decision from its record. It does not prove the policy that made the decision was correct.

## How we checked it

Source: [docs/site/replay/overview.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/replay/overview.mdx).
