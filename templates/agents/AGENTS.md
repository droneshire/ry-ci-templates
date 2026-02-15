# AGENTS

## Development Loop

1. `make format`
2. `make lint_full`
3. `make test`

## Rules

- Never use deferred imports unless necessary.
- Keep docs in `docs/`.
- Update comments/docstrings when constants change.

## Lessons Learned

- Use repo-local virtualenvs for all installs and checks (`make init_dev`, `source ./venv-dev/bin/activate`, `make install_dev`).
- Internal shared packages should be typed:
  - include `py.typed` in package sources
  - include `py.typed` in package data at build time
- Prefer fixing package typing at source over adding broad `ignore_missing_imports` in consumers.
- PyPI Trusted Publishing requires exact claim matches (owner/repo/workflow/branch); no API token password when using OIDC.
- Use `skip-existing: true` in publish workflow to avoid duplicate-version failures.
- Trigger publish workflow from successful `Python Application` runs on `main` pushes.
- Add `make release` to package repos to bump patch version, commit, and push from clean `main`.
- Be careful with automated Makefile replacements; validate with `make -n lint_full`.
- Keep formatter commands batched by default; avoid per-file loops unless strictly necessary.
