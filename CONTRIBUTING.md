# Contributing

The reading lists follow the survey's structure. Find a destination in the [literature directory](literature/README.md) and edit its linked CSV.

## Add or update a paper

1. Edit a category CSV under `catalog/methods/`, `catalog/data/`, or `catalog/evaluation/`.
2. Supply the complete metadata for that occurrence. Use the same citation ID when the paper already appears elsewhere, and add a category-specific note when useful.
3. If the paper belongs to several categories, add a complete row to each CSV. Each copy is independently maintained. Editing one copy leaves the others unchanged.
4. Generate and validate the outputs:

```sh
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

Python 3.10 or later is sufficient; the scripts have no third-party dependencies. Run these commands from the repository root. Commit the edited CSVs together with the generated outputs.

You can also edit a CSV directly on GitHub, then pull the changes and run the generator locally. To enable regeneration on `main` and checks on pull requests, install the prepared workflow following [these instructions](automation/README.md).

## Record fields

| Field | Required | Meaning |
| :-- | :-- | :-- |
| `id` | Yes | Citation ID, unique **within this category**. Reuse the same ID across categories when possible. |
| `title` | Yes | Full paper title. |
| `authors` | Yes | Author names separated by `; `. |
| `year` | Yes | Four-digit publication year. |
| `venue` | Yes | Venue, `arXiv`, or `Publication venue not recorded`. |
| `paper_url` | Recommended | DOI landing page, publisher page, or arXiv abstract URL. |
| `doi` | No | DOI without the `https://doi.org/` prefix. |
| `arxiv_id` | No | arXiv identifier, such as `2310.00746`. |
| `code_url` | No | Verified official implementation. |
| `data_url` | No | Verified dataset or resource landing page. |
| `note` | No | Why the work is relevant to **this category**, or a resource name. |
| `source` | Yes | For existing entries: manuscript subsection/table. For additions: source supporting inclusion, such as the paper's section or project page. |
| `added` | Yes | Date this occurrence was added, in `YYYY-MM-DD` format. |

Use UTF-8 CSV. Quote fields containing commas or line breaks; double embedded quotation marks. Blank optional fields are valid. Avoid replacing unknown information with a guessed venue, URL, or release status.

## Category structure

`catalog/structure.json` records the manuscript's chapter and subsection order. Each leaf points to one independent CSV. Make structural changes when the survey's organization changes. New papers can be added to the existing lists without editing this structure.

`templates/README.md` contains the introduction and reusable page text. `scripts/build.py` reads it together with the category files to generate:

- `README.md` — all category lists, navigation, and counts;
- `literature/` — detailed records and one BibTeX file per category;
- `exports/catalog.csv` — all category occurrences, with duplicates across categories preserved;
- `exports/stats.json` — counts of references and category occurrences.

The generator never writes to a category CSV. It allows metadata differences between categories, and checks accidental duplicates only within an individual category.

## Suggest a paper

Use the “Suggest a paper” issue form with the paper link, relevant survey subsections, and a short explanation of fit. A contribution may belong to multiple lists.
