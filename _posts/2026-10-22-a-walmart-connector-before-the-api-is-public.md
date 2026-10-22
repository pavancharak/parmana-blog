---
layout: post
categories: [Engineering, Industry]
title: "A Walmart connector, before the API is public"
date: 2026-10-22
description: "Walmart's Agent Gateway is in beta and its tools are not published. We built the Parmana side anyway, against a mock, and wrote down exactly what only Walmart can answer."
---

After Walmart announced its Agent Gateway, the obvious question was what a Parmana connector for it would take. The gateway is an MCP server in beta, and its tool names and schemas are not public. So we built everything on our side that does not depend on them, tested it against a mock, and listed what is still missing.

It is an example, not a claim: Walmart's real gateway is not called, and the example is not part of the Parmana repository today. If you want to build the same thing, the pieces below are all on the documented [external connector path](https://docs.parmanasystems.com/guides/connect-any-external-system).

## The shape

```
agent -> Parmana -> signed release -> connector endpoint -> Walmart Agent Gateway
```

- The agent asks Parmana to place an order, naming a cart, its items and a maximum total.
- A policy approves only with a person's signed approval for that cart, covering that maximum, and refuses anything above 500.
- Parmana releases the approved request to a connector endpoint as a signed release.
- The endpoint, and only the endpoint, holds the Walmart account link. It places the order.

No Parmana code changed. This is the external connector path any system can use: you run a small endpoint, register it through maker checker, and Parmana releases approved requests to it.

The account link sits in the endpoint for one reason: an agent that held it could check out at Walmart directly and never ask Parmana.

## Four things the endpoint has to get right

**1. The price can move after approval.** A person approves "this cart, up to 100". By the time the order is placed, the total may be 103. The endpoint asks for a quote first and refuses if the total is above the approved maximum. Nothing is placed.

**2. Parmana may send the same release twice.** If Parmana does not hear back, it can send the release again. The endpoint keeps its first answer by transaction id and returns it, so a repeat never places a second order.

**3. A lost answer is not a refusal.** If the call to Walmart times out, the order may exist. The endpoint answers 502, which Parmana records as an unknown outcome for a person to resolve, and it refuses any later resend for that transaction with 409. It never retries on its own. This is the rule from [Fail closed, and the third answer](/2026/10/21/fail-closed-and-the-third-answer/), applied to a purchase.

**4. Only what was signed counts.** The endpoint acts only on a release whose signature, audience and expiry verify. A changed amount, a release made for another endpoint, or a different action is refused before anything reaches Walmart.

## How we tested it

Nine tests run the endpoint against a mock gateway that can raise prices and lose answers. The releases in the tests are signed by the same code the Parmana server uses, not hand built JSON, so the endpoint sees exactly what it would see in production.

We also checked the tests themselves. Removing the price check makes one test fail. Removing the mark that stops a retry after a lost answer makes another fail. A test suite that stays green when the protection is gone is not testing the protection.

## What only Walmart can answer

- **Access.** Admission to the beta for the account that will own the agent's profile.
- **Tools.** The real tool names and schemas. Above all, whether there is a quote step before an order is placed. Without one, the endpoint cannot refuse a price rise before ordering.
- **Idempotency.** Whether placing an order accepts a key that makes a repeat return the first order. Without one, a lost answer can only be settled by a person checking the account.
- **Sign in.** How the account link works for a server side client, and for how long.
- **Who may connect.** Whether a company's own agent is allowed, or only consumer assistants.
- **Terms.** The full agent terms, rate limits, and how the endpoint must identify itself as an agent.

When those are known, one piece changes: the mock is replaced by an MCP client for Walmart's tools. The policy, the checks and the tests stay.

## Two approvals, by default

With Walmart's default settings an order would be approved twice: by a person through Parmana, then by the customer in Walmart. To rely on Parmana's approval alone, set a spending limit on the agent's Walmart profile at or above the policy's maximum. Walmart says it may still ask for its own approval at times.

## Sources

- [Walmart: Making It Possible for Agents to Shop on Behalf of Customers](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers)
- [TechCrunch: While Amazon blocks AI agents, Walmart rolls out the welcome mat](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)
- [Vendor run agent gateways and Parmana: what each answers](/2026/10/22/vendor-run-agent-gateways-compared/)
