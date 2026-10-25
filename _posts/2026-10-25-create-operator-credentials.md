---
layout: post
categories: [Operations]
title: "Part 9: Create operator credentials safely"
date: 2026-10-25 05:08:00 +0000
series: "Operations in practice"
series_part: 9
description: "The step-by-step procedure for creating maker, checker and operator credentials, and the rules that keep keys out of chat and tickets."
---

This is part 9 of the series Operations in practice. Part 8 covered keeping the advisory record current. This part covers creating the credentials that operators use.

The credential procedure creates the maker, checker and operator credentials, updates the live key list, redeploys, and verifies each caller.

It states the rules first: no key, token, or database address goes into chat, email, a ticket, or a commit. Follow those rules before any step.

## What it does not do

The procedure does not cover how to store the credentials after they are created. Your secrets store needs its own controls.

## How we checked it

Source: [docs/runbooks/CREDENTIAL-CEREMONY.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/CREDENTIAL-CEREMONY.md).
