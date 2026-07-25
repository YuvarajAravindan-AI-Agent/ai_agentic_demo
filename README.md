### AI Agentic Demo

A custom **Frappe/ERPNext app**. This repo holds only our own code — Frappe and
ERPNext core are never forked, so upstream releases stay a clean version bump.

    frappe/erpnext @ v16.29.0   ->  official Docker image (core, untouched)
    this repo                   ->  apps/ai_agentic_demo  (our code)

It currently ships one thing: an **AI Readiness Score** custom field on Customer,
created by the `after_install` hook. Its presence on the Customer form confirms
the app is loading from this repo.

Runs on <https://erp.ai-agentic-enterprises.com>. See [DEVELOPING.md](DEVELOPING.md)
for the dev and deploy loop.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/YuvarajAravindan-AI-Agent/ai_agentic_demo --branch main
bench --site <site> install-app ai_agentic_demo
```

The repo is named after the app on purpose: `bench get-app` derives the directory
in `apps/` from the repo name, and Frappe requires that directory to match
`app_name`. Renaming the repo breaks the standard install path.

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/ai_agentic_demo
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
