# Developing on ERPNext

## Why core is not in this repo

Frappe and ERPNext are GPLv3 and live at `github.com/frappe/frappe` and
`github.com/frappe/erpnext`. We deliberately **do not fork them**. If you fork
core and edit it, every upstream release turns into a merge conflict against your
own changes and upgrades become painful.

| Piece | Where it lives | How it updates |
|---|---|---|
| Frappe + ERPNext core | the official `frappe/erpnext` Docker image | bump `ERPNEXT_VERSION` in `/opt/erpnext/Dockerfile`, rebuild |
| **Our code** | **this repo**, at `/opt/erpnext/apps/ai_agentic_demo` | `git push` → `deploy.sh` on the server |

This is the same split as the Odoo side (`odoo-custom-addons`), with one
difference worth understanding.

## Why there is a Dockerfile at all

Odoo picks up an addons directory just by being pointed at it. Frappe does not.
A Frappe app has to be **importable by the bench's virtualenv** — `apps/<name>`
reaches `sys.path` through an editable install (a `.pth` file in
`env/lib/python3.14/site-packages`), not by sitting in the `apps` folder. Mount
the app without that and `import ai_agentic_demo` simply fails.

So `/opt/erpnext/Dockerfile` layers one thing onto the official image:

```dockerfile
FROM frappe/erpnext:${ERPNEXT_VERSION}
COPY --chown=frappe:frappe apps/ai_agentic_demo /home/frappe/frappe-bench/apps/ai_agentic_demo
RUN cd /home/frappe/frappe-bench && env/bin/pip install --no-cache-dir -e apps/ai_agentic_demo
```

The compose file **also** bind-mounts the host clone over that same path. The
baked copy registers the app on `sys.path`; the bind mount is what actually runs.
That means:

- **Python changes** → `git pull` + restart. No rebuild.
- **New app, or an ERPNext version bump** → rebuild (`deploy.sh -b`).

The `configurator` service regenerates `sites/apps.txt` with `ls -1 apps` on every
`docker compose up`, so a new app is registered with the bench automatically. It
still has to be installed **per site**.

## Shipping a change

```bash
git add -A && git commit -m "..." && git push       # from this repo
ssh contabo-tally '/opt/erpnext/deploy.sh'          # Python only
ssh contabo-tally '/opt/erpnext/deploy.sh -m'       # + bench migrate
ssh contabo-tally '/opt/erpnext/deploy.sh -b -m'    # + rebuild the image
```

Use `-m` whenever you add or change a DocType, a Custom Field, or a patch —
that's what runs the schema migration and re-syncs fixtures.

The server pulls over a **deploy key** (`/root/.ssh/erpnext_deploy`, ssh alias
`github-erpnext`), because this repo is private. Deploy keys are unique per repo
across all of GitHub — if adding one ever returns `422 key is already in use`,
generate a fresh keypair rather than reusing an existing one.

## Extending stock DocTypes

Frappe has no equivalent of Odoo's view inheritance. To add a field to a stock
DocType you ship a **Custom Field**, and the reproducible way to do that is an
`after_install` hook calling `create_custom_fields` — see `install.py`. Exporting
a fixture from a live site works too, but then the definition lives in whatever
site you happened to export from, not in this repo.

## Server notes

- The ERPNext **app** is at <https://erp.ai-agentic-enterprises.com>.
- <https://erp-chat.ai-agentic-enterprises.com> is the **read-only chatbot**, a
  separate Next.js app (`/opt/erpnext-chat`) with its own passcode login.
- The stack listens only on `127.0.0.1:8080`; Caddy is the only thing exposed.
- Site name is `frontend` (not a domain). `FRAPPE_SITE_NAME_HEADER: frontend`
  makes nginx serve it for any Host, which is what makes that work behind Caddy.
- `/opt/erpnext/docker-compose.yml` came from frappe_docker's `pwd.yml`, which is
  a *quickstart* file. It hardcoded `admin` as both the MariaDB root password and
  the site admin password, published 8080 on all interfaces, and used
  `deploy: restart_policy` — a **Swarm** key that Compose degrades to
  `on-failure`, which does not bring containers back after a host reboot. All
  fixed; don't re-import it from upstream without redoing those.
