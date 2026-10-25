---
layout: post
categories: [Security]
title: "Part 3: The caller never holds the credential"
date: 2026-10-25 03:02:00 +0000
series: "Security in practice"
series_part: 3
description: "How Parmana keeps the connector credential away from the AI agent and the policy engine, and why the session credential is used once."
---

Part 3 of Security in practice. Part 2 covered the rule that refuses when unsure. This part covers what the caller is never allowed to hold.

The caller that proposes an action never holds the credential that executes it. Credential resolution happens only inside the gateway, after every gateway check has passed. The caller, the runtime, and the policy engine never see the credential a connector uses to act.

The credential is a session credential. It is issued fresh, scoped to one call, and consumed once.

This means that a compromised agent cannot reuse a credential from an earlier action, because none was ever given to it.

## What it does not do

The isolation page marks this as available as a mechanism but partial as a system-wide guarantee. Read its scope note before you assume it applies to every connector.

## How we checked it

The mechanism lives in the execution control package, and the isolation page names the packages involved.

Source: [docs/site/concepts/credential-isolation.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/concepts/credential-isolation.mdx).
