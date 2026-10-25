---
layout: post
categories: [Security]
title: "Lessons from the limits we still have"
date: 2026-10-25
description: "Honest lessons from building Parmana: what we got wrong, what we fixed, and the limits we still document instead of hiding."
---

Most launch posts describe what a product does. This one describes what we got wrong, what we found, and what we still have not solved. We think a control that names its limits is more useful than one that claims to have none.

## What it does

We keep a public log of gaps. Each gap has its evidence, its severity, and what was done about it. The log is in [docs/VERIFICATION-GAPS.md](https://github.com/pavancharak/parmana-core/blob/main/docs/VERIFICATION-GAPS.md). One entry, G-24, is an authorization bypass that was found and fixed. Publishing it was the point: a reader can see that the problem existed and that it was closed.

## Lesson 1: refuse when you are not sure

When the system cannot tell whether an action is allowed, it refuses. It does not guess. This makes some legitimate requests fail, and we accept that. A system that guesses on an unknown request is the failure we set out to prevent.

## Lesson 2: write down what the signature does not cover

A signature proves that a key signed a set of fields. It does not prove that every field was covered. In one verifier format, the schema version was not covered by the signature, so a version 2 record could be presented as an older format. We document this, and a trust file can require the newer format from a date you choose. We would rather state the gap than hide it.

## What it does not do

This post does not claim that Parmana is free of defects. The gap log lists the open ones. Read it before you decide what to rely on.

## How we checked it

Each lesson links to the evidence: the gap log, the test suite, and the verifier limits. If you think we have missed something, the [security challenge](https://github.com/pavancharak/parmana-core/blob/main/SECURITY-CHALLENGE.md) describes how to test it yourself and how to report it.

## What is still open

We have not yet had an independent audit of the whole system. The internal reviews are described in the claims register, and an external review is the next step we want.
