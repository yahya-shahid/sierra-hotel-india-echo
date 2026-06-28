import os
import json
import zipfile
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

kaggle_username = os.getenv("KAGGLE_USERNAME")
kaggle_key = os.getenv("KAGGLE_KEY")

if kaggle_username is None or kaggle_key is None:
    raise Exception("KAGGLE_USERNAME or KAGGLE_KEY missing in .env")

# Write kaggle.json
kaggle_dir = os.path.expanduser("~/.kaggle")
os.makedirs(kaggle_dir, exist_ok=True)

with open(os.path.join(kaggle_dir, "kaggle.json"), "w") as f:
    json.dump({"username": kaggle_username, "key": kaggle_key}, f)

os.chmod(os.path.join(kaggle_dir, "kaggle.json"), 600)

print("Kaggle API key installed.")

# Download dataset
print("Downloading dataset...")
os.system("kaggle datasets download -d emmarex/plantdisease -o")

# Extract
zip_path = "plantdisease.zip"
data_dir = "data"

if not os.path.exists(data_dir):
    print("Extracting...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in tqdm(zip_ref.namelist()):
            zip_ref.extract(file, data_dir)

print("Dataset downloaded and extracted.")
