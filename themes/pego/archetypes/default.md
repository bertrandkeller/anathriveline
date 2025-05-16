---
title: {{ replace .Name "-" " " | title }}
seo_title: {{ replace .Name "-" " " | title }}
description: 
slug: {{ .Name }}
author: {{ .Site.Params.author }}

draft: true
dateold: "{{ .Date }}"

newsletter: true
---

