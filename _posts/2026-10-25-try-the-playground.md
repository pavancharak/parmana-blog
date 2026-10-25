---
layout: post
categories: [Product]
title: "Part 1: Try Parmana in the playground"
date: 2026-10-25 05:20:00 +0000
series: "Product in practice"
series_part: 1
description: "What the public playground shows in one sitting: a refusal, a signed approval, a release, and an offline check, with no install."
---

This is part 1 of the series Product in practice. It is the easiest place to see the product work before you read anything else.

The playground is a live server you can call now. It runs the same code as production, with its own database, signing keys, and approver.

Its one action is released to an endpoint that does nothing, and answers with a receipt. You see the policy, the approval, the signed release, and a record you can check yourself.

## What it does not do

The playground is a demonstration. It uses a published demo key and does not stand in for your own deployment.

## How we checked it

Source: [docs/site/playground.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/playground.mdx).
