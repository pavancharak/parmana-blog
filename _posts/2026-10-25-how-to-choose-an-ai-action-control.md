---
layout: post
categories: [Product]
title: "How to choose a control for AI actions"
date: 2026-10-25
description: "Seven questions to ask any vendor before you let AI take real actions, with the answers to look for and the warning signs to avoid."
---

Many tools now promise to make AI safe for business. Some filter text, some manage who can call an API, and some only log what happened. Those can all be useful, but they answer different questions. This post gives you questions to ask before you choose, so you can compare tools on the same terms.

## What it does

A control for AI actions should answer one question for every action: was this allowed, and can I prove it? The questions below test that.

1. **Where does the decision happen?** Look for a check that runs before the action, outside the AI. A rule in the prompt is not a control.
2. **What happens when the answer is unclear?** The right answer is a refusal. Ask for an example.
3. **Who can approve an exception, and how?** Look for a named person and a signed approval, not a shared password.
4. **Can you check the record without the vendor?** If you need the vendor's servers to verify a record, you depend on them.
5. **What does the record contain?** It should show what was asked, what was checked, what was allowed, and what happened.
6. **Can your own technical team test it?** Ask for the tests, the evaluation, and how to run them.
7. **What does it not do?** A good vendor names the limits in writing.

## What it does not do

No single tool answers all seven questions for every business. A control at the point of action does not replace identity management, audit, or legal review. Use it alongside them.

## How we checked it

To make this list useful, we apply it to our own product first. The answers, and the evidence for each, are in the [comparison guide](https://docs.parmanasystems.com/how-parmana-compares), which also says where Parmana is weaker than other categories.

## Warning signs

- Claims with no way to test them.
- Verification that needs an account or a live connection to the vendor.
- Limits that are missing from the documentation.
- A promise that the AI "will not" do something, with no check that enforces it.

## What is still open

These questions do not cover every risk. Add questions specific to your industry, and involve your risk team before you sign.
