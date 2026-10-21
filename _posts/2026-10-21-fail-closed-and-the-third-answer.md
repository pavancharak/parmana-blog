---
layout: post
title: "Fail closed, and the third answer"
date: 2026-10-21
description: "A gate in front of an action gives three answers, not two: refused, released, or unknown. The unknown one is the easy one to get wrong."
---

A gate in front of an action seems to have two answers: allow it or refuse it. In practice there is a third, and most integrations get it wrong.

## Refused, released, unknown

- **Refused.** The gate said no, and the action did not run. Retrying with the same facts gets the same answer, so the caller should stop.
- **Released.** The gate said yes, and the action ran. The caller records the result.
- **Unknown.** The request reached the gate, and then the connection dropped or timed out. The gate may already have released the action. We do not know.

The third case is the one that causes damage. If the caller treats a timeout as a refusal, it retries, and the action can run twice.

## What we built, and checked

In a spike that wraps a Python governance engine's actuator, we map each answer explicitly:

- A `403` from the gate, a policy not found, a wrong key, or a kill switch refusal means refused. The actuator does not run.
- A `502` or `500` from the gate, or a timeout after the request was sent, means unknown. The actuator does not run, and the outcome is recorded as unknown.
- A connection refused before the request was sent means refused, and the caller may retry.
- Every retry of the same action reuses the same transaction id, so the gate can recognise a repeat.

Those mappings are checked by tests against a local test server. A test that breaks the refusal path fails, which is how we know the tests are looking at the right thing.

## The rule

When you cannot tell whether an action happened, do not retry it under a new id. Record it as unknown, and check the gate's record before doing anything else.
