---
layout: post
categories: [Engineering]
title: "Run the checks in an afternoon"
date: 2026-10-25 00:30:00 +0000
series: "From limits to proof"
series_part: 3
description: "A practical walkthrough for engineers: build Parmana from source, run the test suite and the attack scenarios, and verify a signed record."
---

This is part 3 of the series From limits to proof. Part 2 gave you questions to ask a vendor. This part shows how an engineer can test the answers for themselves.

If you want to know whether Parmana does what it claims, you do not need to trust our description. You can build it, run the tests, run the attack scenarios, and check a signed record yourself. This post gives the steps in order, with the commands we use.

You need Node.js 24 or later.

## What it does

The repository contains the server, the SDKs and the offline verifier. Each step below checks a different part.

## Step 1: build and test

```bash
git clone https://github.com/pavancharak/parmana-core
cd parmana-core
npm ci
npm run build
npm test
```

`npm test` runs the test suite. It needs no credentials and no network access.

## Step 2: run the attack scenarios

```bash
npm run evaluate
```

This runs the 16 attack scenarios in `evaluations/scenarios.json` and reports whether each one was blocked. Read the output against [EVALUATION.md](https://github.com/pavancharak/parmana-core/blob/main/EVALUATION.md), which explains what each scenario tests.

## Step 3: verify a signed record

The verifier checks a record with only a file and a trust file. It makes no network calls.

```bash
npx @parmana/verifier proof.json trust.json
```

The output is a short JSON result. Exit code `0` means valid, `1` means invalid, and `2` means a usage error, a missing file, or invalid JSON.

To see a valid and an invalid record, run the test vectors in the [verifier repository](https://github.com/pavancharak/parmana-verifier). The tampered record fails on purpose.

## What it does not do

- The verifier checks that a record has not changed and was signed by a key you trust. It does not check the policy that produced the decision.
- The test suite proves what the tests cover. It is not a proof that every path is correct.
- Test keys in the repository are for tests only. Do not use them for real records.

## How we checked it

The steps above are the checks we run. The mutation testing report in [docs/MUTATION-TESTING.md](https://github.com/pavancharak/parmana-core/blob/main/docs/MUTATION-TESTING.md) shows how often the tests catch deliberate bugs in the security code.

## What is still open

Some checks depend on the version of Node.js and on optional hybrid signatures. If a step fails on your machine, open an issue in the repository and include the output.
