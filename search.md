---
layout: default
title: Search
description: Search every post on the Parmana blog by title, topic or text.
---
<h1>Search</h1>
<form class="search" role="search" action="{{ '/search/' | relative_url }}" method="get">
  <label for="q">Search posts</label>
  <input id="q" name="q" type="search" autocomplete="off" placeholder="For example: kill switch, checker, probe">
  <button type="submit">Search</button>
</form>
<p id="status" class="meta" aria-live="polite"></p>
<ul id="results" class="post-list"></ul>
<script src="{{ '/assets/search.js' | relative_url }}"></script>
