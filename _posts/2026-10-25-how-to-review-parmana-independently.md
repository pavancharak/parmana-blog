---
layout: post
categories: [Compliance]
title: "Part 5: How to have Parmana reviewed independently"
date: 2026-10-25 01:00:00 +0000
series: "From limits to proof"
series_part: 5
description: "What an independent reviewer needs to test Parmana, what the repositories already provide, and what we have not yet had reviewed."
---

This is part 5 of the series From limits to proof. Part 4 said that an independent review is the next step we want, and that our internal reviews are not an audit. This part explains what a reviewer needs, and where to find it.

## What it does

The repositories already contain the material a reviewer asks for first. Each one answers a different question:

- **What is claimed, and with what evidence.** [docs/CLAIMS.md](https://github.com/pavancharak/parmana-core/blob/main/docs/CLAIMS.md) states each claim at the scope its evidence supports, with the code and tests behind it. It also lists the claims Parmana does not make.
- **What can go wrong, and what stops it.** [THREAT-MODEL.md](https://github.com/pavancharak/parmana-core/blob/main/THREAT-MODEL.md) gives each threat its control, the evidence for that control, and the risk that remains.
- **What counts as a break.** [SECURITY-CHALLENGE.md](https://github.com/pavancharak/parmana-core/blob/main/SECURITY-CHALLENGE.md) describes what counts as breaking Parmana on a copy you run yourself, and credits every confirmed break.
- **What the verifier claims, and where to look.** [docs/SECURITY-REVIEW.md](https://github.com/pavancharak/parmana-verifier/blob/main/docs/SECURITY-REVIEW.md) in the verifier repository lists what is in scope, what is out of scope, the questions for a reviewer, and the known limits.

## What it does not do

This post does not replace a review. It does not say that a review has been done, and it does not offer one. The internal passes are recorded in the claims register, and they are not an independent audit.

It also does not say which reviewer to hire. Choose a reviewer with experience of security testing and of the AI systems you plan to use.

## How we checked it

Each document above links to the code, the tests, or the test records it relies on, so a reviewer can start from the claim and follow it to the evidence. If a reviewer finds a break, report it privately through [SECURITY.md](https://github.com/pavancharak/parmana-core/blob/main/SECURITY.md) first, not in a public issue.

## What is still open

No independent review of the whole system has been completed yet. Until one is, treat the claims as the claims we have tested ourselves, and read the gap log before you rely on any of them.
