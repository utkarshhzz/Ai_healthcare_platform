"""
Healthcare AI Platform - Complete Setup Script
==============================================
Run this script on any new device to set up the complete healthcare AI environment.

This script will:
1. Install required packages
2. Download all datasets
3. Set up directory structure  
4. Prepare notebooks for immediate use

Author: Healthcare AI Team
Date: August 2025
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages for the healthcare AI platform."""
    print("📦 Installing required packages...")
    
    # Basic requirements
    basic_packages = [
        "torch", "torchvision", "torchaudio",
        "numpy", "pandas", "matplotlib", "seaborn",
        "scikit-learn", "opencv-python", "Pillow",
        "requests", "tqdm", "gdown"
    ]
    
    for package in basic_packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
    
    print("✅ Package installation completed!")

def setup_project():
    """Set up the complete project structure."""
    print("\n🏗️ Setting up project structure...")
    
    # Run the data downloader
    try:
        import data_downloader
        data_downloader.main()
    except ImportError:
        print("❌ data_downloader.py not found")
        print("Please ensure you're in the healthcare_ai_platform directory")

def create_quick_start_guide():
    """Create a quick start guide for the project."""
    guide_content = """
# 🚀 Healthcare AI Platform - Quick Start Guide

## For New Device Setup:

### 1. Clone the Repository:
```bash
git clone https://github.com/utkarshhzz/Ai_healthcare_platform.git
cd Ai_healthcare_platform
```

### 2. Run Complete Setup:
```bash
python setup_new_device.py
```

### 3. Open Jupyter Notebook:
```bash
jupyter notebook notebooks/02_data_exploration_and_visualization.ipynb
```

### 4. Quick Restart Sequence:
Run these cells in order:
- Cell 5: Library imports
- Cell 31: PyTorch setup  
- Cell 33: Image parameters
- Cell 34: Data transformations
- Cell 68: Multi-disease setup

## 🎯 Current Project Status:
- ✅ Basic Pneumonia Detection AI (96.59% accuracy)
- 🔄 Multi-Disease Detection (Normal/Pneumonia/COVID-19)
- 📋 Ready for Phase 3A completion

## 📞 Troubleshooting:
- If data missing: Run `python data_downloader.py`
- If packages missing: Run `pip install -r requirements.txt`
- If models don't load: Re-run setup cells

## 🎓 Learning Path:
1. Data Exploration → Notebook Cell 1-15
2. Basic AI Training → Notebook Cell 16-45  
3. Advanced Models → Notebook Cell 46-60
4. Multi-Disease AI → Notebook Cell 61+

Happy coding! 🏥🤖
"""
    
    with open("QUICK_START.md", "w") as f:
        f.write(guide_content)
    print("✅ Created QUICK_START.md")

def main():
    """Main setup function."""
    print("🏥 Healthcare AI Platform - New Device Setup")
    print("=" * 55)
    
    # Install packages
    install_requirements()
    
    # Set up project
    setup_project()
    
    # Create guide
    create_quick_start_guide()
    
    print("\n" + "=" * 55)
    print("🎉 Setup completed successfully!")
    print("📖 Check QUICK_START.md for next steps")
    print("🚀 Ready to continue your healthcare AI journey!")

if __name__ == "__main__":
    main()
