---
layout: post
categories: [Security]
title: "Part 6: Single-use, time-bound authorization"
date: 2026-10-25 03:05:00 +0000
series: "Security in practice"
series_part: 6
description: "What the signed authorization envelope proves, why it is single use and time bound, and what it does not prove about the business."
---

Part 6 of Security in practice. Part 5 covered the record written before release. This part covers the signed envelope that allows the release.

The authorization is a signed envelope. It is proof that Parmana authorized one specific execution request. It is single use, time bound, and bound to the content it was issued for.

The gateway checks the envelope again before it releases anything. A reused, expired, or altered envelope is refused.

## What it does not do

The envelope proves that Parmana authorized the request. It does not prove that the request was correct for the business. That is the job of business validation, covered in the AI governance series.

## How we checked it

The envelope signer and verifier are named in the concept page, with the source files listed.

Source: [docs/site/concepts/execution-authorization.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/concepts/execution-authorization.mdx).
