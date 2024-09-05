import pandas as pd

def extract_data():
    data = [
        {"name": "Alice", "age": 30, "salary": 700, "has_car": True, "has_house": True},
        {"name": "Bob", "age": 25, "salary": 500, "has_car": False, "has_house": True},
        {"name": "Charlie", "age": 35, "salary": 800, "has_car": True, "has_house": False},
        {"name": "David", "age": 40, "salary": 1200, "has_car": True, "has_house": True},
        {"name": "Eva", "age": 28, "salary": 550, "has_car": False, "has_house": False}
    ]
    return pd.DataFrame(data)

def transform_data(df):
    avg_salary = df["salary"].mean()
    filtered_data = df[df["has_car"] == True]
    return avg_salary, filtered_data

def load_data(avg_salary, filtered_data):
    avg_salary_path = "average_salary.csv"
    filtered_data_path = "filtered_data.csv"

    avg_salary_df = pd.DataFrame([avg_salary], columns=["average_salary"])
    avg_salary_df.to_csv(avg_salary_path, index=False)

    filtered_data.to_csv(filtered_data_path, index=False)
    return avg_salary_path, filtered_data_path

def main():
    df = extract_data()

    avg_salary, filtered_data = transform_data(df)

    avg_salary_path, filtered_data_path = load_data(avg_salary, filtered_data)

    print(f"\nAverage salary: {avg_salary}")
    print(f"Filtered data:\n{filtered_data}")

    print(f"\nAverage salary path: {avg_salary_path}")
    print(f"Filtered data path: {filtered_data_path}")

if __name__ == "__main__":
    main()