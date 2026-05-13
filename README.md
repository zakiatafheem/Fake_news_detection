# Fake News Detection using Machine Learning and NLP

## Project Overview
This project is an NLP-based Fake News Detection system that classifies news articles as REAL or FAKE using Machine Learning techniques. The system uses TF-IDF Vectorization for text feature extraction and LinearSVC for classification. A complete machine learning pipeline is implemented for preprocessing, training, evaluation, and prediction.

The project helps identify misleading or fake news articles automatically and demonstrates the practical use of NLP in real-world applications.

---

## Problem Statement
Develop an NLP-based machine learning model to automatically classify news articles as REAL or FAKE using TF-IDF Vectorization and supervised learning algorithms.

With the rapid spread of misinformation on digital platforms, manually verifying news articles becomes difficult and time-consuming. This project aims to build an automated solution that can analyze textual news content and predict whether the news is genuine or fake.

---

## Dataset Details

### Dataset Features
- `text` → News article content
- `label` → REAL or FAKE

### Data Preprocessing
- Removed missing/null values
- Converted labels:
  - REAL → 1
  - FAKE → 0
- Split dataset into training and testing sets
- Applied TF-IDF Vectorization for feature extraction

### Dataset Source
Publicly available Fake News datasets from Kaggle/open-source repositories.

---

## Model / Architecture Used

### NLP Technique
- TF-IDF Vectorization

### Machine Learning Algorithm
- Linear Support Vector Classifier (LinearSVC)

### Pipeline Used
- TF-IDF Vectorizer
- LinearSVC Classifier

### Parameters Used
```python
TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),
    max_df=0.8
)

LinearSVC(class_weight='balanced')
```

### Workflow
1. Load dataset
2. Preprocess text data
3. Convert text into TF-IDF vectors
4. Train LinearSVC model
5. Evaluate model performance
6. Save trained model using Pickle

---

## Results / Outputs

### Model Performance
- Achieved high accuracy in detecting fake news articles
- Evaluated using:
  - Accuracy Score
  - Precision
  - Recall
  - F1-Score
  - Classification Report

### Example Output
```python
Accuracy: 0.99
```

### Images

[HOME PAGE](home.png)
[REAL NEWS PAGE](real news.png)
[FAKE NEWS PAGE](fake news.png)

---

## Hugging Face Deployment Link

🔗 Add your deployed Hugging Face application link here:

```text
https://huggingface.co/spaces/ZakiaTafheem/Fake_News_Detection_using_NLP
```

---

## Future Improvements
- Implement Deep Learning models like LSTM and BERT
- Add multilingual fake news detection
- Improve preprocessing using stemming and lemmatization
- Deploy the project on cloud platforms
- Integrate real-time news verification APIs
- Add explainable AI features for prediction interpretation
- Build a more interactive UI using Streamlit or React
