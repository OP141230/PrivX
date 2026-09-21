# PrivX

**Your own private, self-hosted metasearch engine — no tracking, no profiling, no logs.**

PrivX is a personal fork of [SearXNG](https://github.com/searxng/searxng) — packaged with Docker, fronted by Caddy, cached with Valkey — restyled with a fully custom terminal/CRT theme so it looks like it belongs to you.

\---

## 🔗 Live instance

[**privx-xe63.onrender.com/**](https://privx-xe63.onrender.com/)

This is my personal instance, open for anyone to use. If you want to create your own private search engine , follow the [Getting started](#getting-started) section below.

\---

## Why PrivX exists

Regular search engines log your queries, fingerprint your browser, and build a profile of you over time. PrivX aggregates results from 70+ search engines (Google, Bing, DuckDuckGo, Qwant, and more) through SearXNG, strips out tracking, and serves them to you from infrastructure **you** control — nothing leaves your server except the anonymized upstream queries.

## Features

|Feature|Details|
|-|-|
|🔒 Full privacy|No query logging, no user profiling, no ads, no third-party trackers|
|🌐 Aggregated results|Pulls from 70+ engines in one search|
|🖥️ Custom terminal UI|Black background, phosphor-green monospace theme, CRT scanline overlay, blinking cursor|
|🔁 Reverse proxy included|Caddy handles HTTPS/TLS automatically|
|⚡ Fast caching|Valkey (Redis-compatible) in-memory cache|
|🐳 One command deploy|`docker compose up -d` and you're live|
|🧩 Fully customizable|Branding, theme, and templates are plain files you can edit|

## Stack

|Component|Role|Image|
|-|-|-|
|[Caddy](https://github.com/caddyserver/caddy)|Reverse proxy, automatic HTTPS via Let's Encrypt|`docker.io/library/caddy:2-alpine`|
|[SearXNG](https://github.com/searxng/searxng)|Metasearch engine core|`docker.io/searxng/searxng:latest`|
|[Valkey](https://github.com/valkey-io/valkey)|In-memory cache (Redis-compatible)|`docker.io/valkey/valkey:8-alpine`|

\---

## Getting started

### 1\. Prerequisites

* [Docker](https://docs.docker.com/install/) and Docker Compose installed
* A Linux/macOS/WSL shell (Windows users, see the PowerShell note below)

### 2\. Clone this repo

```shell
git clone https://github.com/<your-username>/PrivX.git
cd PrivX
```

### 3\. Set your hostname

Edit `.env`:

```env
SEARXNG\\\_HOSTNAME=localhost        # or your domain, e.g. search.yourdomain.com
LETSENCRYPT\\\_EMAIL=you@example.com # only needed if using a real domain + TLS
```

> ⚠️ \\\*\\\*Before you push this repo publicly\\\*\\\*, make sure `.env` doesn't contain your real email or any personal info you don't want on GitHub. Consider adding `.env` to `.gitignore` and committing an `.env.example` template instead.

### 4\. Generate a fresh secret key

Don't reuse the key that ships in this repo — generate your own.

```shell
sed -i "s|^\\\\(\\\\s\\\*secret\\\_key:\\\\s\\\*\\\\).\\\*|\\\\1\\\\"$(openssl rand -hex 32)\\\\"|" searxng/settings.yml
```

On macOS:

```shell
sed -i '' "s|^\\\\(\\\\s\\\*secret\\\_key:\\\\s\\\*\\\\).\\\*|\\\\1\\\\"$(openssl rand -hex 32)\\\\"|" searxng/settings.yml
```

> \\\NOTE
> Windows (PowerShell):
> ```powershell
> $randomBytes = New-Object byte\\\[] 32
> (New-Object Security.Cryptography.RNGCryptoServiceProvider).GetBytes($randomBytes)
> $secretKey = -join ($randomBytes | ForEach-Object { "{0:x2}" -f $\\\_ })
> (Get-Content searxng/settings.yml) -replace '"\\\[0-9a-f]{32,}"', "`"$secretKey`"" | Set-Content searxng/settings.yml
> ```

### 5\. Run it

**Option A — with Caddy (recommended, handles HTTPS for you):**

```shell
docker compose up -d
```

Visit `http://localhost:8080` (or your domain if you set one).

**Option B — bring your own reverse proxy (Nginx, HAProxy, etc.):**

1. Remove the `caddy` service and its volumes from `docker-compose.yaml`
2. Point your reverse proxy at the `searxng` service's port (`8080` by default)
3. Configure TLS on your own proxy
4. `docker compose up -d`

\---

## Customizing the look

The terminal theme isn't baked into the SearXNG image — it's layered on at runtime via Docker volume mounts, so it's easy to tweak without rebuilding anything:

|What you want to change|File|
|-|-|
|Colors, fonts, scanline intensity, layout|`searxng/custom.css`|
|Instance name / branding text|`searxng/settings.yml` → `general.instance\\\_name`|
|Logo markup / page structure|`searxng/templates/simple/base.html`, `page\\\_with\\\_header.html`|
|About page content|`searxng/infopage/en/about.md`|
|Search engines enabled, safe search, autocomplete, etc.|`searxng/settings.yml`|

After editing, restart the `searxng` container to pick up changes:

```shell
docker compose restart searxng
```

If your CSS changes don't seem to apply, hard-refresh the browser (`Ctrl/Cmd + Shift + R`) — browsers cache stylesheets aggressively.

> \\\*\\\*Note on the CSS mount:\\\*\\\* `docker-compose.yaml` mounts `custom.css` directly over SearXNG's compiled stylesheet files (`sxng-ltr.min.css` / `sxng-rtl.min.css`, plus their `.gz`/`.br` compressed variants), rather than adding an extra stylesheet. This means the mounted file fully \\\*replaces\\\* the default theme — which is why `custom.css` here is a complete stylesheet rather than a short list of overrides. If a future SearXNG image release renames these compiled files, check the page's `<link rel="stylesheet">` tag in your browser's dev tools and update the volume mount paths in `docker-compose.yaml` to match.

\---

## Updating

Pull the latest SearXNG image and restart:

```shell
git pull
docker compose pull
docker compose up -d
```

## Logs \& troubleshooting

All containers:

```shell
docker compose logs -f
```

Individual containers:

```shell
docker compose logs -f caddy     # reverse proxy
docker compose logs -f searxng   # search engine
docker compose logs -f redis     # cache (Valkey)
```

## Running as a systemd service (optional)

```shell
cp searxng-docker.service.template PrivX.service
```

1. Edit `WorkingDirectory` in `PrivX.service` to match your install path
2. Enable it: `systemctl enable $(pwd)/PrivX.service`
3. Start it: `systemctl start PrivX.service`

## Supported architectures

* `amd64`
* `arm64`
* `arm/v7`

\---

## Credits

PrivX is built on top of:

* [searxng/searxng-docker](https://github.com/searxng/searxng-docker) — the Docker Compose base (Caddy + Valkey + SearXNG wiring) this project started from
* [searxng/searxng](https://github.com/searxng/searxng) — the metasearch engine itself

All PrivX adds is the branding, the terminal/CRT theme, and configuration tweaks on top of that foundation.

## License

This project inherits the [GNU AGPLv3](LICENSE) license from SearXNG. See [LICENSE](LICENSE) for the full text.

