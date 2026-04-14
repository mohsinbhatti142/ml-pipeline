# 🚀 ML Pipeline: Spam Detection Classifier

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![DVC](https://img.shields.io/badge/DVC-3.49+-orange.svg)](https://dvc.org/)
[![MLflow](https://img.shields.io/badge/MLflow-1.27+-red.svg)](https://mlflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8+-green.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end machine learning pipeline for spam message detection using natural language processing and traditional ML algorithms. Built with DVC for reproducible pipelines, MLflow for experiment tracking, and modern Python tooling.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Stages](#pipeline-stages)
- [Results](#results)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a complete ML pipeline for classifying SMS messages as spam or ham (non-spam). The pipeline follows MLOps best practices with:

- **Data Versioning**: DVC tracks data and model artifacts
- **Experiment Tracking**: MLflow logs parameters, metrics, and models
- **Reproducible Pipelines**: DVC pipelines ensure consistent execution
- **Live Metrics**: DVC Live provides real-time monitoring

The model achieves **94.2% accuracy** on the test set using Random Forest with TF-IDF features.

## ✨ Features

- 🔄 **Automated Pipeline**: End-to-end workflow from raw data to model deployment
- 📊 **Comprehensive Evaluation**: Accuracy, Precision, Recall, and AUC metrics
- 🔍 **Text Preprocessing**: NLTK-based cleaning, stemming, and stopword removal
- 🎯 **Feature Engineering**: TF-IDF vectorization for text representation
- 🌳 **Ensemble Model**: Random Forest classifier for robust predictions
- 📈 **Experiment Tracking**: Full parameter and metric logging
- 🔄 **Version Control**: Data and model versioning with DVC
- 📝 **Detailed Logging**: Comprehensive logging at each pipeline stage

## 📁 Project Structure

```
ml-pipeline/
├── src/                          # Source code
│   ├── data-ingestion.py         # Data loading and preprocessing
│   ├── preprocessing.py          # Text cleaning and normalization
│   ├── feature_eng.py            # TF-IDF feature extraction
│   ├── model_building.py         # Model training
│   └── model_evl.py              # Model evaluation
├── data/                         # Data directory
│   ├── raw/                      # Raw datasets
│   ├── interim/                  # Intermediate processed data
│   └── processed/                # Final feature matrices
├── models/                       # Trained models
├── reports/                      # Evaluation reports
├── experiments/                  # Experiment artifacts
├── logs/                         # Log files
├── dvclive/                      # Live metrics and plots
├── dvc.yaml                      # DVC pipeline definition
├── params.yaml                   # Pipeline parameters
├── pyproject.toml                # Project configuration
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (modern Python package manager)
- [DVC](https://dvc.org/) for pipeline management
- [MLflow](https://mlflow.org/) for experiment tracking

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ml-pipeline
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Activate virtual environment**
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install additional tools**
   ```bash
   pip install dvc mlflow
   ```

## 🚀 Usage

### Running the Full Pipeline

Execute the entire pipeline with DVC:

```bash
dvc repro
```

This will run all stages sequentially:
1. Data ingestion
2. Preprocessing
3. Feature engineering
4. Model training
5. Model evaluation

### Running Individual Stages

Run specific pipeline stages:

```bash
# Data ingestion only
dvc repro data_ingestion

# Model training only
dvc repro model_building
```

### Viewing Results

- **Metrics**: Check `reports/metrics.json` or `dvclive/metrics.json`
- **Logs**: View detailed logs in `logs/` directory
- **MLflow UI**: Run `mlflow ui` to view experiments
- **DVC Live**: View live metrics in `dvclive/` directory

## 🔧 Pipeline Stages

### 1. Data Ingestion 📥
- **Input**: Raw spam dataset from URL
- **Processing**: Load CSV, clean columns, train/test split
- **Output**: Raw train/test datasets in `data/raw/`

### 2. Data Preprocessing 🧹
- **Input**: Raw text data
- **Processing**:
  - Text normalization (lowercase, tokenization)
  - Stopword and punctuation removal
  - Porter stemming
  - Target encoding (spam/ham → 0/1)
- **Output**: Cleaned datasets in `data/interim/`

### 3. Feature Engineering ⚙️
- **Input**: Preprocessed text data
- **Processing**: TF-IDF vectorization (max 35 features)
- **Output**: Feature matrices in `data/processed/`

### 4. Model Building 🏗️
- **Input**: Feature matrices
- **Processing**: Random Forest training (25 estimators)
- **Output**: Trained model in `models/model.pkl`

### 5. Model Evaluation 📊
- **Input**: Trained model and test features
- **Processing**: Prediction and metric calculation
- **Output**: Performance metrics and plots

## 📈 Results

Current model performance on test set:

| Metric | Value |
|--------|-------|
| Accuracy | 94.2% |
| Precision | 86.5% |
| Recall | 69.9% |
| AUC | 92.4% |

### Performance Visualization

DVC Live generates interactive plots for:
- Accuracy over time
- Precision trends
- Recall curves
- AUC scores

## ⚙️ Configuration

Pipeline parameters are defined in `params.yaml`:

```yaml
data_ingestion:
  test_size: 0.2

feature_engineering:
  max_features: 35

model_building:
  n_estimators: 25
  random_state: 40
```

Modify these values and re-run `dvc repro` to experiment with different configurations.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
uv sync --dev

# Run tests
uv run pytest

# Format code
uv run black .
uv run isort .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ using DVC, MLflow, and modern Python tooling**

*Star this repo if you find it useful!* ⭐