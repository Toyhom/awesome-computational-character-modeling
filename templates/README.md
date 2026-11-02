<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Awesome Computational Character Modeling — a behavioral science perspective on role-playing agents">
</p>

# {{title}}

**Role-playing agents through a behavioral science perspective.**

A reading list accompanying **{{survey_title}}**, by **Yihong Tang, Kehai Chen, and Min Zhang**.

Explore how character behavior is modeled, what information supports it, and how it is evaluated. The organization follows the survey's chapters and subsections: **role modeling → data foundations → evaluation**.

[Browse the literature directory](literature/README.md) · [Contribute a paper](CONTRIBUTING.md) · [中文维护说明](docs/维护说明.md) · [Download the catalog](exports/catalog.csv)

**{{unique}} distinct references · {{records}} category records · {{categories}} independent lists**<br>
Initial collection: the survey corpus frozen on **{{cutoff}}**. Cross-category entries are maintained independently, with full metadata in every category.

{{overview}}

## Contents

{{toc}}

{{catalog}}

## Keep the collection growing

1. Open the relevant CSV under [`catalog/`](catalog/README.md). Each list follows a subsection of the survey.
2. Add the paper's full metadata to that category. Add a separate record to every other relevant category; notes and links can differ between categories.
3. Run `python scripts/build.py` to refresh this page, the detailed lists, category bibliographies, and downloadable catalog.

Run the generator locally after editing a category. A ready-to-install [GitHub Actions workflow](automation/README.md) also supports regeneration on `main` and validation on pull requests. See [Contributing](CONTRIBUTING.md) for the editing workflow.

## About the survey

**Computational Character Modeling: A Survey of Role-Playing Agents from a Behavioral Science Perspective**<br>
Yihong Tang · Kehai Chen · Min Zhang

The initial lists follow the manuscript's citations and inventory tables. Each record identifies its original subsection or table in the `source` field. [Import provenance](docs/PROVENANCE.md) describes the initial export; [the manuscript bibliography snapshot](references/survey.bib) preserves the original reference list.

## Acknowledgments

The community reading-list format was inspired by [LLM Role-Playing/Persona Papers and Resources](https://github.com/Neph0s/awesome-llm-role-playing-with-persona). The organization and initial records in this repository come from our survey manuscript and its bibliography.

## License

Repository tooling and original documentation are available under the [MIT License](LICENSE). Bibliographic facts identify the cited works; rights in the papers and linked resources remain with their respective owners.
