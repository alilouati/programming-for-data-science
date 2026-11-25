# Programming for Data Science

Course material for **Programming for Data Science** (Master of Data Science) by Dr. Ali Louati.

Every chapter has a **slide deck** (PowerPoint and PDF) and **Jupyter notebooks** you can run in your browser with **Google Colab**: click a badge, then **File → Save a copy in Drive**. Nothing to install.

## Chapters

| # | Chapter | Slides | Lecture | Exercises |
|---|---|---|---|---|
| 0 | Getting started with Colab and Jupyter | [PDF](00_getting_started/slides.pdf) · [PPTX](00_getting_started/slides.pptx) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/00_getting_started/getting_started.ipynb) | in the notebook |
| 1 | Introduction to data science | [PDF](01_intro_to_data_science/slides.pdf) · [PPTX](01_intro_to_data_science/slides.pptx) | [notes](01_intro_to_data_science/README.md) | discussion questions |
| 2 | Python essentials for data science | [PDF](02_python_essentials/slides.pdf) · [PPTX](02_python_essentials/slides.pptx) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/02_python_essentials/lecture.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/02_python_essentials/exercises.ipynb) |
| 3 | NumPy and linear algebra | [PDF](03_numpy/slides.pdf) · [PPTX](03_numpy/slides.pptx) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/03_numpy/lecture.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/03_numpy/exercises.ipynb) |
| 4 | Pandas: loading, cleaning and transforming data | [PDF](04_pandas/slides.pdf) · [PPTX](04_pandas/slides.pptx) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/04_pandas/lecture.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/04_pandas/exercises.ipynb) |
| 5 | Visualization and exploratory statistics | [PDF](05_visualization/slides.pdf) · [PPTX](05_visualization/slides.pptx) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/05_visualization/lecture.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/05_visualization/exercises.ipynb) |
| 6 | Real-life case study: road accidents in Al-Kharj, 2022 | [PDF](06_case_study_alkharj_accidents/slides.pdf) · [PPTX](06_case_study_alkharj_accidents/slides.pptx) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alilouati/programming-for-data-science/blob/main/06_case_study_alkharj_accidents/case_study.ipynb) | in the notebook |

The Chapter 6 instructor version with solutions is [`case_study_instructor.ipynb`](06_case_study_alkharj_accidents/case_study_instructor.ipynb).

## Chapter 6 at a glance

A complete project on real data: 365 days of road accidents in Al-Kharj in 2022, inside and outside the city.
Students audit data quality (20 days break basic consistency rules), reshape and enrich the data with a holiday calendar, explore seasonality, compare severity inside and outside the city, and test whether daily accidents can be forecast.

## Datasets

All datasets are in [`data/`](data/) and are loaded by the notebooks directly from GitHub. See [data/README.md](data/README.md).

## Running locally (optional)

```bash
git clone https://github.com/alilouati/programming-for-data-science.git
cd programming-for-data-science
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## License

Course text and notebooks: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code snippets: MIT. See [LICENSE](LICENSE).
