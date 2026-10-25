---
layout: post
categories: [Product]
title: "Part 3: Self-hosted or hosted"
date: 2026-10-25 05:22:00 +0000
series: "Product in practice"
series_part: 3
description: "What running Parmana on your own infrastructure involves, what it needs, and what it does not do, compared with the hosted API."
---

This is part 3 of the series Product in practice. Part 2 helped you choose a path. This part covers the choice between running Parmana yourself and using the hosted service.

Self-hosted Parmana is the same server as the hosted API. It is packaged to run on your own infrastructure with one command.

Decisions, signatures, the audit trail, and the trust records stay in your deployment. Nothing is sent to Parmana.

## What it does not do

Self-hosting takes on operating work: keeping the server, the database, and the keys running. The self-hosted page lists what it does not do.

## How we checked it

Source: [docs/site/self-hosted/overview.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/self-hosted/overview.mdx).
