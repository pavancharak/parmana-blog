---
layout: post
categories: [AI governance]
title: "Part 6: Business facts come from the system that owns them"
date: 2026-10-25 04:05:00 +0000
series: "AI governance in practice"
series_part: 6
description: "Why an agent's claim about a business fact is not treated as fact, and how the policy asks the system that owns the fact."
---

Part 6 of AI governance in practice. Part 5 covered grants, which limit what an agent may do. This part covers the facts an agent uses to justify an action.

An agent proposes an action, and it also proposes the facts that justify it. A fact such as eligibility for a refund is the agent's claim, not a business fact.

Parmana answers two questions separately: may this kind of action be decided here at all, and is this exact action valid for this exact business object according to the system that owns the facts. An action runs only when both hold.

## What it does not do

This check depends on the owning system being correct. If that system holds wrong data, the check will accept it.

## How we checked it

The concept page names the statuses for authority, validity and execution, and how a trusted signal is recorded.

## What is still open

Each business system needs to be connected before a policy can rely on its facts.
