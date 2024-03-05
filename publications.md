---
layout: single
collection: publications
author_profile: true
classes: wide
---

You can find an up-to-date list on my [Google Scholar profile](https://scholar.google.nl/citations?user=Uq5KrMoAAAAJ&hl=en).<br/>
<a class="btn btn--info" onclick="$('.screenshot').toggle()" ><i class="fas fa-images" aria-hidden="true"></i> Toggle screenshots</a>

{% assign pubs_by_year = site.publications | group_by: "year" | sort: "name" | reverse %}
{% for y in pubs_by_year %}
{% assign currentyear = y.name %}
## {{currentyear}}

{% assign pubs_by_order = y.items | sort: _order | reverse %}
{% for pub in pubs_by_order %}
- {% include citation.html pub=pub %}
  {%- if pub.screenshot -%}<br/>[<img class="screenshot" src='../{{pub.screenshot}}' width="200px" alt="{{pub.title}}"/>](../{{pub.screenshot}}){%- endif -%}
{% endfor %}
{% endfor %}
