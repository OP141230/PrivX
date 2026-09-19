FROM searxng/searxng:latest

# --- Settings (instance name, privacy options, etc.) ---
COPY ./searxng/settings.yml /etc/searxng/settings.yml

# --- PrivX theme ---
# These REPLACE the compiled stylesheets (same as the volume mounts in
# docker-compose.yaml) rather than appending to them. Must overwrite the
# raw file AND its .gz/.br precompressed siblings, or the server will
# keep serving the old (default) compressed copies instead of your CSS.
COPY ./searxng/custom.css    /usr/local/searxng/searx/static/themes/simple/sxng-ltr.min.css
COPY ./searxng/custom.css    /usr/local/searxng/searx/static/themes/simple/sxng-rtl.min.css
COPY ./searxng/custom.css.gz /usr/local/searxng/searx/static/themes/simple/sxng-ltr.min.css.gz
COPY ./searxng/custom.css.gz /usr/local/searxng/searx/static/themes/simple/sxng-rtl.min.css.gz
COPY ./searxng/custom.css.br /usr/local/searxng/searx/static/themes/simple/sxng-ltr.min.css.br
COPY ./searxng/custom.css.br /usr/local/searxng/searx/static/themes/simple/sxng-rtl.min.css.br

# --- PrivX branding ---
# The wordmark, ">" prompt, blinking cursor, and nav text live in these
# templates, not in CSS. Without this, the logo still reads "SearXNG"
# regardless of how the stylesheet looks.
COPY ./searxng/templates/simple/base.html             /usr/local/searxng/searx/templates/simple/base.html
COPY ./searxng/templates/simple/page_with_header.html  /usr/local/searxng/searx/templates/simple/page_with_header.html
COPY ./searxng/infopage/en/about.md                    /usr/local/searxng/searx/infopage/en/about.md

EXPOSE 8080
