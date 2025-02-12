# Systematically Improving Your RAG Application

## Workshop Overview

Most teams build RAG applications on shaky foundations, assuming retrieval "just works" with semantic similarity and lacking systematic testing. Without clear metrics and objective measurements, teams struggle to identify failing components and can't tell if changes like complex re-ranking pipelines or filtering mechanisms actually improve performance.

In this workshop, we'll use an e-commerce RAG application as a case study to demonstrate how synthetic data can bootstrap evaluation datasets, establish key metrics, and quantify improvements from techniques like metadata filtering to enhance retrieval quality.

## Notebook Breakdown

### Notebook 1: RAG Fundamentals and Evaluation

**Summary**: Learn to evaluate and improve RAG systems using an e-commerce product catalog as a case study. We'll build test datasets with synthetic queries, implement evaluation metrics, and measure retrieval performance objectively.

**Learning Outcomes**

- Generate synthetic shopping queries for testing retrieval
- Understand and address semantic search edge cases
- Master key metrics for measuring product retrieval accuracy
- Compute an initial baseline for semantic search for our RAG application

### Notebook 2: Metadata-Enhanced Retrieval

**Summary**: We'll use a vision language model to generate high-quality product metadata using a predefined taxonomy. We'll then use this taxonomy to generate query filters when we receive a user query, ensuring results are semantically relevant and conform to business requirements. We’ll then use the original metrics we covered in Notebook 1 and quantify the corresponding improvement that our new metrics have generated.

**Learning Outcomes**:

- Learn techniques for generating high-quality product metadata systematically
- Build effective metadata filtering systems to complement semantic search
- Quantify improvements using recall and MRR as objective metrics
