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

The task can be run locally, I suggest using a virtual environment (in my case I used Conda) install the environment.yml file, and activate the
environment. 

### 1. Unzip & Navigate

Download and unzip the `gemma_test.zip` file. Then navigate into the project folder:

```bash
cd gemma_test
```

### 2. Set up a virtual environment
Created using Conda. You can recreate it with:

```bash
conda env create -f environment.yml
conda activate gemma_test # Install dependencies
```

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt # Install dependencies
```

### 3. Run it

```bash
jupyter notebook notebooks/01_analysis.ipynb
```

### Notes 

- All SQL logic is stored in separate .sql files for reuse and modularity.
- It's supposed to not be OS-specific or Conda-only commands to be required.
- I tried to stick to no more than 2 hours spent in the task; started 18:00 and finished 20:03 CEST 11.07.2025.
- After testing as a user I ran into some issues so I had to implement some changes for simplicity and therefore ended up spending a bit more time on it.  


