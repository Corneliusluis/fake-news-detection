# 📰 Fake News Detection — Methodology Reproduction

## 📌 Overview
Fake news has become a significant challenge in today’s digital world, influencing public opinion, politics, and even public safety. This project aims to **reproduce the methodology from the WELFake paper** to classify news articles as **real** or **fake** based on their content.

We use the **WELFake** dataset — a large, balanced benchmark dataset specifically designed for fake news detection — and reimplement the approach described in the original paper by Shahane et al. (2021), comparing our results against theirs.

---

## 📂 Dataset
**Source:** [WELFake Dataset - Zenodo](https://zenodo.org/records/4561253)  

- **Total articles:** 72,134  
  - **Fake:** 37,106  
  - **Real:** 35,028  
- **Format:** CSV with the following columns:
  - `title` — headline of the news
  - `text` — main body of the news
  - `label` — binary classification (1 = fake, 0 = real)

The dataset was created by merging four reputable sources:
- Kaggle Fake News Dataset
- McIntire Fake News Dataset
- Reuters Dataset
- BuzzFeed Political News Dataset

---

## 🧪 Methodology Reproduction
This project **reimplements the approach** described in:

> P. K. Verma, P. Agrawal, I. Amorim and R. Prodan, "WELFake: Word Embedding Over Linguistic Features for Fake News Detection," in IEEE Transactions on Computational Social Systems, vol. 8, no. 4, pp. 881-893, Aug. 2021, doi: 10.1109/TCSS.2021.3068519.
keywords: {Social networking (online);Linguistics;Data models;Bit error rate;Feature extraction;Training;Vegetation;Bidirectional encoder representations from transformer (BERT);convolutional neural network (CNN);fake news;linguistic feature;machine learning (ML);text classification;voting classifier;word embedding (WE)},

The original paper experiments with multiple machine learning classifiers — **KNN, SVM, Naive Bayes, Decision Tree, Bagging, and AdaBoost** — using a combination of **word embeddings** and **linguistic features**.  

Our implementation:
- Follows the preprocessing, feature extraction, and modeling pipeline described in the paper.
- Uses independently written code — no original code from the paper is copied.
- Benchmarks results against the reported metrics in the paper.

---

## ⚙️ Features & Workflow
- **Text preprocessing:** tokenization, stopword removal, lemmatization  
- **Feature extraction:** TF-IDF, word embeddings (GloVe)  
- **Models reproduced from the paper:**
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Naive Bayes (NB)
  - Decision Tree (DT)
  - Bagging Classifier
  - AdaBoost Classifier
- **Evaluation metrics:** Accuracy, Precision, Recall, F1-score

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
