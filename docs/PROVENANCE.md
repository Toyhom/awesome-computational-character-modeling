# Initial collection provenance

The initial collection follows Chapters III–V of the submission manuscript, **Computational Character Modeling: A Survey of Role-Playing Agents from a Behavioral Science Perspective**.

## Classification

Category membership is imported from the manuscript's citations and tables, without a new topic-classification pass:

- Modeling categories contain the references cited in the corresponding subsection and method table.
- Data categories contain the references cited in each subsection. “Scale and Coverage” also includes the dataset inventory table.
- Evaluation targets use the references cited in each E1–E9 passage. Test settings and scoring protocols follow the manuscript's paragraphs. “Observed benchmark distribution” also includes both benchmark inventory tables.
- “Comparative Synthesis” is retained as a structural subsection. It introduces no new citations in the manuscript, so its editable CSV initially has only the column header.

This preserves all **110 core RPA papers**, plus **33 supporting references** cited in these chapters. A modeling subsection can cite evaluation or theory work as part of its discussion; membership therefore denotes the manuscript's placement, not an exclusive contribution type.

## Metadata

Titles, authors, years, venues, and DOIs were imported from the submission bibliography. arXiv IDs and existing links were supplemented from the workspace's literature catalogs. Code links were included only when explicitly present in the stored paper abstract. Missing links for three classical books were supplemented from publisher or Google Books records. Publication metadata is an inherited snapshot, not a fresh verification of every paper's current status.

Each category contains its own complete metadata rows. Records shared by several categories were copied into each category at initialization and are independently editable afterwards. The generator reads each file as-is and never synchronizes fields across categories.

The `source` column identifies the original subsection or table. [Source hashes](../catalog/import-sources.json) identify the exact input files used for the one-time import. The original [survey bibliography](../references/survey.bib) is an archival snapshot, separate from the editable category records and generated category bibliographies.

## Dates and counts

- Survey corpus cutoff: **2026-07-16**, Asia/Shanghai.
- Repository initialization: **2026-11-02**, Asia/Shanghai.
- Counts in the README are computed from the current category files. Distinct-reference counts use citation IDs; category-record counts include separate occurrences of the same paper.

The downloadable CSV preserves every category occurrence. It can be searched by category, citation ID, year, title, venue, or link without modifying the underlying catalogs.
