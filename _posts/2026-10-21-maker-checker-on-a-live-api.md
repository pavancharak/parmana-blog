---
layout: post
categories: [Governance]
title: "Maker and checker on a live API: what we proved, and what we did not"
date: 2026-10-21
description: "A policy change needs a listed checker. We found production refusing every approval, fixed it, and approved one live change. Here is exactly what that shows."
---

A policy change in Parmana takes effect only when a second person approves it. The proposer is the maker, the approver is the checker, and the approval needs a single-use step-up signature. Each policy has its own list of allowed checkers, set in configuration.

This week we found a fault that the tests had missed.

## The fault

The local server read the checker list correctly. The production entry point did not pass it on. Every approval on production was refused with `403 CHECKER_NOT_IN_SCOPE`. This failed closed, so nothing was approved wrongly, but the approval step was unusable.

The fix is a few lines in the production entry. We also added a test that fails if either entry point stops passing the list. We checked that the test fails on the old code before we trusted it.

## What we proved live

We proposed a change to a policy that no agent uses, with a maker key, and approved it with the checker key and a signed step-up. The response showed `status: APPROVED`, and the approved version was stored. That shows the wiring works end to end on production.

## What we did not prove

- **Refusal of an unlisted checker on production.** That is covered by unit tests, not tried live.
- **Separation of duties.** Both keys were created by the same operator on one machine. The check shows the wiring, not that two different people made the decision.
- **Approval issuers.** The keys that sign approvals for agent actions are not yet limited per policy. That gap is still open.
- **Quorum.** One checker is enough. We have not built a second approval requirement.

Writing these down matters as much as the fix. A claim is only as strong as the list of what it does not cover.
