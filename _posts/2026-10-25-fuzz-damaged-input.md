---
layout: post
categories: [Engineering]
title: "Part 8: Fuzz the input: refuse, never crash"
date: 2026-10-25 05:31:00 +0000
series: "Working on Parmana"
series_part: 8
description: "What the fuzz tests send to the server, and the rule they enforce: damaged input must be refused clearly, never crash the system."
---

This is part 8 of the series Working on Parmana. Part 7 covered testing that a control works. This part covers testing what happens when the input is damaged or arbitrary.

The fuzz tests send damaged and arbitrary requests, policies, and records to the system. Each one must be refused with a clear answer.

A crash on bad input is a defect, because a crash may leave a decision half made.

## What it does not do

The fuzz tests cover the inputs they generate. They do not prove that every possible input is refused cleanly.

## How we checked it

Source: [CONTRIBUTING.md](https://github.com/pavancharak/parmana-core/blob/main/CONTRIBUTING.md).
