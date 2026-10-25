---
layout: post
categories: [Operations]
title: "Part 10: Read the runbooks in the right order"
date: 2026-10-25 05:09:00 +0000
series: "Operations in practice"
series_part: 10
description: "How the runbook index routes each problem to the right runbook, and why the rules in the index apply to every runbook."
---

This is part 10, the last part of Operations in practice. Part 9 covered creating operator credentials. This part shows how to find the right runbook for any problem.

The runbook index has a table that sends each problem to one runbook, for example a production error to the troubleshooting runbook.

The index also states the rules that apply to every runbook. Read those rules before you open any of them.

## What it does not do

The index routes you. It does not replace the runbook, and a runbook can change without the index changing.

## How we checked it

Source: [docs/runbooks/README.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/README.md).
