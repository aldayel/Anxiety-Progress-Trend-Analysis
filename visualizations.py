# visualizations.py

import pandas as pd
import matplotlib.pyplot as plt

def load_cleaned_data(file_path):
    return pd.read_csv(file_path)

def plot_anxiety_by_gender(df):
    anxiety_by_gender = df.groupby('choose_your_gender')['do_you_have_anxiety?'].value_counts().unstack()

    anxiety_by_gender.plot(kind='bar', stacked=False, color=['#e74c3c', '#2ecc71'], width=0.6)
    plt.title('Anxiety Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('images/anxiety_by_gender.png')
    plt.show()

def plot_anxiety_by_cgpa(df):
    anxiety_by_cgpa = df.groupby('what_is_your_cgpa?')['do_you_have_anxiety?'].value_counts().unstack()

    anxiety_by_cgpa.plot(kind='bar', stacked=False, color=['#e74c3c', '#2ecc71'], width=0.6)
    plt.title('Anxiety Distribution by CGPA')
    plt.xlabel('CGPA')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/anxiety_by_cgpa.png')
    plt.show()

if __name__ == "__main__":
    input_file = 'data/student_mental_health_cleaned.csv'
    df = load_cleaned_data(input_file)

    plot_anxiety_by_gender(df)
    plot_anxiety_by_cgpa(df)
