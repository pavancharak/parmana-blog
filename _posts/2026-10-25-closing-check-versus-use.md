---
layout: post
categories: [Security]
title: "Part 4: Closing the gap between check and use"
date: 2026-10-25 03:03:00 +0000
series: "Security in practice"
series_part: 4
description: "How Parmana makes sure the payload that runs is the payload that was approved, by recomputing its hash before release."
---

Part 4 of Security in practice. Part 3 showed what the caller never holds. This part covers the gap between approving an action and running it.

A system that authorizes a payload and then runs a different payload under the same authorization has a check-versus-use gap. Parmana closes it with content binding: the gateway recomputes the hash of the content it is about to release and compares it with the hash that was authorized.

The default server builds a real gateway, so every execute request gets this comparison. The gap closed by this mechanism is the one described in the content binding page.

## What it does not do

The page sets out what the mechanism covers and what it does not. Read that section before relying on the binding for a case the page does not name.

## How we checked it

The binding is wired into the server bootstrap, which builds the gateway unconditionally.

Source: [docs/site/concepts/content-binding-toctou.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/concepts/content-binding-toctou.mdx).
