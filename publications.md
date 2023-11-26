---
layout: single
collection: publications
author_profile: true
classes: wide
---

You can find an up-to-date list on my [Google Scholar profile](https://scholar.google.nl/citations?user=Uq5KrMoAAAAJ&hl=en).<br/>
<a class="btn btn--info" onclick="$('.screenshot').toggle()" ><i class="fas fa-images" aria-hidden="true"></i> Toggle screenshots</a>

{% assign pubs_by_date = site.publications | sort: "year" | reverse %}
{% for pub in pubs_by_date %}
{% assign paperyear = pub.year %}
{% if paperyear != currentyear %}
## {{paperyear}}

{% assign currentyear = paperyear %}
{% endif %}
- {% include citation.html pub=pub %}
  {%- if pub.screenshot -%}<br/>[<img class="screenshot" src='../{{pub.screenshot}}' width="200px" alt="{{pub.title}}"/>](../{{pub.screenshot}}){%- endif -%}
{% endfor %}
