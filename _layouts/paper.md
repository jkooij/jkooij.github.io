---
layout: single
collection: papers
author_profile: true
classes: wide
---
{% comment %}
Layouts do not support Markdown, se need a "capture+markdownify" hack
https://github.com/jekyll/jekyll/issues/6166#issuecomment-322771527
{% endcomment %}
{% capture md %}

{% include citation.html pub=page notitle=true noinfo=true %}

{% if page.youtube -%}<br/>
 <iframe width="560" height="315" src="https://www.youtube.com/embed/{{page.youtube}}" title="{{page.title}}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
{%- endif %}
{% if page.screenshot -%}<br/>[<img class="screenshot" src='../../{{page.screenshot}}' width="400px" alt="{{page.title}}"/>](../../{{page.screenshot}}){%- endif %}

## Cite this work


{% if page.journal %}
```bibtex
@article{ {{- page.key -}} ,
    title={%raw%}{{{%endraw%} {{- page.title -}} {%raw%}}}{%endraw%},
    author={ {{- page.authors | split: ", " | join: " and " -}} },
    journal={ {{- page.journal -}} },
    volume={ {{- page.volume -}} },
    number={ {{- page.number -}} },
    pages={ {{- page.pages -}} },
    year={ {{- page.year -}} },
    doi={ {{- page.doi -}} },
}
```
{% else %}
```bibtex
@inproceedings{ {{- page.key -}} ,
    title={%raw%}{{{%endraw%} {{- page.title -}} {%raw%}}}{%endraw%},
    authors={ {{- page.authors | split: ", " | join: " and " -}} },
    booktitle={ {{- page.booktitle -}} },
    pages={ {{- page.pages -}} },
    year={ {{- page.year -}} },
    doi={ {{- page.doi -}} },
}
```
{% endif %}

{% endcapture %}
{{ md | markdownify }}
