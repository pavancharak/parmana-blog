---
layout: post
categories: [AI governance]
title: "Part 5: Authority grants: what an agent may do"
date: 2026-10-25 04:04:00 +0000
series: "AI governance in practice"
series_part: 5
description: "How a grant says which agent may do what, within which limits, and until when, so an API key is not the same as permission to act."
---

Part 5 of AI governance in practice. Part 4 covered the public record of policy changes. This part covers the permission that sits between a key and an action.

An API key that can call an endpoint is not yet authority over every request. A grant says exactly what one agent may do: which action, up to what limit, and until when.

A policy can require a grant. The request is decided only when its caller holds a grant that is in force.

## What it does not do

The guide's status note says which grants are implemented and deployed, and which policies require them. Check that note before you rely on a grant.

## How we checked it

The grant guide describes each refusal and what the signed record holds for it.

## What is still open

Grants must be reviewed when they expire, or the agent keeps the permission past its purpose.
