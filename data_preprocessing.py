# data_preprocessing.py

import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Clean and preprocess the data."""
    df = df.drop(['Timestamp'], axis=1)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
        input_file = 'data/student_mental_health.csv'
        output_file = 'data/student_mental_health_cleaned.csv'

    df = load_data(input_file)
    df_cleaned = preprocess_data(df)
    save_clean_data(df_cleaned, output_file)
    print("Data preprocessing complete. Cleaned data saved to:", output_file)
