from scripts.load_data import load_data
from scripts.clean_transform import clean_data

df = load_data("data/raw/dataset.csv")

cleaned = clean_data(df)

cleaned.to_csv("data/cleaned/cleaned_dataset.csv", index=False)

print("Project completed successfully!") 