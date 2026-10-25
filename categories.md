---
layout: default
title: Categories
description: Every topic on the Parmana blog, with the posts in each.
---
<h1>Categories</h1>
<p class="lede">Each topic lists its posts. Choose a topic to jump to it.</p>
<p class="chips">{% assign cats = site.categories | sort %}{% for cat in cats %}<a class="pill" href="#{{ cat[0] | slugify }}">{{ cat[0] }} ({{ cat[1].size }})</a> {% endfor %}</p>

{% assign cats = site.categories | sort %}{% for cat in cats %}
<section id="{{ cat[0] | slugify }}" class="category">
  <h2>{{ cat[0] }}</h2>
  <ul class="post-list">
  {% for post in cat[1] %}
    <li><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a> <span class="meta">{% if post.series %}<span class="series-label">{{ post.series }}, part {{ post.series_part }}</span> &middot; {% endif %}<time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %B %Y" }}</time></span></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
