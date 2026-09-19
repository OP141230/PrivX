FROM searxng/searxng:latest

# Copy custom settings and theme CSS overlay into SearXNG container
COPY ./searxng/settings.yml /etc/searxng/settings.yml
COPY ./searxng/custom.css /usr/local/searxng/searx/static/themes/simple/css/sxng-ltr.min.css

EXPOSE 8080
