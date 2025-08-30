"""
Healthcare AI Platform - Automated Data Downloader
==================================================
This script automatically downloads all required datasets for the healthcare AI project.
Run this on any new device to set up the complete dataset structure.

Author: Healthcare AI Team
Date: August 2025
"""

import os
import requests
import zipfile
import gdown
from pathlib import Path
import shutil
from tqdm import tqdm

def create_directory_structure():
    """Create the complete directory structure for the healthcare AI project."""
    base_path = Path("data")
    
    directories = [
        "data/raw/chest_xray",
        "data/raw/covid_xray", 
        "data/raw/brain_mri",
        "data/raw/blood_tests",
        "data/raw/cough_audio",
        "data/raw/diabetes",
        "data/raw/ecg", 
        "data/raw/heart_disease",
        "data/raw/medical_text",
        "data/raw/skin_cancer",
        "data/processed/multi_disease/train/NORMAL",
        "data/processed/multi_disease/train/PNEUMONIA", 
        "data/processed/multi_disease/train/COVID",
        "data/processed/multi_disease/test/NORMAL",
        "data/processed/multi_disease/test/PNEUMONIA",
        "data/processed/multi_disease/test/COVID"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def download_file_from_url(url, destination, description="Downloading"):
    """Download a file from URL with progress bar."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(destination, 'wb') as file, tqdm(
            desc=description,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                size = file.write(chunk)
                progress_bar.update(size)
        
        print(f"✅ Downloaded: {destination}")
        return True
    except Exception as e:
        print(f"❌ Error downloading {url}: {str(e)}")
        return False

def download_chest_xray_dataset():
    """Download the chest X-ray pneumonia dataset."""
    print("\n🫁 Downloading Chest X-Ray Pneumonia Dataset...")
    
    # Kaggle chest X-ray dataset
    url = "https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/download"
    destination = "data/raw/chest_xray/chest-xray-pneumonia.zip"
    
    # Alternative direct download links
    alternative_urls = [
        "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/rscbjbr9sj-2.zip",
        "https://storage.googleapis.com/kagglesdsdata/datasets/17810/23812/chest_xray.zip"
    ]
    
    success = False
    for i, url in enumerate([url] + alternative_urls):
        print(f"Trying download source {i+1}...")
        if download_file_from_url(url, destination, "Chest X-Ray Dataset"):
            success = True
            break
    
    if success:
        # Extract the dataset
        try:
            with zipfile.ZipFile(destination, 'r') as zip_ref:
                zip_ref.extractall("data/raw/chest_xray/")
            print("✅ Extracted chest X-ray dataset")
            os.remove(destination)  # Clean up zip file
        except Exception as e:
            print(f"❌ Error extracting: {str(e)}")
    else:
        print("❌ Failed to download chest X-ray dataset from all sources")
        print("📋 Manual download instructions:")
        print("1. Go to: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia")
        print("2. Download the dataset")
        print("3. Extract to: data/raw/chest_xray/")

def download_covid_dataset():
    """Download the COVID-19 radiography dataset."""
    print("\n🦠 Downloading COVID-19 Radiography Dataset...")
    
    # COVID-19 Radiography Database
    urls = [
        "https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database/download",
        "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/8h65ywd2jr-3.zip"
    ]
    
    destination = "data/raw/covid_xray/covid-radiography.zip"
    
    success = False
    for i, url in enumerate(urls):
        print(f"Trying COVID dataset source {i+1}...")
        if download_file_from_url(url, destination, "COVID-19 Dataset"):
            success = True
            break
    
    if success:
        try:
            with zipfile.ZipFile(destination, 'r') as zip_ref:
                zip_ref.extractall("data/raw/covid_xray/")
            print("✅ Extracted COVID-19 dataset")
            os.remove(destination)
        except Exception as e:
            print(f"❌ Error extracting: {str(e)}")
    else:
        print("❌ Failed to download COVID dataset")
        print("📋 Manual download instructions:")
        print("1. Go to: https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database")
        print("2. Download and extract to: data/raw/covid_xray/")

def download_sample_datasets():
    """Download smaller sample datasets for testing."""
    print("\n🩺 Downloading Sample Medical Datasets...")
    
    # Heart disease dataset (CSV)
    heart_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    if download_file_from_url(heart_url, "data/raw/heart_disease/heart.csv", "Heart Disease Data"):
        print("✅ Heart disease dataset downloaded")
    
    # Diabetes dataset
    diabetes_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
    if download_file_from_url(diabetes_url, "data/raw/diabetes/diabetes.csv", "Diabetes Data"):
        print("✅ Diabetes dataset downloaded")

def create_data_info_file():
    """Create an information file about the datasets."""
    info_content = """
# Healthcare AI Platform - Dataset Information
============================================

## 🎯 Required Datasets for Complete Healthcare AI Platform

### 1. Chest X-Ray Pneumonia Detection
- **Source**: Kaggle - Chest X-Ray Images (Pneumonia)
- **Link**: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
- **Size**: ~1.2GB
- **Classes**: Normal, Pneumonia
- **Images**: 5,863 total images

### 2. COVID-19 Radiography Database  
- **Source**: Kaggle - COVID-19 Radiography Database
- **Link**: https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database
- **Size**: ~1.1GB  
- **Classes**: Normal, COVID-19, Lung Opacity, Viral Pneumonia
- **Images**: 21,165 total images

### 3. Heart Disease Dataset
- **Source**: UCI Machine Learning Repository
- **Link**: https://archive.ics.uci.edu/ml/datasets/heart+disease
- **Size**: <1MB
- **Type**: Tabular data (CSV)

### 4. Diabetes Dataset
- **Source**: UCI - Pima Indians Diabetes Database
- **Link**: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
- **Size**: <1MB
- **Type**: Tabular data (CSV)

## 🚀 Quick Setup Instructions

### Automatic Setup (Recommended):
```python
python data_downloader.py
```

### Manual Setup (If needed):
1. Create account on Kaggle.com
2. Download datasets from links above
3. Extract to respective folders in data/raw/
4. Run notebook: 02_data_exploration_and_visualization.ipynb

## 📁 Expected Directory Structure After Download:
```
data/
├── raw/
│   ├── chest_xray/
│   │   └── chest_xray/
│   │       ├── train/
│   │       └── test/
│   ├── covid_xray/
│   │   └── COVID-19_Radiography_Dataset/
│   ├── heart_disease/
│   │   └── heart.csv
│   └── diabetes/
│       └── diabetes.csv
└── processed/
    └── multi_disease/
        ├── train/
        └── test/
```

## 🎓 Project Status:
- ✅ Phase 1: Environment Setup Complete
- ✅ Phase 2: Basic Pneumonia Detection AI (96.59% accuracy)  
- 🔄 Phase 3A: Multi-Disease Detection (Normal/Pneumonia/COVID)
- 📋 Phase 3B: Advanced Multi-Modal AI (Images + Audio + Tabular)

## 🔧 Troubleshooting:
- If download fails: Use manual download instructions
- If paths don't work: Check directory structure matches above
- If models don't load: Re-run setup cells in notebook

## 💡 Next Steps:
1. Run data_downloader.py
2. Open notebooks/02_data_exploration_and_visualization.ipynb  
3. Execute cells 1-5 for environment setup
4. Continue from your last checkpoint

Happy coding! 🚀
"""
    
    with open("DATA_INFO.md", "w") as f:
        f.write(info_content)
    print("✅ Created DATA_INFO.md with complete setup instructions")

def main():
    """Main function to download all datasets."""
    print("🏥 Healthcare AI Platform - Data Downloader")
    print("=" * 50)
    
    # Create directory structure
    create_directory_structure()
    
    # Download datasets
    download_chest_xray_dataset()
    download_covid_dataset() 
    download_sample_datasets()
    
    # Create information file
    create_data_info_file()
    
    print("\n" + "=" * 50)
    print("🎉 Data download process completed!")
    print("📋 Check DATA_INFO.md for manual download instructions if needed")
    print("🚀 Ready to run your healthcare AI notebooks!")

if __name__ == "__main__":
    # Check if required packages are installed
    required_packages = ['requests', 'tqdm', 'gdown']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {missing_packages}")
        print("Install with: pip install " + " ".join(missing_packages))
    else:
        main()
