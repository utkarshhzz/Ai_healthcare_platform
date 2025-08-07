# AI Healthcare Platform 🏥🤖

A comprehensive multi-modal healthcare AI platform for disease detection, risk analysis, and personalized medicine.

## Features
- 🔬 X-ray image analysis for disease detection
- 🎵 Cough audio analysis for respiratory conditions
- 📊 Electronic Health Record (EHR) analysis
- 💬 AI-powered medical chatbot
- 📈 Risk prediction and personalized recommendations
- 🔍 Explainable AI with visualizations

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- Kaggle account (for datasets)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd healthcare_ai_platform
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Kaggle API:
```bash
pip install kaggle
# Download kaggle.json from your Kaggle account
# Place it in ~/.kaggle/ (or C:\Users\{username}\.kaggle\ on Windows)
```

### Quick Start
1. Download datasets (see notebooks/01_data_download.ipynb)
2. Run data preprocessing
3. Train baseline models
4. Launch Streamlit app

## Project Structure
```
├── data/
│   ├── raw/          # Original datasets
│   └── processed/    # Cleaned data
├── src/
│   ├── models/       # ML model definitions
│   ├── utils/        # Utility functions
│   └── pipeline/     # Data processing
├── notebooks/        # Jupyter notebooks
├── app/             # Web application
└── models/          # Saved model files
```

## Development Status
🚧 Work in Progress - Building step by step!

## License
MIT License
