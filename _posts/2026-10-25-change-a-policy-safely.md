---
layout: post
categories: [Engineering]
title: "Part 4: Change a policy safely"
date: 2026-10-25 02:20:00 +0000
series: "Working on Parmana"
series_part: 4
description: "How to write a new version of a policy, test it, and move it through approval, without changing what a live decision means."
---

This is part 4 of the series Working on Parmana. Part 3 followed a request through the code, and the policy decision is the step where that request is approved or refused. This part shows how to change a policy without changing its decisions in ways nobody reviewed.

## What it does

Policies live in the repository as versioned files. Each version is a folder, with the policy file inside it. The customer refund policy, for example, has three versions:

```
policies/customer-refund/1.0.0/policy.json
policies/customer-refund/1.1.0/policy.json
policies/customer-refund/1.2.0/policy.json
```

The engine evaluates a policy in a fixed way. Rules are checked in order, the first match decides, and a request that matches no rule is refused. Every approve rule must require an approval signal, so the policy cannot approve on the agent's word. The policy validator refuses to load or accept a policy that breaks this rule.

To change a policy, write a new version rather than editing an old one. Keep the old version, so that past decisions can still be explained against the rules that made them.

## What it does not do

This post does not show how a change is approved, and it does not change a live policy. Approval is a separate step, handled by policy governance under a maker and checker, and the guide for it is linked below. Do not treat a passing test as approval.

## How we checked it

The policy engine has unit tests in `packages/policy/tests/unit`. Run them after any change to a policy or to the engine:

```bash
npx vitest run packages/policy
```

Then check the outcome on the cases that matter: a request that should be approved, one that should be refused, and one that falls outside every rule. The [policy governance guide](https://docs.parmanasystems.com/guides/policy-governance-maker-checker) describes how a changed policy is proposed, reviewed and approved.

## What is still open

The tests check the engine and the policy file's structure. They do not check whether the rules express the business's intent. That check belongs to the person who owns the policy, and to the review that approves it.
