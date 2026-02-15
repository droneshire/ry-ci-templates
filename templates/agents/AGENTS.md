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

- Always run tooling in repo venv (`make init_dev`, `source ./venv-dev/bin/activate`, `make install_dev`).
- Shared internal packages should publish typing metadata (`py.typed` + package-data).
- For Trusted Publishing, repo/workflow/branch must exactly match PyPI publisher settings.
- Bump versions before publish (`make release`); existing versions cannot be re-uploaded to PyPI.
- After Makefile edits, validate quickly with `make -n lint_full`.
