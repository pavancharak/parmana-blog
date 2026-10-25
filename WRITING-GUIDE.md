# Writing guide for the Parmana blog

Read this before you write or change a post. Every new post must follow it. Start each new post from [templates/post-template.md](templates/post-template.md).

## Purpose

The blog explains how Parmana checks AI actions and keeps proof of what happened. It shows what we built, what we tested, and what is still open. It is not a marketing channel. Readers should finish a post knowing something true and useful.

## Who we write for

Name the reader in the first paragraph. Every post serves one of these three readers.

| Reader | What they need | What to avoid |
| ------ | -------------- | ------------- |
| **Business leaders** | The risk, the decision they can make, and what it costs them. | Code, internal jargon, unexplained acronyms. |
| **Engineers** | Steps they can run, the reason behind each one, and the expected output. | Vague claims with no command, file or test to check. |
| **Auditors and risk teams** | Evidence they can verify, with the limits stated plainly. | Assurances without links, and claims that go beyond the evidence. |

## Voice

- Plain English. Short sentences. Active voice.
- Define a term the first time you use it, or link to the [glossary](https://docs.parmanasystems.com/glossary).
- Do not use em dashes or en dashes in any text. Use a full stop, a comma, or a colon.
- Use the homepage wording for the framing: every action stays within what your business allowed, and Parmana keeps proof of what happened.
- Do not overstate. Say what is built, what is tested, and what is not yet true.
- Address the reader as "you". Speak for the team as "we".

## Every claim has evidence

- Link each claim to the code, the test, or the doc that supports it. If you cannot link it, say it is not yet verified, or leave it out.
- Name the limits. Every post that describes a capability has a section on what it does not do.
- Do not publish unresolved security findings. Security results go to the reports folder only after review, as described in [reports/README.md](https://github.com/pavancharak/parmana-core/blob/main/reports/README.md).
- Do not include secrets, keys, customer data, or internal hostnames. Use placeholders such as `YOUR_API_KEY`.

## Front matter

Every post starts with this front matter, in this order:

```yaml
---
layout: post
categories: [Security]
title: "Sentence case title, under 70 characters"
date: YYYY-MM-DD
description: "One sentence that tells the reader what they will learn. Under 160 characters."
---
```

- **layout:** always `post`.
- **categories:** one or two of `Security`, `Operations`, `Engineering`, `Product`, `Compliance`.
- **title:** sentence case, specific, and free of dashes.
- **date:** the publication date, in `YYYY-MM-DD` format.
- **description:** one sentence. It appears in search results and on the post list.

File names follow the pattern `YYYY-MM-DD-short-kebab-title.md` and match the date in the front matter.

## Structure

Use these sections, in this order. Keep the headings in plain words.

1. **Opening (2 to 4 sentences).** The problem, who it affects, and what the post covers.
2. **What it does.** The capability, in plain terms, with the link to its code or doc.
3. **What it does not do.** Required. The limits, stated plainly.
4. **How we checked it.** The test, the scenario, or the run, with links to the evidence.
5. **What is still open.** Known gaps, and what would close them.

Engineering posts add a section with commands and expected output. Keep every command runnable, and state the version or date it was checked.

## Publishing checklist

Before you open a pull request, confirm every item:

- [ ] Front matter is complete, in the order above, and the date matches the file name.
- [ ] The post names its reader in the first paragraph.
- [ ] There are no em dashes or en dashes anywhere in the post.
- [ ] Every claim links to evidence, or is marked as not yet verified.
- [ ] A "What it does not do" section is present.
- [ ] Commands were run, and the output shown is real.
- [ ] No secrets, keys, customer data, or unresolved security findings.
- [ ] Every link was checked, and each one opens.
- [ ] The post was reviewed by someone other than its author.

## Process

1. Draft the post from the template, on a branch.
2. Check it against this guide and the checklist.
3. Open a pull request. Do not push directly to `main`.
4. Publish after review and merge.
