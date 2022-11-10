---
title: Fictions
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Fictions
menuTopIndex: 2
---

<ul>
{% for fiction in site.pages %}
{% if fiction.layout == "fiction" and fiction.menuInclude == "yes" %}
<li> <a href="{{fiction.url}}">{{fiction.title}}</a></li>
{% endif %}
{% endfor %}
</ul>