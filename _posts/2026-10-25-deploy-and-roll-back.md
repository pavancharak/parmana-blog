---
layout: post
categories: [Operations]
title: "Part 4: Deploy to production and roll back"
date: 2026-10-25 05:03:00 +0000
series: "Operations in practice"
series_part: 4
description: "How the production server is deployed, how to confirm it is healthy, and how to roll back if it is not."
---

This is part 4 of the series Operations in practice. Part 3 listed the variables a deployment needs. This part covers the deployment that uses them.

The deploy and rollback runbook describes how production is deployed, how to confirm a deployment is healthy, and how to roll back. It also points to the general production deployment guide for the wider picture.

A healthy deployment is confirmed before anyone moves on. A rollback is written down with the reason it was needed.

## What it does not do

The runbook covers the current hosting setup. If your deployment differs, the steps need adapting, and the runbook does not cover that.

## How we checked it

Source: [docs/runbooks/PRODUCTION-DEPLOY-AND-ROLLBACK.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/PRODUCTION-DEPLOY-AND-ROLLBACK.md).
