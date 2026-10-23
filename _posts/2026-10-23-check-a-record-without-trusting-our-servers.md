---
layout: post
categories: [Engineering]
title: "Check a record without trusting our servers"
date: 2026-10-23
description: "A signed record only helps if someone can check it without asking us. The Parmana verifier runs offline, with no network calls and no account. Here is how to run it, and what a changed record looks like."
---

A record of what an AI agent did is only useful if the person reading it does not have to trust the company that produced it. If checking the record means calling the same servers that wrote it, the check proves very little.

So the Parmana verifier runs on your own machine. It makes no network calls and needs no account.

## What it checks

The verifier recomputes the record's hash, then checks its Ed25519 signature. Where a record carries an ML-DSA-65 signature, it checks that too. The keys it trusts are the ones you pin in a trust file, each with a fingerprint and validity dates. The verifier does not fetch keys from us.

## Run a valid record

```sh
node bin/parmana-verify.mjs test/vectors/record-whole-record-v3.json test/vectors/trust-whole-record.json
```

The output is one line of JSON:

```json
{"valid":true,"coverage":"full","errors":[],"checks":{"trustRecordHash":true,"signature":true,"hybridSignatures":true}}
```

The exit code is 0.

## Run a changed record

Change one value in a record after it was signed, and the check fails:

```sh
node bin/parmana-verify.mjs test/vectors/record-tampered-amount.json test/vectors/trust.json
```

The output lists each failed check. Here the hash no longer matches the record, and the signatures do not verify. The exit code is 1.

The files in `test/vectors` are test material, labelled as such in the repository. For a real record, pin the keys you trust and run the same command.

## What you need

- Node.js 24 or later. ML-DSA-65 checks also need OpenSSL 3.5 or later.
- Nothing else. The verifier has no dependencies.

## What a passing check does not show

A passing check shows that the record is intact and was signed by a key you trust. It does not show that the policy behind the record was the right one, or that the external system carried out the action. Those are separate questions, and the record does not answer them.

The verifier source and installation steps are in the [verifier repository](https://github.com/pavancharak/parmana-verifier). The [verify page](https://parmanasystems.com/verify) has the same commands.
