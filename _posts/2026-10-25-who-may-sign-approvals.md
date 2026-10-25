---
layout: post
categories: [Security]
title: "Part 9: Who may sign an approval"
date: 2026-10-25 03:08:00 +0000
series: "Security in practice"
series_part: 9
description: "How trusted approval issuers are listed in the code and a fallback key file, and how an issuer is revoked when a key should no longer be trusted."
---

Part 9 of Security in practice. Part 8 covered rotating the keys that callers use. This part covers the keys that approvers use to sign.

An approval is trusted only when it is signed by an issuer that Parmana trusts. The trusted issuers come from two sources, in order: the reviewed list in code, and a key file as a fallback.

Each entry in the code names the approver, the key, the public key, and whether the key has been revoked. A revoked issuer's approvals are no longer accepted.

## What it does not do

Parmana does not decide who should be an approver. That is a business decision, and the runbook only describes how a decision is recorded.

## How we checked it

The runbook names the code file where the issuers are listed, and it separates policy-change checkers from approval issuers.

## What is still open

The runbook lists what is still open for approval issuers. Read that section before you add or revoke one.
