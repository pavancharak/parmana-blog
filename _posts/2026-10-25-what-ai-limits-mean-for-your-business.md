---
layout: post
categories: [Product]
title: "What AI spending limits mean for your business"
date: 2026-10-25
description: "A plain guide for business leaders on why AI needs limits outside the AI, who approves what, and how to know an action was allowed."
---

Your business is starting to let AI systems do real work: issue refunds, pay suppliers, update customer records. That saves time, and it also means a mistake can cost money or harm a customer in minutes. This post is for leaders who need to decide how much control to keep, and what proof to ask for.

## Why a rule in the prompt is not enough

Many teams tell an AI system the rules in plain words, for example "only refund up to $500." That is a request, not a control. The system can misread it, or someone can persuade it to ignore it. A limit is only real when something outside the AI checks every action against it before the action happens.

## What it does

Parmana sits between the AI and your business systems. Think of it like a card network that approves a purchase before the shop receives the money. Each action follows the same steps:

- **You set the limits.** For example, refunds up to $200, set by Finance.
- **Each action is checked.** A request that fits the limit goes ahead. A request that does not fit is refused.
- **A person approves exceptions.** If an action needs sign-off, a named person approves it, and the approval is signed.
- **Every decision leaves a record.** The record shows who or what asked, what was checked, what was allowed, and what happened.

## What it does not do

- It does not decide whether your limits are the right ones. That remains your decision.
- It does not check the business systems themselves. If a connected system is wrong, Parmana does not fix it.
- It does not replace your own controls, audit, or legal review.

## How we checked it

We run an automated set of attack scenarios against the system and check whether each one is blocked. The results are described in the [evaluation guide](https://github.com/pavancharak/parmana-core/blob/main/EVALUATION.md). You can read the same report yourself, or ask your technical team to run it.

## What is still open

We are still working out how these limits apply across every kind of business system. If your process is unusual, talk to us before you rely on it.

If you want to see a refusal and an approval in practice, the [playground](https://docs.parmanasystems.com/playground) runs a live example with no installation.
