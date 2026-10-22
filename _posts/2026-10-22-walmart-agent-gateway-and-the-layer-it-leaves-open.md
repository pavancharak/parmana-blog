---
layout: post
categories: [Governance, Industry]
title: "Walmart's Agent Gateway, and the layer it leaves open"
date: 2026-10-22
description: "Walmart now lets approved AI agents shop through an MCP server, with no card access, spending limits and per purchase approval. That covers one store. Here is what it leaves to the company running the agent."
---

On 21 October 2026 Walmart announced the Walmart Agent Gateway and Agent Profiles. As reported, the gateway is an MCP server that lets approved AI assistants, including ChatGPT, Gemini and Meta's Muse, search Walmart and Sam's Club and complete purchases. Agent Profiles, due next month, let a shopper authorize each agent separately.

We read the announcement closely, because it puts into a large retailer's product several controls we have argued for. We could not open Walmart's own page from our environment, so everything below about Walmart comes from the press coverage linked at the end.

## What Walmart built

- **The agent never holds payment credentials.** Agents cannot see card data and cannot add or change payment methods.
- **Limits per agent.** A shopper can set a spending limit for an agent, or require approval for each purchase.
- **Separate tracking.** Purchases made by an agent are shown apart from the shopper's own orders.
- **Revocation.** A shopper can remove an agent's access at any time.
- **Agents must say they are agents.** They must not hide that they are automated, and they must respect rate limits. Walmart says it will block agents that break these terms.

## The same pattern, applied to one store

These controls answer a specific question: what may an agent do inside Walmart, and who agreed to it. Each has a counterpart in Parmana, which sits between an agent and the systems it acts on.

| Walmart | Parmana |
|---|---|
| The agent never gets card data | A gateway holds the credentials for every connected system; the agent never receives them |
| A spending limit per agent | A versioned policy rule, for example a refund amount up to a set value |
| Approval for each purchase | A person's signed approval, bound to one action, one resource and an amount, used once, and expiring |
| Purchases tracked per agent | A signed record of every released action and every refusal, tied to the calling key |
| Revoke an agent | Remove the agent's API key; an operator kill switch refuses all new actions at once |

The point is not that one copies the other. It is that a retailer facing real agents arrived at the same controls: keep credentials away from the agent, decide by rule, ask a person for the actions that need one, and keep a record per agent.

## What it leaves open

Walmart's controls end at Walmart's boundary. That is reasonable for a store, and it leaves three things to whoever runs the agent.

**1. Other systems.** A company's agent that buys supplies from Walmart may also issue refunds, merge code and post in Slack. Each vendor that builds a gateway will build its own limits, approvals and logs, in its own form. The company still needs one place where its own policy applies to all of them, before any of them is called.

**2. Evidence the company can check.** The purchase history lives in Walmart's systems. Nothing in the announcement says the shopper or the agent's operator receives a record they can verify without trusting the platform. For an auditor, "the vendor's dashboard says so" is weaker than a signed record that anyone can check offline with a public key.

**3. Refusals.** A spending limit that stops a purchase is useful. A record that the purchase was attempted, refused, and why, is what an investigation needs afterwards. In Parmana a refusal produces a signed Refusal Record, the same as an approval produces an Execution Trust Record, and since this month each Refusal Record names the hash of the policy that decided it.

## What we are not claiming

- Parmana has no Walmart connector today. Whether one is possible depends on Walmart's terms for third party agents, which we have not seen.
- A per purchase approval in Walmart's app and a signed approval in Parmana are different things. We have not tested Walmart's flow.
- A governance layer only governs actions that are routed through it. An agent that calls a vendor directly, with its own credentials, is outside it. That is why the credentials belong in the gateway, not in the agent.

## The takeaway

Walmart's gateway is good news for anyone building agent controls: it shows a retailer treating "what may this agent do, and who agreed" as a product feature, not an afterthought. Each vendor will answer that question for its own platform. The company running the agent still has to answer it across all of them, and keep proof it can show to someone else.

## Sources

- [Unite.AI: Walmart Introduces Agent Profiles, Gateway for AI Shopping Agents](https://www.unite.ai/walmart-introduces-agent-profiles-gateway-for-ai-shopping-agents/)
- [Inside Retail US: Walmart launches tools for AI agents to shop for customers](https://insideretail.us/walmart-launches-tools-for-ai-agents-to-shop-for-customers/)
- [Android Headlines: Walmart Opens Doors to AI Shopping Agents](https://www.androidheadlines.com/2026/10/walmart-ai-agent-shopping-profiles-gateway.html)
- [dig.watch: Walmart announces AI agent and gateway shopping tools](https://dig.watch/updates/walmart-announces-ai-agent-shopping-tools)
- [Walmart Agent Gateway page](https://www.walmart.com/cp/walmart-agent-gateway/1280482)
