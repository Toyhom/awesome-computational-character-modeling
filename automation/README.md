# Enable automatic README updates

The repository includes a ready-to-install [GitHub Actions workflow](catalog.yml). The initial publishing credential has repository access but lacks GitHub's `workflow` scope, so the workflow is stored here as a template and is **not active**.

Local generation is fully functional:

```sh
python scripts/build.py
```

To activate automation, use a GitHub session authorized to edit workflows and place the supplied file at `.github/workflows/catalog.yml` on `main`. This can be done in GitHub's web editor, or by moving the file locally and pushing with a credential that has workflow permissions.

After installation, the workflow:

1. Runs the category validation tests.
2. Checks generated outputs on pull requests.
3. Regenerates README, reading lists, BibTeX, and exports on `main`.
4. Commits generated changes using the repository's built-in `GITHUB_TOKEN`.

No external service secrets or package dependencies are required. The generation job requests `contents: write` to commit generated files. Pull-request validation has read-only access.
