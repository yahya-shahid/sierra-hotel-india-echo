# Plant Disease Detection [CNN + PlantVillage]

This project uses a Convolutional Neural Network (CNN) to classify plant leaf diseases using the PlantVillage dataset.

## Features
- Automatic dataset download from Kaggle
- Automatic train/val/test split
- Simple CNN architecture
- Colab + local VS Code compatible
- Clean modular codebase

## Setup (Local)

1. Clone the repo:
   git clone https://github.com/YOUR_USERNAME/plant-disease-detection

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create `.env`:
   cp .env.example .env
   # Add your Kaggle username + key

5. Download dataset:
   python src/data_download.py

6. Split dataset:
   python src/data_split.py

7. Train model:
   python src/train_cnn.py

## Running in Colab
- Open `notebooks/main.ipynb`
- Add Kaggle key in Colab Secrets
- Run all cells

## Dataset
PlantVillage dataset by Emma Rex (Kaggle)

## License
MIT License
