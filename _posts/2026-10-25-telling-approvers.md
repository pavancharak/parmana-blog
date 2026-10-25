---
layout: post
categories: [AI governance]
title: "Part 8: Tell the approver when their signature is needed"
date: 2026-10-25 04:07:00 +0000
series: "AI governance in practice"
series_part: 8
description: "How approval notifications reach the person who must sign, by email or by a signed webhook, when a request is refused for lack of approval."
---

Part 8 of AI governance in practice. Part 7 covered the evidence left by a refusal. This part covers how the person who must approve learns that a request is waiting.

When a request is refused only because it needs a person's approval, Parmana can tell the approver right away. The approver gets exactly what they need to sign.

Notifications can go by email, or by a signed webhook to your own system, or both.

## What it does not do

A notification approves nothing. The approver still signs the approval themselves, and the agent must send a new request with it attached.

## How we checked it

The guide lists the settings for each channel, so you can check the configuration against it.

Source: [docs/site/guides/approval-notifications.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/guides/approval-notifications.mdx).
