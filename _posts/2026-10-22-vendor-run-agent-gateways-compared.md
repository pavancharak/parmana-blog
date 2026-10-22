---
layout: post
categories: [Governance, Industry]
title: "Vendor run agent gateways and Parmana: what each answers"
date: 2026-10-22
description: "Vendors are starting to run their own gateways for AI agents. This compares that category with Parmana question by question, and shows how to use the two together."
---

Some vendors now run their own gateway for AI agents. In October 2026 Walmart announced one: an MCP server through which approved assistants search and buy at Walmart and Sam's Club, with Agent Profiles that let a shopper set a spending limit or require approval for each purchase, track an agent's orders separately, and revoke its access. Agents never see card data. We wrote about the announcement in [Walmart's Agent Gateway, and the layer it leaves open](/2026/10/22/walmart-agent-gateway-and-the-layer-it-leaves-open/).

This post compares the category, not one product. Vendors differ and their terms change, so check the ones you use.

## Two different questions

A vendor run gateway governs agents inside one vendor's platform. It answers: what may an agent do here, under our rules?

Parmana governs an organisation's own agents across every system they act on. It answers: may this specific action, with these parameters, run now under our policy, did a named person approve it, and can we prove what happened?

Both questions matter. They are not the same question.

## Question by question

| Question | Vendor run agent gateway | Parmana |
|---|---|---|
| Whose rules apply? | The vendor's, for its own platform | Yours, the same policy for every connected system |
| Which systems are covered? | That vendor's only | Every system routed through Parmana |
| Does the agent hold payment or system credentials? | No, for that vendor | No: they stay in Parmana's gateway, or in your connector endpoint for an external system |
| Can a limit or a person's approval stop an action? | Yes, as the vendor implements it | Yes: a versioned policy, and a signed approval bound to one action, one resource and an amount, used once |
| Who holds the record of what the agent did? | The vendor, in its platform | You: signed records of every action and every refusal |
| Can a third party verify that record offline? | Not stated in what vendors have published so far | Yes, with only the public key |
| Is a refused attempt recorded? | Not stated in what vendors have published so far | Yes: a signed Refusal Record that names the hash of the policy that decided it |

## Using both

Route the agent's calls to the vendor through Parmana. Your policy and a person's approval apply first; the vendor's limits apply second. An action has to pass both.

Parmana has no connector for a vendor run agent gateway today. One way to add it is an [external endpoint](https://docs.parmanasystems.com/guides/connect-any-external-system) you run: Parmana releases each approved request to it as a signed release, the endpoint verifies the release, and only then calls the vendor's gateway with the account's own credentials. The agent never holds those credentials, so it cannot go around Parmana to the vendor directly.

Two details need care in such an endpoint:

- **The price can move.** Between approval and checkout a total can change. The endpoint should refuse if the vendor's total is above the approved amount.
- **A timeout is not a refusal.** If the call to the vendor times out, the order may or may not exist. Record the outcome as unknown and do not retry under a new id. See [Fail closed, and the third answer](/2026/10/21/fail-closed-and-the-third-answer/).

Whether any of this is allowed depends on the vendor's terms for third party agents.

## Where a vendor gateway is stronger

- **It knows its own platform.** Catalogue, stock, prices and order state are the vendor's own data. Parmana only sees the facts it is given or the ones a connector checks.
- **It is already there.** A shopper can switch it on today with an account they have. Parmana has to be deployed and connected.
- **One approval, in one app.** If every action an agent takes is with one vendor, that vendor's controls may be enough.

## The takeaway

Expect more vendors to ship agent gateways. Each will answer "what may an agent do here" for its own platform, in its own form. An organisation whose agents act across several systems still needs one policy, one place for approvals, and records it holds and can prove. That is the layer Parmana provides, and it sits in front of the vendor gateways, not in place of them.

## Sources

- [Walmart: Making It Possible for Agents to Shop on Behalf of Customers](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers)
- [TechCrunch: While Amazon blocks AI agents, Walmart rolls out the welcome mat](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)
- [Unite.AI: Walmart Introduces Agent Profiles, Gateway for AI Shopping Agents](https://www.unite.ai/walmart-introduces-agent-profiles-gateway-for-ai-shopping-agents/)
- [Parmana docs: How Parmana compares](https://docs.parmanasystems.com/how-parmana-compares)
