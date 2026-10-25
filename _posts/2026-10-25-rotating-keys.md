---
layout: post
categories: [Security]
title: "Part 8: Rotate keys without losing access"
date: 2026-10-25 03:07:00 +0000
series: "Security in practice"
series_part: 8
description: "How caller keys are stored and replaced in production, so access continues during a rotation and an old key does not stay live."
---

Part 8 of Security in practice. Part 7 covered stopping new actions. This part covers replacing the keys that let callers act in the first place.

Each caller key is one entry in the production caller list. The entry stores only a hash of the key, never the key itself.

The rotation runbook describes how to replace a key, a step-up key, or the whole caller list without losing access and without leaving an old key live.

## What it does not do

The runbook is the procedure. This post does not repeat its steps, and it contains no key values.

## How we checked it

The runbook names the scripts and bootstrap code it was written from, so you can check it against the code.

## What is still open

Rotation needs a second person to confirm access still works. Keep the runbook's checks in your own process.
