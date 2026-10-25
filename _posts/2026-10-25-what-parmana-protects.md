---
layout: post
categories: [Security]
title: "Part 1: What Parmana protects, and from whom"
date: 2026-10-25 03:00:00 +0000
series: "Security in practice"
series_part: 1
description: "The scope of Parmana's threat model: what is protected, the threats it names, and the residual risk that remains after each control."
---

This is the first part of the series Security in practice. It starts with the scope every later part depends on.

Security claims are only useful when they say what they cover. Parmana's threat model is the document that does that. It states what Parmana protects, from whom, how, and what stays exposed.

Each threat in the model names the control that addresses it, the evidence for that control, and the residual risk. The evidence is either an attack scenario you can run, or a claim in the claims register, cited by section number.

The model lists the in-scope parts of the system: the API, the runtime that evaluates policy and signs authorizations, the execution gateway, the built-in connectors, policy and approver governance, and the records the system signs.

## What it does not do

The threat model does not remove the residual risks it lists. Read each threat with its residual risk, not as a promise that the control covers everything around it.

## How we checked it

The model was reviewed against the main branch on 2026-10-10, and it must change in the same pull request as any claim, enforcement point, or attacker capability that changes. Each attack scenario can be run with npm run evaluate.

## What is still open

The model is a snapshot. Check its review date against the code you are reading.
