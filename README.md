[![DeepSource Issues](https://deepsource.io/gh/vapronva/goxor_store-website_troll.svg/?label=active+issues&show_trend=true&token=yvH-TF3qsL8rAlqw7RPQT8ly)](https://deepsource.io/gh/vapronva/goxor_store-website_troll/?ref=repository-badge)
[![API Uptime](https://status.vapronva.pw/api/v1/endpoints/websites-goxorstore_goxor-store-backend-url-ping-internal/uptimes/7d/badge.svg)](https://status.vapronva.pw/endpoints/websites-goxorstore_goxor-store-backend-url-ping-internal)
[![Website Uptime](https://status.vapronva.pw/api/v1/endpoints/websites-goxorstore_goxor-store-frontend-url-ping/uptimes/7d/badge.svg)](https://status.vapronva.pw/endpoints/websites-goxorstore_goxor-store-frontend-url-ping)
[![Continuous Integration](https://gitlab.vapronva.pw/vapronva/goxor_store-website_troll/badges/main/pipeline.svg)](https://gitlab.vapronva.pw/vapronva/goxor_store-website_troll/pipelines/latest)
[![Time Spent on the Project](https://wakapi.vapronva.pw/api/badge/vapronva/interval:any/project:goxor_store-website_troll)](https://wakapi.vapronva.pw/summary?project=goxor_store-website_troll&interval=any)

# **[goxor.store](https://goxor.store)** — Yet Another Troll Website

> *holy smokes!!!1! guys, all goxor songs that are in making right now are available to download here!11!!*

## Why?

The domain registrar I use gifted me a `.store` for free.\
Huh, that's pretty cool. But what should I do with it?

That's when [middle of May 2022] Geoxor (a music artist) began to publish small snippets of the upcoming *Zenith* release. One day, such a snippet contained a rickroll.\
Additionally, there's a joke going around for calling him "goxor".\
Moreover, earlier this year I created [thats-a-nice-argument-unfortunately.com](https://thats-a-nice-argument-unfortunately.com).

All those things and thoughts have emerged into `goxor.store`.

## What?

Upon visiting the website, a personal audio message is generated containing information about one's geographical location based on the IP address.

## How?

The repository is divided into two parts: the *website* and the *API*.

### Website

The website is assembled with Bootstrap 5 on an almost pure HTML and CSS.
Animations are done through CSS via combination of 3rd-party librares and are intiated through simple JavaScript.

Everything's served via beloved Flask in Python.

### API

The API is built in Python with FastAPI.\
It was written in under 3 hours, and is not meant to be a production-ready solution or something to show off.

Speech-to-text utilizes [Yandex's SpeechKit](https://cloud.yandex.com/services/speechkit) technology. It isn't very good at English (rather "ok", would say) (and I couldn't use others, since, you know, "current world situation"), though accomplishes stunning results in Russian.

### Docker & Proxy

Everything is deployed in Docker containers.

Routed via the Traefik proxy on the server, goes through Coraza WAF on the other, straight into Caddy on another one.
