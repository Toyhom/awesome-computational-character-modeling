# Literature catalogs

| Directory | Survey chapter |
| :-- | :-- |
| [methods](methods/) | III. Behavioral-Science-Informed Role Modeling |
| [data](data/) | IV. Character Information and Data Foundations |
| [evaluation](evaluation/) | V. Evaluation of Computational Characters |

Find individual lists in the [literature directory](../literature/README.md). To suggest a paper or submit an edit, follow [How to contribute](../CONTRIBUTING.md).

## CSV fields

| Field | Content |
| :-- | :-- |
| `id` | A citation key, unique within this category. Reuse an existing paper's key where possible. |
| `title` | Full paper title. |
| `authors` | Author names separated by `; `. |
| `year` | Four-digit publication year. |
| `venue` | Conference abbreviation and year (e.g. `ACL 2025`), journal abbreviation (e.g. `TPAMI`), book publisher, `arXiv`, or `Publication venue not recorded`. |
| `paper_url` | Publisher, DOI, or arXiv page. |
| `doi` | Optional DOI without its URL prefix. |
| `arxiv_id` | Optional arXiv identifier. |
| `code_url` | Optional official implementation link. |
| `data_url` | Optional official dataset link. |
| `note` | Optional note about the paper's relevance or resources. |

Use UTF-8 CSV and quote fields containing commas. Include a full record in each applicable category. Run `python scripts/build.py` to refresh the reading lists after editing.

## Venue format

| Publication type | Format | Example |
| :-- | :-- | :-- |
| Conference | Abbreviation and conference year | `ACL 2025`, `EMNLP 2024`, `NeurIPS 2023` |
| Findings | Conference and year, followed by `(Findings)` | `ACL 2025 (Findings)` |
| Industry track | Conference and year, followed by `(Industry)` | `EMNLP 2024 (Industry)` |
| Workshop | Workshop abbreviation and year, followed by `(Workshop)` | `PERSONALIZE 2024 (Workshop)` |
| Journal | Established acronym or abbreviated title | `TPAMI`, `TACL`, `CACM`, `CHBAH`, `Psychol. Rev.` |
| Preprint | Repository name | `arXiv` |
| Book or book chapter | Publisher or abbreviated book-series title | `Academic Press`, `Adv. Exp. Soc. Psychol.` |

Use the conference year rather than its edition number or proceedings volume. For conference papers in a book series such as LNCS, identify the actual conference. Omit repeated acronyms, `Proceedings of`, and long-paper volume labels. For a published paper, use its publication year in `year`, even if an earlier preprint has a different year. Keep single-word journal titles such as `Information` as they are.

Each category stores its own complete venue value. The generated README, detailed lists, and exports display that value directly.
