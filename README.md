# Gemma Analytics Test

## Task

Analyze surgical performance data for hip replacement operations. Identify the **most and least skilful surgeons** based on changes in patient health outcomes.

---

## Feature list

1. Connected to PostgreSQL database.
2. Explore schema to identify relevant tables for:
   - Pre- and post-operative questionnaires.
   - Surgeon and patient mapping.
3. Convert questionnaire answers to health scores using `answer_options`.
4. Calculate improvement scores per patient.
5. Aggregate results to rank surgeons.

---

## How to run

The task can be run locally, I suggest using a virtual environment (in my case I used Conda) with the environment.yml file, and activate the
environment. 


### Environment
Created using Conda. You can recreate it with:

```bash
conda env create -f environment.yml
conda activate gemma_test
```

### Run

```bash
jupyter notebook notebooks/01_analysis.ipynb
```

