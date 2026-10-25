---
layout: post
categories: [AI governance]
title: "Part 2: Policies are versioned files"
date: 2026-10-25 04:01:00 +0000
series: "AI governance in practice"
series_part: 2
description: "Why each policy version is kept as a separate file, how the engine reads the rules in order, and why a request that matches nothing is refused."
---

Part 2 of AI governance in practice. Part 1 explained why a person must sign. This part explains what the signed approval is checked against: the policy.

A policy lives in the repository as a versioned file. The customer refund policy, for example, has three versions, each in its own folder. A new version is a new folder, so the old decisions can still be explained.

The engine checks rules in order, the first match decides, and a request that matches no rule is refused. Every approve rule must require an approval signal, so a policy cannot approve on the agent's word.

## What it does not do

The files show what a policy says. They do not show whether it is the right policy for your business. That review belongs to the people who own the policy.

## How we checked it

The engine rules are stated in the policy concept page, and the policy package has unit tests.

## What is still open

Each version needs a review before it is used. The next part covers how that review is recorded.
