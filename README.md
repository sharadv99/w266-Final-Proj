# Multi-Label Movie Genre Classification from Plot Summaries

--Data Science project at UC Berkeley--  
--Team: [Sharad Varadarajan](https://www.linkedin.com/in/sharadv/), [Akhil Patel](https://www.linkedin.com/in/akhil-patel-b4431639/)--  

Description
---------

When reading a plot summary, a person can intuit which genre(s) the movie falls into and compare that to his or her individual preferences. While the genre itself may not be explicitly mentioned in the plot summary, many have hypothesized that a hidden representation of genre information lies within the underlying text. Our goal was to confidently classify these hidden representations to their corresponding genre using various NLP techniques. 

We performed multi-label, multi-class movie genre classification on plot summaries from a considerably imbalanced dataset. Specifically, we explore different ways to construct informative plot summary vectors, including through the use of a novel integration of Universal Sentence Encodings (USE) with Hierarchical Attention Networks (HAN). We also address problems faced by past researchers who used this corpus by combining multi-label sampling with homogeneous ensemble methods to effectively train models on de-skewed data. Each exploratory ensemble of classifiers is compared to a counterpart trained on the full imbalanced data, as well as to a bag-of-words TFIDF baseline. We find that utilization of USE and HAN can outperform the baseline though improvements, as measured by precision, recall, and F1-score, are incremental at best.

For a full overview of the project, as well as details on the motivation, technical design/methods, model performance, and next steps, please see our [full research report](https://github.com/sharadv99/w266-Multi-Label-Genre-Classification/blob/master/Multi-Label%20Movie%20Genre%20Classification%20from%20Plot%20Summaries.pdf).


