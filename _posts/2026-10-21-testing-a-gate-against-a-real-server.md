---
layout: post
title: "Testing a gate against a real server, not a stub"
date: 2026-10-21
description: "A stub that returns the answer you expect proves little. Running the real API in test mode showed refusals and approvals that the stub never produced."
---

When we first tested a gate in front of an action, we used a stub. The stub returned the answers we had written down. The tests passed, and they told us almost nothing about the real system.

## What the stub missed

We then ran Parmana's real API in test mode, with in-memory storage, and sent it the same requests. The real server refused things the stub would have allowed:

- A policy version that approves an action without a signed human approval is refused when it is loaded. Every request under that policy fails, including requests that should be refused on other grounds.
- A policy version that has no approved policy-change record is refused with `POLICY_DENIED`.
- A policy version that does not exist is refused with `404`.
- A wrong key is refused with `401`.

An approved run also needed three things the stub did not model: a policy approved through maker and checker, a human approval signed for the exact resource, and business signals the policy reads. The approval was single use. A second request with the same approval was refused.

## What this changed

Each of these showed a place where our wrapper's mapping was wrong or incomplete. A `401` from the real server had been treated as an unknown outcome. The action did not run, so it should be a refusal. We fixed that, and kept the test.

## The limits

The test server runs in test mode, with its own keys and in-memory storage. It shows that the wiring works. It does not show that a production deployment behaves the same way. Test a real deployment before you rely on it.
