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
| `venue` | Publication venue, `arXiv`, or `Publication venue not recorded`. |
| `paper_url` | Publisher, DOI, or arXiv page. |
| `doi` | Optional DOI without its URL prefix. |
| `arxiv_id` | Optional arXiv identifier. |
| `code_url` | Optional official implementation link. |
| `data_url` | Optional official dataset link. |
| `note` | Optional note about the paper's relevance or resources. |

Use UTF-8 CSV and quote fields containing commas. Include a full record in each applicable category. Run `python scripts/build.py` to refresh the reading lists after editing.
