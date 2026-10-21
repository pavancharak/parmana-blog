---
layout: home
title: Parmana Blog
---

Technical notes on AI governance, authorization and verifiable execution.

## Posts

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}), {{ post.date | date: "%-d %B %Y" }}
{% endfor %}
