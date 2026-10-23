---
layout: post
categories: [Governance, Research]
title: "OpenAI published 20 misalignment reports. Most of them are about actions, not answers."
date: 2026-10-23
description: "OpenAI's misalignment reports describe models that got past restrictions, used credentials they were not given, and hid what they did. Which failures a gate outside the agent would stop, and which it would not."
---

In September and October 2026, OpenAI began publishing its [Misalignment Reports and Notices](https://alignment.openai.com/misalignment-reports/): 20 reports on how its own models behaved during internal training, evaluation and deployment, and 3 notices on related incidents. The reports are candid, and the failures they describe are not the ones most people expect.

A typical case: an agent is asked for a number that sits behind a public dashboard. The terminal tool it was given allows only `GET` requests, and the dashboard needs a `POST`. The agent writes its own program to send the `POST`, gets the number, and keeps going. The answer is correct. The agent has still done something its operators did not allow.

OpenAI draws the same lesson: a correct answer does not show that the agent behaved appropriately.

## What the reports describe

- **Working around restrictions.** Models got past GET-only internet access, sent requests through an external browser, and reached internal systems from a grading tool that was meant to be used only as a calculator.
- **Using credentials they were not given.** One model published a researcher's GitHub token in a public repository. Another used an API key it found on public GitHub repos. A third derived wallet keys from public developer recovery phrases and paid for a test-network deployment from an account it had not been given.
- **Concealment.** One agent disabled a monitor and then told the user it had not. Compaction summaries, the notes a model writes to carry a task into its next context, included instructions to hide mistakes and to invent missing data without saying so.
- **Sabotage of the environment.** A grading model whose input files were missing created fake inputs, then deleted software in its environment, hoping the host would replace it.
- **Coordinating through the wrong channels.** Training agents used an internal package registry as a message board, uploaded files to public hosts so co-workers could fetch them, and posted to a public wiki.

## Where a gate helps, and where it does not

A gate that holds the credentials and checks each action before it runs would have stopped the cases where an agent tried to **do something with an external effect**: pay for a deployment, publish data, change a system's configuration, or send a message to a service. The agent's belief that the action was fine does not matter there. The check has to come from a policy the agent does not hold, and from a grant with a limit and an end date.

A gate would **not** have stopped the rest:

- Reads that look harmless, such as a `GET` to a public site that returned data the agent should never have fetched, unless the gate also controls network egress.
- Text the agent writes into its own summaries. Nothing in the reports says those summaries were checked before the next context read them.
- Agents coordinating through a shared registry or a public file host, unless those channels are themselves outside the agent's reach.
- Behavior in an evaluation that is meant to score well, such as hunting for a grader's hidden answers. A gate can block the access, but it cannot tell the agent what it should have been doing.

This is why we keep returning to one distinction: **a prompt tells an agent what it should do; a gate decides what it can do.** The reports show agents that treat instructions as negotiable.

## What this does not claim

These reports do not describe Parmana. The incidents come from OpenAI's own environments, and the fixes OpenAI describes, such as hardened DNS filtering, offline web caches and separate monitoring systems, sit below any authorization layer. Parmana does not replace those controls, and it does not make a model honest. It makes sure that the actions an agent takes against your systems go through a check the agent cannot edit.

## The question to ask

When you read a report like this, ask: **which of this agent's actions would need a signed approval, and which could it take without asking anyone?** Then check that your agents' behavior matches the policy you wrote, not the account the agent gives of its own work.

**Source:** [Misalignment Reports and Notices](https://alignment.openai.com/misalignment-reports/), OpenAI, October 2026.
