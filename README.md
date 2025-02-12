# Systematically Improving Your RAG Application

## Workshop Overview

Most teams build RAG applications on shaky foundations, assuming retrieval "just works" with semantic similarity and lacking systematic testing. Without clear metrics and objective measurements, teams struggle to identify failing components and can't tell if changes like complex re-ranking pipelines or filtering mechanisms actually improve performance.

In this workshop, we'll use an e-commerce RAG application as a case study to demonstrate how synthetic data can bootstrap evaluation datasets, establish key metrics, and quantify improvements from techniques like metadata filtering to enhance retrieval quality.

## Notebook Breakdown

## Notebook 1: Why Semantic Search Isn't Enough

**Summary**: In this notebook, we'll talk briefly about why you want to prioritise benchmarking retrieval quality in order to iterate quickly when building a RAG application. We'll then explore some of the limitations of semantic search and how it falls short when handling real-world queries that involve multiple constraints like price ranges, complementary items, and specific product attributes.

**Key Takeaways**:

- Understanding when and why semantic search fails for complex queries
- Identifying common retrieval failure patterns in real-world applications
- Learning to implement basic RAG with proper evaluation methods

## Notebook 2: Systematic RAG Evaluation

**Summary**: In this notebook, we'll discuss how synthetic data can be used to quickly bootstrap an evaluation dataset and some practical considerations to consider when building a synthetic dataset. We'll then show you how to use two simple metrics - Mean Reciprocal Rank (MRR) and Recall - to establish baseline performance measurements for your RAG application.

**Key Takeaways**:

- Understanding the importance of synthetic data in RAG evaluation
- Creating synthetic datasets for testing retrieval quality
- Implementing key metrics to measure RAG system performance

## Notebook 3: Enhancing Retrieval with Metadata

**Summary**: In the last notebook, we'll implement metadata filtering when we recieve a user query. This allows us to filter for results based on implicit user requirements. We'll quantify this improvement by showing how MRR and Recall metrics improve as a result of this filtering before exploring how we might use these same metrics to evaluate the performance of better embedding chunks.

**Key Takeaways**:

- Implementing effective metadata filtering systems to complement semantic search
- Combining structured filters with semantic search for better retrieval
- Measuring and quantifying improvements in retrieval quality
