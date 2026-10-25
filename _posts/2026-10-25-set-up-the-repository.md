---
layout: post
categories: [Operations]
title: "Part 1: Set up the repository on your machine"
date: 2026-10-25 05:00:00 +0000
series: "Operations in practice"
series_part: 1
description: "What you need to build, typecheck and test Parmana locally, in the order the local development runbook gives."
---

This is part 1 of the series Operations in practice. It starts from a clean machine, before any production work.

The local development runbook sets out the steps: install Node.js 24 or later, build the repository, typecheck it, and run the tests. Each command in the runbook is in the package file, and each fix in it matches an error the team has seen.

Run the steps in order. A failure at one step is easier to understand than a failure at the end of a long chain.

## What it does not do

The runbook covers a clean setup on Windows. It does not cover every operating system, and it does not replace the production steps in later parts.

## How we checked it

Source: [docs/runbooks/LOCAL-DEVELOPMENT.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/LOCAL-DEVELOPMENT.md).
