---
layout: post
categories: [Governance, Industry]
title: "Which AI decisions need a person? MIT's decision matrix, and where Parmana sits"
date: 2026-10-23
description: "MIT CISR sorts AI decisions by how clear the answer is and how costly a mistake would be. Parmana is built for one of the four boxes, on purpose. Here is which one, and what that means for the others."
---

Researchers at the MIT Center for Information Systems Research published a simple way to decide what AI may decide on its own: the AI Decision Matrix. It came out of interviews with 30 executives, and MIT Sloan summarised it in September 2026. We read it because it answers a question every Parmana user has to answer first: which actions should need a person at all?

## The matrix in two questions

Ask two questions about any decision:

1. **Is the answer clear?** Does the data decide it, and would people agree on it? The researchers call this ambiguity.
2. **How bad is a mistake?** Is it costly and hard to undo, or cheap and easy to reverse? They call this risk.

That gives four kinds of decision:

| | A mistake is cheap | A mistake is costly |
|---|---|---|
| **The answer is clear** | **Routine.** Automate it; people watch while trust builds | **Consequential.** AI acts, people approve and handle exceptions |
| **The answer is unclear** | **Exploratory.** AI and people work it out together | **Strategic.** People decide; AI supports |

The researchers also split every decision into three parts: framing it (the rules, limits and goals), acting on it (gathering information, authorizing, executing) and learning from it (monitoring outcomes and holding someone accountable).

Their example company, One New Zealand, runs more than 50 AI agents. Each agent has a named human owner. Some limits are not negotiable: anything about pricing always has a human in the loop.

## Where Parmana sits: clear answers, costly mistakes

Parmana is built for the top right box. Refunds, payments, merges, deployments, changes to customer records: actions where the rule is clear, but getting it wrong costs money or trust and is hard to undo.

For that box, the matrix's three parts map onto Parmana directly:

| The matrix asks for | Parmana provides |
|---|---|
| Framing set in advance: rules, limits, criteria | A versioned policy for each action. Changing it needs a second person (maker and checker) |
| Authorizing and executing approved steps | A person's signed approval for that exact action, resource and amount, used once. The action is released through a gateway the agent cannot go around |
| Limits that are not negotiable, like One New Zealand's pricing rule | A policy rule. No rule that matches means no action |
| A named human owner for each agent | Each agent has its own key, limited to named actions. Approvers are registered people |
| Accountability for outcomes | A signed record of every action and every refusal, checkable later by anyone with the public key |

## A deliberate choice: every action needs a person

The matrix says routine decisions, clear and cheap, are good candidates for automation, with the agent given more freedom as trust builds.

Parmana does not do that, on purpose. Every action that goes through Parmana needs a signed human approval, reads included. A policy that tries to approve anything without one is refused when it loads. There is no amount or risk level below which an action runs on its own.

That is a trade-off, and it is worth being plain about it:

- **What it costs.** Every action waits for a person. For high volume, low risk work that is slow, and the matrix is right that it does not need to be.
- **What it buys.** The rule is the same everywhere and easy to check. There is no threshold an agent can learn to stay under, and no "low risk" label that someone sets wrong.

So the practical answer is to choose what goes through Parmana. Routine decisions, in the matrix's sense, can run without it, under the controls they already have. The actions you route through Parmana are the ones you have decided need a person every time.

## What Parmana does not cover

- **Unclear answers.** Parmana checks whether an action is allowed, not whether the agent understood the task. Exploratory and strategic decisions are about framing and judgement. People and other tools do that work; Parmana can still guard the action at the end of it.
- **Learning beyond the record.** The matrix asks companies to monitor outcomes and improve over time. Parmana keeps the signed records that learning needs, but it does not analyse them for you.

## The takeaway

The matrix's closing line is worth repeating: the shift is from asking where AI can be used to managing the business decisions it shapes. Parmana is one answer for the decisions where the rule is clear and a mistake is expensive: a person approves each action, and the proof is kept. Deciding which of your decisions belong in that box comes first.

## Sources

- [MIT Sloan: A framework for determining when AI can make decisions](https://mitsloan.mit.edu/ideas-made-to-matter/a-framework-determining-when-ai-can-make-decisions)
- [MIT CISR: Designing Decision Rights for AI](https://cisr.mit.edu/publication/2026_0601_AIDecisionMatrix_SebastianWeillHaskampVomBrocke)
- [Parmana docs: Human approval](https://docs.parmanasystems.com/concepts/human-approval)
