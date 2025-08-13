# 📰 Fake News Detection

## 📌 Overview
Fake news has become a significant challenge in today’s digital world, influencing public opinion, politics, and even public safety. This project aims to develop a **machine learning-based fake news detection system** that can classify news articles as **real** or **fake** based on their content.

We use the **WELFake** dataset — a large, balanced benchmark dataset specifically designed for fake news detection — and experiment with various machine learning and deep learning models to improve detection accuracy.

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

The dataset is created by combining four reputable sources:
- Kaggle Fake News Dataset
- McIntire Fake News Dataset
- Reuters Dataset
- BuzzFeed Political News Dataset

---

## ⚙️ Features & Methodology
- **Text preprocessing:** tokenization, stopword removal, lemmatization  
- **Feature extraction:** TF-IDF, word embeddings (GloVe)  
- **Models experimented:**
  - Logistic Regression
  - Naive Bayes
  - SVM
  - Decision Tree
  - Bagging & AdaBoost
  - CNN (for text classification)
- **Evaluation metrics:** Accuracy, Precision, Recall, F1-score

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
