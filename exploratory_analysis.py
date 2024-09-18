# exploratory_analysis.py
import pandas as pd

def load_cleaned_data(file_path):
    return pd.read_csv(file_path)

def summarize_data(df):
    summary = df.describe(include='all')
    print("Summary Statistics:\n", summary)
    
    return summary

def analyze_anxiety_distribution(df):
    anxiety_by_gender = df.groupby('choose_your_gender')['do_you_have_anxiety?'].value_counts()
    anxiety_by_cgpa = df.groupby('what_is_your_cgpa?')['do_you_have_anxiety?'].value_counts()

    print("Anxiety distribution by gender:\n", anxiety_by_gender)
    print("Anxiety distribution by CGPA:\n", anxiety_by_cgpa)

if __name__ == "__main__":
    input_file = 'data/student_mental_health_cleaned.csv'
    df = load_cleaned_data(input_file)
    summarize_data(df)
    analyze_anxiety_distribution(df)
