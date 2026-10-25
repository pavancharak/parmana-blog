---
layout: post
categories: [Security]
title: "Part 5: Sign the intent before anything is released"
date: 2026-10-25 03:04:00 +0000
series: "Security in practice"
series_part: 5
description: "Why Parmana stores a signed statement of an action before it calls the connector, and what happens when that record cannot be stored."
---

Part 5 of Security in practice. Part 4 covered binding the content that runs to the content that was approved. This part covers the record written before anything runs.

An execution trust record contains the result, so it can only be built after the action has been released. That leaves a window in which an action could run with no signed record of what was about to run.

An execution intent closes that window. Before the connector is called, the runtime signs and stores a record of what it is about to release. If that record cannot be stored, nothing is released.

## What it does not do

The intent proves what Parmana was about to release. It does not prove that the connector completed the action. The page explains what the intent does not prove, and how to find and repair a released action that has no signed record.

## How we checked it

The feature is listed as available, with the source files named in the page and a live verification date.

Source: [docs/site/concepts/execution-intents.mdx](https://github.com/pavancharak/parmana-core/blob/main/docs/site/concepts/execution-intents.mdx).
