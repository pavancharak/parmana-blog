---
layout: post
categories: [Compliance]
title: "Part 3: Check a record offline, without trusting us"
date: 2026-10-25 00:40:00 +0000
series: "From limits to proof"
series_part: 3
description: "How an auditor or risk team can check a signed Parmana record with a file and a trust file, with no network access and no account."
---

This is part 3 of the series From limits to proof. Part 2 gave you questions to ask a vendor. This part shows an auditor how to check one signed record.

An audit is only as strong as the evidence behind it. If the only proof that an AI action was approved is a log written by the system that did the action, the auditor has to trust that system. This post explains how to check a Parmana record without trusting Parmana's servers or database.

## What it does

Each action that goes through Parmana leaves a signed record. The record says what was asked, what was checked, what was allowed, and what ran. The offline verifier checks three things:

- The record has not been changed since it was signed.
- The signature was made by a key listed in your trust file.
- Each key is the one you chose to trust, matched by its fingerprint.

The verifier works with a record file and a trust file. It never fetches keys, makes no network calls, and needs no account.

## What it does not do

- It does not check whether the policy behind the decision was the right one. That is a review of the policy itself.
- It does not check the state of the business system the action touched.
- It does not decide which keys you should trust. You decide, and you check each key against its owner's published fingerprint before you pin it.
- It does not catch a record that was never created. If an action ran without a record, the verifier cannot show that.

## How we checked it

The verifier has its own test suite, its test records, and a documented security review scope for an external reviewer. The security review scope is in [docs/SECURITY-REVIEW.md](https://github.com/pavancharak/parmana-verifier/blob/main/docs/SECURITY-REVIEW.md). The test records include valid records and records that fail on purpose, so you can see each check work.

## How to run it

On Node.js 24 or later:

```bash
npx @parmana/verifier record.json trust.json
```

Exit code `0` means the record is valid, `1` means it is invalid, and `2` means a usage error, a missing file, or invalid JSON in either file. The output lists each check, so you can keep it as part of the audit file.

## What is still open

A version 2 record can be altered so that it appears to be an older format, because the schema version is not covered by the signature. The verifier documents this limit, and a trust file can require the newer format from a set date. Review the [verifier limitations](https://github.com/pavancharak/parmana-verifier#limitations) before you rely on a version 2 record.
