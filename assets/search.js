(function () {
  var input = document.getElementById('q');
  var list = document.getElementById('results');
  var status = document.getElementById('status');
  if (!input || !list) return;

  function escape(text) {
    return String(text).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function render(posts, query) {
    var terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    var hits = posts.filter(function (p) {
      var haystack = (p.title + ' ' + p.description + ' ' + p.categories.join(' ') + ' ' + p.text).toLowerCase();
      return terms.every(function (t) { return haystack.indexOf(t) !== -1; });
    });
    list.innerHTML = hits.map(function (p) {
      var cats = p.categories.map(function (c) { return '<span class="pill">' + escape(c) + '</span>'; }).join(' ');
      return '<li><a class="post-link" href="' + escape(p.url) + '">' + escape(p.title) + '</a>' +
        '<p class="meta">' + escape(p.date) + ' ' + cats + '</p><p>' + escape(p.description) + '</p></li>';
    }).join('');
    status.textContent = terms.length
      ? hits.length + (hits.length === 1 ? ' post matches' : ' posts match') + ' "' + query + '"'
      : 'Type to search every post.';
  }

  fetch('/search.json')
    .then(function (r) { return r.json(); })
    .then(function (posts) {
      var initial = new URLSearchParams(window.location.search).get('q') || '';
      input.value = initial;
      render(posts, initial);
      input.addEventListener('input', function () { render(posts, input.value); });
    })
    .catch(function () { status.textContent = 'Search is unavailable right now. Browse the categories instead.'; });
})();
