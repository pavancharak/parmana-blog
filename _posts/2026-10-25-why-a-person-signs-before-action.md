---
layout: post
categories: [AI governance]
title: "Part 1: Why a person must sign before an agent acts"
date: 2026-10-25 04:00:00 +0000
series: "AI governance in practice"
series_part: 1
description: "The rule that no action goes ahead without a signed approval from a person, reads included, and what a refused request looks like."
---

Part 1 of AI governance in practice. It starts with the rule everything else in the series depends on: a person must approve each action first.

No action goes ahead without a signed approval from a person, reads included. A refund, a merge, a message, an update, and a read of a pull request or deal each runs only when a trusted person has signed an approval for that action, on that resource.

An approval expires, and it can be used only once. People also approve the policies before those policies can authorize anything. A refused request stays refused, and the agent sends a new request with the approval attached.

## What it does not do

Parmana does not hold a request while it waits for a person. A refused request is refused. This is a deliberate design choice, and it means a waiting queue is not part of the product.

## How we checked it

The rule is enforced in the human approval concept page, and the same rule is listed as an invariant that tests check.

Source: [docs/site/concepts/human-approval.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/concepts/human-approval.mdx).
