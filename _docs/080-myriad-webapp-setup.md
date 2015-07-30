---
title: "Myriad Webapp Setup"
parent: "Myriad Webapp"
---

The Myriad webapp is a [React](http://facebook.github.io/react/) single page application served by Jetty embedded in the Myriad jar.

## Building the Webapp

The application uses [NPM](https://www.npmjs.com/) to manage dependencies and [Gulp](http://gulpjs.com/) to assemble the distribution. The application is served from the `webapp/public` directory. 

To get setup, install `npm` and `gulp` from the webapp directory by executing the following:

```
npm install
gulp
```

## Building a Development Server

The gulp file contains a dev target that launches a node.js webserver, watches the webapp files, and re-assembles them when files change. 

To launch, run the following:

```
gulp dev
```

A browser window should open with the site loaded. If not, specify your localhost with port 8888. 
```
http://localhost:8888
```

{% include startnote.html %}It is helpful to have Myriad setup in Vagrant locally so the API is available. Default values are coded into the dashboard if the Myriad API isn't available.{% include endnote.html %}

