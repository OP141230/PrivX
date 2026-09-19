FROM searxng/searxng:latest

# Copy settings
COPY ./searxng/settings.yml /etc/searxng/settings.yml

# Append custom CSS directly into all SearXNG theme files
COPY ./searxng/custom.css /usr/local/searxng/searx/static/themes/simple/css/custom.css
RUN cat /usr/local/searxng/searx/static/themes/simple/css/custom.css >> /usr/local/searxng/searx/static/themes/simple/css/searxng.min.css || true
RUN cat /usr/local/searxng/searx/static/themes/simple/css/custom.css >> /usr/local/searxng/searx/static/themes/simple/css/sxng-ltr.min.css || true

EXPOSE 8080
