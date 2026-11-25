# Chapter 1: Introduction to data science

This chapter is taught from slides. Below is the updated outline (about 20 slides) with speaker notes, replacing the 2025 deck. Examples from 2011-2015 have been replaced with current ones.

## Learning outcomes

By the end of this chapter, students can

- define data science and explain how it relates to statistics, computer science and domain knowledge;
- describe the steps of the data science lifecycle;
- give examples of data science applications in Saudi Arabia and worldwide;
- name common pitfalls (biased data, pipeline errors, over-interpretation) and ethical issues;
- explain why this course uses Python, Jupyter and Colab.

## Slide outline

| # | Slide | Content and notes |
|---|---|---|
| 1 | Title | Course name, instructor, contact, office hours |
| 2 | Plan | Why data science; what it is; the lifecycle; pitfalls and ethics; course organisation |
| 3 | Data is everywhere | Sources: phones, apps, sensors and IoT, transactions, satellites, health records, government open data. Mention that global data volume is now measured in **hundreds of zettabytes per year** |
| 4 | Why now? | Cheap storage and cloud computing, open-source tools (Python, pandas, scikit-learn), and large models such as ChatGPT that are themselves products of data science |
| 5 | Data science in Saudi Arabia | Vision 2030 and the Saudi Data and AI Authority (SDAIA); the national open data portal; Tawakkalna and the COVID-19 dashboards; smart-city and traffic projects. Link to Chapter 6 (Al-Kharj road accidents) |
| 6 | Data science around the world | Recommender systems (Netflix, YouTube), fraud detection in banking, demand forecasting in retail and logistics, medical imaging, weather and climate models |
| 7 | Definition | Data science combines computer science, statistics and machine learning, visualisation and domain knowledge to collect, clean, integrate, analyse, visualise and communicate data and turn it into decisions or data products |
| 8 | The Venn diagram | Hacking skills + maths and statistics + substantive expertise; the "danger zone" is hacking without statistics |
| 9 | The data science lifecycle | Question → collect → clean → explore → model → evaluate → communicate → deploy and monitor (CRISP-DM style). Most time is spent on cleaning and exploring |
| 10 | Two ways to use data | Exploratory analysis → knowledge → decision; predictive model → evaluation → product |
| 11 | Roles | Data analyst, data scientist, data engineer, machine learning engineer: what each does and which tools they use |
| 12 | Example walk-through | Al-Kharj road accidents: question, data, a chart, a finding, a recommendation (preview of Chapter 6) |
| 13 | What is hard | Surprising results are usually pipeline errors (Kohavi); beware the HiPPO (highest paid person's opinion); overgeneralising; communication; moving from prototype to production |
| 14 | Data does not always make things clearer | A misleading trend extrapolation: a short-lived spike in searches or sales projected forward as a permanent trend. Ask students to spot the flaw |
| 15 | Bias and fairness | Biased training data produces biased models (e.g. face recognition error rates, hiring algorithms). Data reflects how it was collected |
| 16 | Privacy and ethics | Personal data, consent, anonymisation and re-identification; Saudi Personal Data Protection Law (PDPL); responsible use of AI assistants |
| 17 | Reproducibility | Notebooks, version control (Git/GitHub), fixed random seeds, documenting data cleaning decisions |
| 18 | Tools for this course | Python, Jupyter notebooks, Google Colab (no installation), GitHub repository with all material; why Python rather than R, SAS or MATLAB |
| 19 | Course organisation | Chapters 0-6, assessment, exercises notebooks, mini-project, AI-assistant policy |
| 20 | Textbooks | See below |

## Textbooks and resources

Required

- Wes McKinney, *Python for Data Analysis*, 3rd edition (O'Reilly, 2022). Free to read online at <https://wesmckinney.com/book/>.
- Jake VanderPlas, *Python Data Science Handbook*, 2nd edition (O'Reilly, 2022). First edition free online at <https://jakevdp.github.io/PythonDataScienceHandbook/>.

Recommended

- Joel Grus, *Data Science from Scratch*, 2nd edition (O'Reilly, 2019).
- Allen B. Downey, *Think Stats* (free online at <https://greenteapress.com/wp/think-stats/>).

## Discussion questions

1. Name one decision in your organisation that could be improved with data. What data would you need?
2. A model predicts which students will fail a course. What could go wrong, and who could be harmed?
3. Why might two analysts reach different conclusions from the same dataset?
