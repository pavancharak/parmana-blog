---
layout: post
categories: [Compliance]
title: "Part 7: Keep the evidence inside your network"
date: 2026-10-25 05:16:00 +0000
series: "Compliance in practice"
series_part: 7
description: "What a self-hosted Parmana keeps in your own deployment: decisions, signatures, the audit trail and the trust records."
---

This is part 7 of the series Compliance in practice. Part 6 covered replaying a past decision. This part covers where the evidence lives when you run Parmana yourself.

A self-hosted deployment runs the same server as the hosted API. Decisions, signatures, the audit trail, and the trust records stay in your deployment.

This matters when a regulator or your own policy says the evidence must not leave your network.

## What it does not do

Self-hosting moves where the evidence lives. It does not make your own deployment secure, and you still need your own controls.

## How we checked it

Source: [docs/site/self-hosted/overview.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/self-hosted/overview.mdx).
