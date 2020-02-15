# Multi-Label Movie Genre Classification from Plot Summaries

--Data Science project at UC Berkeley--  
--Team: [Sharad Varadarajan](https://www.linkedin.com/in/sharadv/), [Akhil Patel](https://www.linkedin.com/in/akhil-patel-b4431639/)--  

Description
---------

When reading a movie plot summary, a person can usually intuit which genre(s) the movie falls into and compare that to his or her individual preferences. While the genre itself may not be explicitly mentioned in the plot summary, many have hypothesized that a hidden representation of genre information lies within the underlying text. Our goal was to confidently classify these hidden representations to their corresponding genre(s) using various NLP techniques. 

We performed multi-label, multi-class movie genre classification on plot summaries from a considerably imbalanced dataset. Specifically, we explore different ways to construct informative plot summary vectors, including through the use of a novel integration of Universal Sentence Encodings (USE) with Hierarchical Attention Networks (HAN). We also address problems faced by past researchers who used this corpus by combining multi-label sampling with homogeneous ensemble methods to effectively train models on de-skewed data. Each exploratory ensemble of classifiers is compared to a counterpart trained on the full imbalanced data, as well as to a bag-of-words TFIDF baseline. We find that utilization of USE and HAN can outperform the baseline though improvements, as measured by precision, recall, and F1-score, are incremental at best.

For a full overview of the project, as well as details on the motivation, technical design/methods, model performance, and next steps, please see our [full research report](https://github.com/sharadv99/w266-Multi-Label-Genre-Classification/blob/master/Multi-Label%20Movie%20Genre%20Classification%20from%20Plot%20Summaries.pdf).

Tech Stack/Methods
-------------

- Python
- Tensorflow/Keras
- NLTK
- Bag-of-Words modeling (BoW)
- TFIDF
- Word Embeddings
- Universal Sentence Encoder
- Hierarchical Attention Networks
- Deep Learning/Neural Networks
- Ensemble Methods
- Multi-Label Classification
- Custom Sampling

Key Files
-----------

- **`EDA and Model Building.ipynb`**: In this file we read in training/test data (`train_genres.txt`, `test_genres.txt`, `train_plots.txt`, `test_plots.txt`), conduct major data pre-processing and exploratory data analysis, train/evaluate different variants of our hierarchical attention network, and perform error analysis.
- **`Analysis2_Univ_Sent_Encoder.ipynb`**: Archived file where we first introduced the universal sentence encoder to our models
- **`Neural_BOW_Model.ipynb`**: This file introduces the custom sampling methods we explored for our imbalanced, multi-label data. Additionally it houses the training/evaluation of our different bag-of-word models (including homogenous ensembles).
- **`Files with .h5 extension`**: These files represent various trained deep learning models for our project, which we saved so as to prevent the need for re-training if any evaluation was needed in future sessions.
- **`Multi-Label Movie Genre Classification from Plot Summaries.pdf`**: Final research report with full scope/analysis/results.



