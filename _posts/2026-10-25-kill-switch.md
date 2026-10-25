---
layout: post
categories: [Security]
title: "Part 7: Stop every new action at once: the kill switch"
date: 2026-10-25 03:06:00 +0000
series: "Security in practice"
series_part: 7
description: "What the operator kill switch does when it is tripped, how a reset is controlled, and what it does not undo."
---

Part 7 of Security in practice. Part 6 covered the envelope that allows one action. This part covers how an operator stops all new actions at once.

The kill switch is a control an operator can trip to stop new actions quickly. The operations runbook covers how it is set, how it is checked, and how it is reset.

While the switch is tripped, new execution requests are refused. The runbook also describes a setting that requires a second operator to reset the switch.

## What it does not do

The kill switch stops new actions. It does not reverse actions that already ran. Treat it as a stop, and follow your incident process for what has already happened.

## How we checked it

The runbook records the decision that introduced the switch, and the setting that controls the second operator for a reset.

Source: [docs/runbooks/KILL-SWITCH-OPERATIONS.md](https://github.com/pavancharak/parmana-core/blob/main/docs/runbooks/KILL-SWITCH-OPERATIONS.md).
