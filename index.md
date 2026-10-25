---
layout: default
title: Latest posts
description: Technical notes on how Parmana checks every action and keeps proof of what happened.
---
<h1>Latest posts</h1>
<p class="lede">Practical notes on how Parmana checks every action, what we tested, and what is still open.</p>
<p>Browse by topic on the <a href="{{ '/categories/' | relative_url }}">categories page</a>, or <a href="{{ '/search/' | relative_url }}">search the blog</a>.</p>

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <p class="meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %B %Y" }}</time>{% for c in post.categories %} <a class="pill" href="{{ '/categories/' | relative_url }}#{{ c | slugify }}">{{ c }}</a>{% endfor %}</p>
    <p>{{ post.description }}</p>
  </li>
{% endfor %}
</ul>
