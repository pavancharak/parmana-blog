---
layout: post
categories: [AI governance]
title: "Part 4: A public record of approved policy changes"
date: 2026-10-25 04:03:00 +0000
series: "AI governance in practice"
series_part: 4
description: "How every approved policy change is written to an append-only, hash-chained log that anyone can check without the server or database."
---

Part 4 of AI governance in practice. Part 3 covered the maker and checker process. This part covers the record that the process leaves behind.

Every policy change approved through the maker and checker process is written to a public, append-only record. Each line is one approval, stored as the production server signed it, inside a hash chain.

Anyone can check the chain without the server or the database. A changed or removed line breaks the chain.

## What it does not do

The chain shows that the record has not been altered. It does not show that the approver was who they claimed to be. That depends on the approver keys you trust.

## How we checked it

The record and how to verify it are described in the governance folder's README.

Source: [governance/README.md](https://github.com/pavancharak/parmana-core/blob/main/governance/README.md).
