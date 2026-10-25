---
layout: post
categories: [Engineering]
title: "A refusal is also a record"
date: 2026-10-23
description: "When Parmana stops an AI agent's action, it still writes a signed record of why. Here is what a refusal record holds, and why a failure to write one never blocks the refusal."
---

When a system stops an action, the record usually stops too. The request is logged as an error, or nothing is kept at all. That is a gap. If an AI agent tried to make a payment and was stopped, someone will later want to know what it asked for, which rule stopped it, and whether the check itself was sound.

Parmana keeps a record for those cases too.

## What a refusal record holds

Every decision that does not approve an action gets a refusal record. It is built from the decision itself, so it carries the same policy and signal evidence as an approval would. It records:

- the business transaction it refers to,
- the decision, including which rule stopped the request,
- the target and parameters of the action that was asked for,
- the binding violations found, if any, where the declared signals did not match the request,
- who submitted the request, when the caller identity is known,
- the hash of the policy content that was evaluated.

The record is signed, so a third party can check it later.

## A failed write does not change the refusal

Writing the record can fail. The database may be down, or the write may time out. Parmana logs the failure and carries on. The action is still refused.

This is deliberate. A refusal should not depend on its own evidence being writable. If it did, an outage in the record store could turn a refusal into an approval, or into an unclear outcome, and the action would not be stopped by the thing meant to stop it.

The trade-off is that a refusal can exist without a record, if the write fails. The failure is logged, so an operator can find those cases and look into them.

## Checking a refusal record

Anyone can check the signature on a refusal record through the public verification route, `POST /refusal/verify`. The route takes the record and checks its signature. It does not need an account, and it does not look anything up in our database. That matches how the trust record is checked: the signature is what matters, not the server that returned it.

Checking a signature does not show that the rule was the right one. It shows which rule was applied, and that the record has not been changed since it was signed.

## What this is for

Refusal records give a reviewer a way to ask why an action did not happen. They also let a team look for patterns: a rule that stops too many requests, a signal that is often missing, or an agent that keeps asking for the same thing.

The refusal record page and the verifier commands are in the [documentation](https://docs.parmanasystems.com).
