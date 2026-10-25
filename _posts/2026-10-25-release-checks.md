---
layout: post
categories: [Engineering]
title: "Part 6: The checks a change must pass before release"
date: 2026-10-25 02:40:00 +0000
series: "Working on Parmana"
series_part: 6
description: "The branch, sign-off, tests and records a change needs before it is merged, and the CI checks that run again on every pull request."
---

This is part 6 of the series Working on Parmana. Part 5 covered adding a connector, and the earlier parts covered the map, the request path and the policy. This part covers what a change must pass before it is merged, so the work you have done reaches the code in a state that can be trusted.

## What it does

Every change follows the same steps:

1. **Its own branch from `main`**, and a pull request. Nothing is pushed to `main` directly.
2. **Tests with the change.** A bug fix adds a test that fails without the fix. A new behavior adds tests, including the refusal paths.
3. **The full check passes.** A pre-commit hook scans for secrets with gitleaks, then runs the typecheck, lint, format, every test, the build, and the runnable examples. CI runs the same checks on the pull request.
4. **Each commit carries a `Signed-off-by` line**, added with `git commit -s`.
5. **The records are updated in the same pull request.** That means the claims register when a claim changes, the gap log when a gap is found or closed, the open work list, an architecture decision record when a decision is made, and the published docs and changelog when behavior a reader relies on changes.

The principles a change must keep are short. The policy decides. Failures refuse rather than degrade silently. Evidence is signed and append only. Policy evaluation is deterministic.

## What it does not do

Passing these checks is not an audit, and it does not show that a change is correct for your business. It shows that the change builds, passes its tests, and keeps the ownership rules and the records in order.

## How we checked it

Run the same checks locally before you push:

```bash
npm test
npm run evaluate
npm run examples
```

CI runs the test suite, the build, the connector and Python SDK jobs, the self-hosted check, CodeQL, dependency review, the sign-off check, and a job that verifies policy approvals. A change that fails any of them is not merged.

## What is still open

The pre-commit hook needs gitleaks installed locally, or Docker. If the hook reports stale build output, run `npm run build` and commit again.
