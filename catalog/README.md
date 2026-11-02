# Editable literature catalogs

These category files are the editable sources for the reading lists. Each category owns its complete records, including title, authors, year, venue, links, and notes.

| Directory | Manuscript chapter |
| :-- | :-- |
| [methods](methods/) | III. Behavioral-Science-Informed Role Modeling |
| [data](data/) | IV. Character Information and Data Foundations |
| [evaluation](evaluation/) | V. Evaluation of Computational Characters |

Use the [full category index](../literature/README.md) to jump to a CSV, a detailed reading list, or a category bibliography.

The same paper may appear in multiple CSVs with independently edited metadata. `structure.json` supplies ordering and headings only; it is not a central paper database. `import-sources.json` records the manuscript file hashes used for the initial export.

Run `python scripts/build.py` after editing. See [Contributing](../CONTRIBUTING.md) or [中文维护说明](../docs/维护说明.md).
