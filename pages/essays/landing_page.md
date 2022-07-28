---
title: Essays
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Essays
menuTopIndex: 1
---

<ul>
{% for essay in site.pages %}
{% if essay.layout == "essay" and essay.menuInclude == "yes" %}
<li> <a href="{{essay.url}}">{{essay.title}}</a></li>
{% endif %}
{% endfor %}
</ul>
