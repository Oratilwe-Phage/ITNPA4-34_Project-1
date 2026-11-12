# ITNPA4-34_Project-1

## Researchly: NLP Research Document Classification, Summarization & Topic Mining Pipeline

A complete Natural Language Processing (NLP) pipeline designed for Researchly that automates academic research abstract preprocessing, feature engineering, semantic clustering, supervised classification, and topic modeling.



## 🚀 Project Overview 
Researchly is a comprehensive Natural Language Processing (NLP) and Machine Learning solution that automates academic research article screening, classification, summarization, and thematic discovery. This repository, which was created as a thorough proof-of-concept, includes latent topic modeling, extractive/abstractive text summarization, supervised and unsupervised machine learning, data preparation, and interactive online deployment.

## 🧩 Repository Structure

### For Data and Notebooks
- Question 1:
  - Python Script for Question 1
 
- Question 2:
  - Python Script for Question 2
  - Research Abstract Classifier file
  - Research abstract preprocessed.csv file
  - Research abstract preprocessed.xlsx file
 
- Question 3:
  - Python Script for Question 3
  - Topic Analysis file
 
- Question 4:
  - Python Script for Question 4
  - Topic Modeling using LDA
  - index.html for the Interactive PyLDAvis Intertopic Distance Map
 
### For Deployments:   
- App.py for Question 2 Researchly Research Abstract Classifier
  
- Requirements.txt for Question 2 Researchly Research Abstract Classifier
  


## 📚Project Methodology and Workflow (Questions 1–4)

Question 1: Baseline modeling, feature engineering, and data preprocessing
- Data Ingestion & Denoising (1.1): A structured pandas DataFrame was loaded with research_abstracts.json. used a thorough text denoising pipeline that included WordNet lemmatization, NLTK stopword filtering, punctuation and digit removal, URL/HTML element stripping, and lowercasing.

- Using TF-IDF (Term Frequency–Inverse Document Frequency) vectorization using unigrams and bigrams (ngram_range=(1, 2)), feature engineering (1.2) converted cleaned text into numerical representations, isolating the most relevant domain terms.

- Baseline Model (1.3): Before adding supervised labels, an unsupervised K-Means Clustering baseline (n_clusters=5) was established and assessed using the Silhouette Score to benchmark semantic grouping.

Question 2: Multi-Model Benchmarking, Supervised Classification, Optimization, and Web Deployment 

- Multi-Model Benchmarking (2.1): Trained and evaluated four supervised machine learning classifiers to distinguish between AI-related and classical research abstracts:
1. Logistic Regression
2. Random Forest ClassifierSupport
3. Vector Classifier (Linear SVC)
4. Multinomial Naive BayesPerformance Enhancement
   
- Performance Enhancement (2.2):Applied 5-Fold Cross-Validated Grid Search (GridSearchCV) to optimize regularization strength (C) and penalty parameters, improving weighted F1-score and generalization over default configurations.
- *Web Application Deployment* (2.3): Deployed the optimal classifier into an interactive Streamlit web interface (deployment/app.py), enabling real-time user input, automated text denoising, and instant classification feedback.

Question 3: Topic Analysis: Mining and Summarizing Research Documents

- Corpus Extraction (3.1): Extracted and parsed raw research articles from research_corpus.zip into a unified pandas DataFrame mapping each document identifier to its full textual content.
- Corpus Denoising (3.2): Applied state-of-the-art text cleaning and normalization techniques tailored for long-form academic articles to remove formatting artifacts, citations noise, and non-informative tokens.
- Single-Document Summarization (3.3): Summarized the information content of the primary article using an extractive/abstractive summarization technique, accompanied by keyword frequency and sentence-importance visualizations.
- Aggregate Corpus Summarization (3.4): Synthesized an aggregate summary across the remaining articles in the corpus using a complementary summarization approach, supported by visual thematic and word-distribution charts.

Question 4: Interactive Topic Mapping and Latent Dirichlet Allocation (LDA)

- LDA Topic Modeling (4.1): Constructed a term-frequency matrix (CountVectorizer) and trained a Latent Dirichlet Allocation (LDA) model to uncover latent research themes, displaying top salient words per topic alongside corpus-wide probability distribution bar charts.
- Interactive Visualization (4.2): Built an interactive Intertopic Distance Map using pyLDAvis (exported to deployment/lda_interactive_visualization.html), allowing dynamic inspection of topic overlap, cluster distances, and term saliency (parameter tuning).



## ⚙️ Installation & Quick Start

1. Ran the Streamlit Web Classifier (Question 2.3)
2. Navigate to the deployment directory and launch the web application:
3. **Researchly-abstract-classifier link:** https://itnpa4-34project-1-hdqtxtfmhgaj29ri9aexzn.streamlit.app/
4. View the Interactive Topic Map (Question 4.2)
- Open index.html directly in any web browser to explore the interactive pyLDAvis topic clusters and salient terms.



## 🤖 Technologies Used
- Data Manipulation & Analysis: pandas, numpy

- Natural Language Processing: nltk, re, string

- Machine Learning & Topic Modeling: scikit-learn (TF-IDF, K-Means, Logistic Regression, Random Forest, SVC, MultinomialNB, GridSearchCV, LDA)

- Visualization & Deployment: matplotlib, pyLDAvis, streamlit







    































