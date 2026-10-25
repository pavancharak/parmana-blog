---
layout: post
categories: [Security]
title: "Part 2: Fail closed: refuse when you are not sure"
date: 2026-10-25 03:01:00 +0000
series: "Security in practice"
series_part: 2
description: "Why Parmana refuses when a check fails, a connector is missing, or a dependency is down, instead of quietly letting the action through."
---

Part 2 of Security in practice. Part 1 set out what Parmana protects and from whom. This part explains the rule that decides what happens when something goes wrong.

The contribution rules state the principle plainly: missing configuration, a failed check, or an unavailable dependency refuses. It never degrades silently into an allowed action.

The glossary applies the same rule to decisions. If no rule matches, the request is denied. If a connector is missing, the request is denied. If a check fails, the request is denied. There is no default-allow path.

In practice a refusal can look like a 503 error. For example, an approved request with no connector registered returns CONNECTOR_NOT_REGISTERED at dispatch, which is the expected result before a connector is built.

## What it does not do

Fail closed does not make the system always available. A correct refusal can block legitimate work, and the team must fix the missing piece to let it through.

## How we checked it

The principle is stated in the contribution rules and applied in the glossary. The connector behavior is described in the connector build guide, which lists what each missing piece produces.

Source: [CONTRIBUTING.md](https://github.com/pavancharak/parmana-core/blob/main/CONTRIBUTING.md).
