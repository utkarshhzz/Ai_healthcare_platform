# 🚀 Healthcare AI Platform - Cross-Device Setup Guide

## 🎯 **For Your New Laptop/Device:**

### **Step 1: Clone the Project**
```bash
git clone https://github.com/utkarshhzz/Ai_healthcare_platform.git
cd Ai_healthcare_platform
```

### **Step 2: Automated Setup (Recommended)**
```bash
# Complete setup with one command
python setup_new_device.py
```

This will:
- ✅ Install all required packages (PyTorch, OpenCV, etc.)
- ✅ Download all medical datasets automatically
- ✅ Set up directory structure
- ✅ Create documentation

### **Step 3: Manual Setup (Alternative)**
```bash
# Install packages
pip install -r requirements.txt

# Download datasets
python data_downloader.py
```

### **Step 4: Open Jupyter Notebook**
```bash
jupyter notebook notebooks/02_data_exploration_and_visualization.ipynb
```

### **Step 5: Quick Restart Sequence**
In the notebook, run these cells in order:
1. **Cell 1** - Portable Setup Cell (checks data availability)
2. **Cell 6** - Library imports  
3. **Cell 32** - PyTorch setup
4. **Cell 34** - Image parameters
5. **Cell 35** - Data transformations

## 📊 **What You Get:**

### **Automatic Downloads:**
- 🫁 Chest X-Ray Pneumonia Dataset (~1.2GB)
- 🦠 COVID-19 Radiography Dataset (~1.1GB)  
- ❤️ Heart Disease Data (CSV)
- 🩺 Diabetes Dataset (CSV)

### **AI Models Ready:**
- ✅ Basic CNN (96.59% accuracy achieved)
- ✅ ResNet50 Transfer Learning
- 🔄 Multi-Disease Detection (in progress)

### **Project Status:**
- ✅ Phase 1: Environment Setup
- ✅ Phase 2: Basic Pneumonia Detection AI
- 🔄 Phase 3A: Multi-Disease Detection (Normal/Pneumonia/COVID)

## 🔧 **Troubleshooting:**

### **If Data Download Fails:**
1. Manual download from:
   - [Chest X-Ray Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
   - [COVID-19 Dataset](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)

2. Extract to:
   - `data/raw/chest_xray/`
   - `data/raw/covid_xray/`

### **If Packages Missing:**
```bash
pip install torch torchvision numpy pandas matplotlib seaborn scikit-learn opencv-python requests tqdm
```

## 🎓 **Continue Your AI Journey:**
After setup, you can immediately continue from where you left off - your multi-disease detection AI development!

The notebook automatically detects missing data and provides instructions, making it truly portable across any device.

**Happy coding on your new device! 🏥🤖**
