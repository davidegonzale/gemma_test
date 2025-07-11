import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Streamlit app title
st.title("Surgeon Performance Dashboard: Hip Replacement Outcomes")

# Database connection info (hidden in actual deployment)
db_user = 'c50c162d93e1b19027aafe01f4915371e'
db_pass = 'f1c1e1f88935a9c21b05e200cc938c0c'
db_host = 'candidate-testing.cowkpei4bgel.eu-central-1.rds.amazonaws.com'
db_port = '5432'
db_name = 'hiring_test'

# Connect to the database
@st.cache_resource
def get_engine():
    return create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")

engine = get_engine()

# Load responses and scores
@st.cache_data
def load_data():
    with open("sql/responses_and_scores.sql", "r") as file:
        responses_sql = file.read()
    with open("sql/patient_surgeon_mapping.sql", "r") as file:
        mapping_sql = file.read()

    responses_df = pd.read_sql(responses_sql, engine)
    mapping_df = pd.read_sql(mapping_sql, engine)

    score_sums = (
        responses_df
        .groupby(['patient_id', 'questionnaire_type'], as_index=False)['central_estimate']
        .sum()
    )
    score_sums['health_score'] = 1 - score_sums['central_estimate']

    score_pivot = score_sums.pivot(index='patient_id', columns='questionnaire_type', values='health_score').reset_index()
    score_pivot['improvement'] = score_pivot['post'] - score_pivot['pre']

    merged_df = pd.merge(score_pivot, mapping_df, on='patient_id', how='inner')
    return merged_df

data = load_data()

# Sidebar surgeon selection
surgeons = sorted(data['surgeon_name'].dropna().unique())
selected_surgeons = st.sidebar.multiselect("Select Surgeons to Compare", surgeons, default=['Han Solo', 'Yoda'])

# Filter and show summary
filtered_data = data[data['surgeon_name'].isin(selected_surgeons)]

# Average improvement bar chart
st.subheader("Average Improvement by Surgeon")
avg_improvement = (
    filtered_data.groupby('surgeon_name')['improvement']
    .mean()
    .sort_values(ascending=False)
)
st.bar_chart(avg_improvement)

# Boxplot of distributions
st.subheader("Improvement Distribution by Surgeon")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_data, x='surgeon_name', y='improvement', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Show patient-level table
st.subheader("Patient-Level Data")
st.dataframe(filtered_data[['patient_id', 'pre', 'post', 'improvement', 'surgeon_name']].sort_values(by='improvement', ascending=False).reset_index(drop=True))