# How to contribute

We welcome relevant papers, missing resources, and corrections. Choose either of the options below. Maintainers review submissions before adding them to the collection.

## Suggest a paper — no coding required

1. Sign in to GitHub and open the [Suggest a paper form](https://github.com/Toyhom/awesome-computational-character-modeling/issues/new?template=paper.yml).
2. Enter the paper's title and link.
3. Name the relevant category or categories and briefly explain why the paper belongs there. Include official code or data links if available.
4. Click **Submit new issue**. A maintainer will review the suggestion and add the paper if it fits the collection.

An issue is a suggestion for the maintainers; it does not change the literature list automatically.

## Submit a prepared change — for GitHub users

1. Click **Fork** at the top of the repository to create a copy under your account.
2. In your copy, find the relevant category CSV using the [literature directory](literature/README.md).
3. Add or correct the paper's metadata and save your changes. For a paper relevant to several categories, add a complete row to each applicable CSV.
4. If you have Python 3.10 or later, run `python scripts/build.py` to update the reading lists. Otherwise, submit the CSV changes and a maintainer can regenerate the pages.
5. In your fork, click **Contribute → Open pull request**, then select this repository's `main` branch as the destination. Explain the paper addition or correction and submit the request.
6. A maintainer reviews the changes. They appear in this collection after the pull request is merged.

Forking and submitting a pull request do not give you direct editing access to this repository. See GitHub's [contribution guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) for more detail.

## What to include

Supply the full title, authors, year, venue, and a paper link. Official code and dataset links are welcome. Use the existing categories from the survey and include a short category-specific note when useful.

The [catalog field guide](catalog/README.md) explains the CSV columns. Edit the category CSVs; the README and detailed reading lists are generated from them.
