import pandas as pd

def load_crop_params(csv_path, species_name):
    df = pd.read_csv(csv_path)
    row = df[df['species'] == species_name]
    
    if row.empty:
        raise ValueError(f"Species '{species_name}' not found. Available: {df['species'].tolist()}")
    
    params = row.iloc[0].to_dict()
    return params


if __name__ == "__main__":
    params = load_crop_params("crop_data.csv", "Lactuca_sativa")
    
    for key, value in params.items():
        print(f"{key}: {value}")