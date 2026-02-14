---
layout: single
author_profile: true
collection: publications
title: "Julian Kooij - Research"
classes: wide
header:
    overlay_image: /files/prius_before_library_clean_lp_1350x665.jpg
---

I am an Associate Professor at the [Intelligent Vehicles group](http://intelligent-vehicles.org/), 
part of the [Cognitive Robotics department](http://cor.tudelft.nl/) of the Mechanical Engineering faculty, TU Delft, The Netherlands.
You can find [my staff page](https://www.tudelft.nl/en/staff/j.f.p.kooij/) on the TU Delft website.
I work on multi-modal environment perception for intelligent vehicles, and mostly target crowded urban settings.

# Recent publications

Below are publications from recent years.
A more complete list can be found on the [Publications]({%link publications.md %}) page,
and on my [Google Scholar profile](https://scholar.google.nl/citations?user=Uq5KrMoAAAAJ&hl=en).<br/>
<a class="btn btn--info" onclick="$('.screenshot').toggle()" ><i class="fas fa-images" aria-hidden="true"></i> Toggle screenshots</a>

{% assign pubs_by_year = site.publications | group_by: "year" | sort: "name" | reverse | slice: 0, 2 %}
{% for y in pubs_by_year %}
{% assign currentyear = y.name %}
## {{currentyear}}

{% assign pubs_by_order = y.items | sort: "_order" | reverse %}
{% for pub in pubs_by_order %}
- {% include citation.html pub=pub %}
  {%- if pub.screenshot -%}<br/>[<img class="screenshot" src='../{{pub.screenshot}}' width="200px" alt="{{pub.title}}"/>](../{{pub.screenshot}}){%- endif -%}
{% endfor %}
{% endfor %}

List continues on my [Publications]({%link publications.md %}) page.
