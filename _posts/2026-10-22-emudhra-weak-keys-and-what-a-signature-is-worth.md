---
layout: post
categories: [Security, Industry]
title: "eMudhra's weak keys, and what a signature is worth"
date: 2026-10-22
description: "Eight eMudhra CA keys turned out to be weak, created in a 2025 key ceremony. Browsers blocked them within days; many servers did not. What we checked in Parmana, and what anyone who signs records should take from it."
---

This week the web learned that eight intermediate certificate authority keys from eMudhra, an Indian certificate authority, were weak enough to be recovered. eMudhra says its systems were not breached: a step in an April 2025 key ceremony produced a second, weak set of keys, and those were the ones published. Anyone who recovered them could issue an HTTPS certificate for any site that clients would accept.

Everything here comes from public reporting, linked at the end. We could not open every primary page from our environment, so check them.

## What happened, briefly

- A researcher reported the problem to Google's Chrome Root Program on 17 October 2026.
- Chrome, Mozilla, Apple and Microsoft blocked the eight intermediates between 17 and 20 October. Mozilla also removed the emSign ECC Root CA G3.
- CERT-In (advisory CIAD-2026-0050) said that, as of 21 October, nothing confirmed malicious use. No certificates under these intermediates were found in Certificate Transparency logs before the block.
- MeitY said the impact on Indian sites was very limited and brief, and that eMudhra's DSC and eSign services regulated by the CCA were unaffected.

## Browsers were fast. Servers are the gap.

Browsers check Certificate Transparency and receive revocation lists from their vendors. Most server software does neither. A Node.js, Python, Go or Ruby program trusts whatever its own certificate bundle trusts, and usually never asks whether a certificate was revoked.

That matters for a system like Parmana, which runs on a server and makes outbound HTTPS calls on behalf of agents: to connected systems such as HubSpot, GitHub and Slack, to registered connector endpoints, to its database and to its key service. A client that still trusts the bad intermediates could be shown a forged certificate by anyone who can get between it and those systems. Doing that also needs control of DNS or the network path, so it is not easy. The fix is cheap, so it should still be done.

Node.js shipped security releases on 21 October (22.23.4, 24.22.1 and 26.12.1) that reject chains through the compromised keys and update the bundled roots. Python's certifi shipped 2026.10.19.

## What we checked in Parmana

| Where Parmana runs | What we found | What we did |
|---|---|---|
| The Docker image, for self hosting and the published image | Its Node base image was Node 24.22.0, before the fixed release | Re-pinned the base image to Node 24.22.1 (23 October). The published image is rebuilt with the next server release |
| Continuous integration | Installs the newest Node 24 on every run | Nothing needed; it already includes the fix |
| The hosted API | Its hosting provider runs Node 24.21.0, and a redeploy does not change that | The server now removes eMudhra's four emSign root certificates from its trust list at startup, before any outbound connection, so a certificate issued from the weak keys is refused whatever Node version runs it. The production log confirms it: `"node":"v24.21.0"`, `"distrustedRootsRemoved":4` |
| The Python SDK | Uses `requests`, which uses certifi | Users should update certifi to 2026.10.19 or later |

The last row was a surprise. We had expected to check a version number and redeploy. The hosting provider decides which Node patch runs, and on 23 October it was still one release behind the fix. So we stopped relying on the runtime and made the server distrust the roots itself. The cost is that a server whose certificate chains to an emSign root can no longer be reached from Parmana; none of the systems it calls uses one.

If you self host Parmana, rebuild from the current `Dockerfile`; the startup check applies there too. If your host uses the operating system's trust store instead of Node's, update that as well.

**Update, 23 October 2026:** this section now reports what was done, not what was planned.

## What a signature is worth

There is a second lesson, and it is the one closer to what Parmana does.

Parmana signs a record of every action an agent takes and every action it refuses, so that anyone can check later, offline, with only a public key. That promise is exactly as good as the key behind it. eMudhra's keys were held carefully and still failed, because the weakness was introduced when they were created, in a ceremony that nobody caught for eighteen months.

For anyone who signs records, three things follow:

1. **Check the key, not just the custody.** A key in a hardware module is still weak if it was generated weakly. A simple check at startup, refusing a key that is too short or matches a known bad key, catches the crudest failures. Parmana does not have that check today; we are adding it to our list.
2. **Write the ceremony down, and have a second person check it.** How a key is generated, by whom, and how its public half is checked before anyone trusts it. eMudhra's own explanation points at one step of its ceremony.
3. **Plan for the day a key must be withdrawn.** Records signed with a withdrawn key should still be checkable, with a clear statement of what changed and when. We have done this once before, and it is easier to do with the procedure written in advance.

A signature proves that a record has not changed since a key signed it. It does not prove the key was any good. That part is up to the people who make and keep the key.

## Sources

- [Google: Protecting Chrome and Android users from compromised eMudhra intermediate CA certificates](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/)
- [eMudhra: Statement on recent certificate security incident](https://emudhra.com/en/post/certificate-security-incident)
- [The Hacker News: Eight eMudhra CA Keys Compromised](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html)
- [Help Net Security: eMudhra security blunder left trusted CA signing keys exposed](https://www.helpnetsecurity.com/2026/10/21/emudhra-certificates-private-keys-compromised/)
- [Asianet Newsable: eMudhra incident had limited impact on Indian sites, says MeitY](https://newsable.asianetnews.com/business/emudhra-security-incident-had-limited-impact-on-indian-sites-meity-articleshow-a1wfmnz)
- [The Economic Times: Netizens react as IT Ministry says impact on Indian sites very limited](https://economictimes.indiatimes.com/tech/technology/emudhra-breach-netizens-react-as-it-ministry-says-impact-on-indian-sites-very-limited/articleshow/135107533.cms)
- [heise: Node.js fixes its own and inherited security vulnerabilities](https://www.heise.de/en/news/Node-js-fixes-its-own-and-inherited-security-vulnerabilities-11496143.html)
- [Endor Labs: The trust stores you patched, and the ones you did not know you had](https://www.endorlabs.com/learn/emudhra-intermediate-ca-compromise-the-trust-stores-you-patched-and-the-ones-you-didnt-know-you-had)
