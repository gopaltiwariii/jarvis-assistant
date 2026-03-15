import pandas as pd

def main():
    print("Loading data from 'data.csv'...")
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("Error: 'data.csv' not found. Please ensure it's in the same directory.")
        return

    print("\n--- First few rows of the dataset ---")
    print(df.head())

    print("\n--- Basic Information ---")
    print(df.info())

    print("\n--- Summary Statistics ---")
    print(df.describe())

    print("\n--- Average Salary by Department ---")
    avg_salary_by_dept = df.groupby('department')['salary'].mean().sort_values(ascending=False).reset_index()
    print(avg_salary_by_dept)

if __name__ == "__main__":
    main()
