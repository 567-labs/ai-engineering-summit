# Systematically Improving Your RAG Application

> **Note** : This workshop is a preview of the material from [Systematically Improving RAG Applications](https://maven.com/applied-llms/rag-playbook).
>
> Check out [improvingrag.com](https://improvingrag.com) which walks through the same RAG playbook that you can use in your own application in more detail.

## Installation Instructions

Installing the necessary packages for this set of notebooks is relatively straightforward.

1. First, clone the repository:

```bash
git clone https://github.com/ivanleomk/ai-engineer-summit.git
```

2. Then, make sure to install the necessary packages. We recommend using a virtual environment to do this with `uv`. To install `uv`, you can follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/). Once you've done so, you can install the dependencies by running the following command:

```bash
uv sync
```

3. Once you've done so, you can run the notebooks. Don't forget to select the right kernel.

## Learning Objectives

By the end of this notebook series, you should be able to

1. Understand why you need a systematic approach to building RAG applications
2. Generate your first few synthetic questions to evaluate retrieval
3. Quantify the impact of different techniques like better captioning and metadata filtering using key metrics

Most teams build RAG applications on shaky foundations, assuming retrieval "just works" with semantic similarity. Without a clear way to evaluate retrieval quality and other aspects of your RAG pipeline, teams can't iterate quickly and improve their application. This makes it tricky to know if changes like a new complex re-ranking pipeline or metadata filtering are actually improving retrieval quality.

We'll use an e-commerce RAG application as a case study in this notebook series to demonstrate these key concepts.

### Notebook 1: Why Semantic Search Isn't Enough

**Summary**: In this notebook, we'll talk briefly about why you want to prioritise benchmarking retrieval quality in order to iterate quickly when building a RAG application. We'll then explore some of the limitations of semantic search and how it falls short when handling real-world queries that involve multiple constraints like price ranges, complementary items, and specific product attributes.

**Key Takeaways**:

- Understanding when and why semantic search fails for complex queries
- Identifying common retrieval failure patterns in real-world applications
- Learning to implement basic RAG with proper evaluation methods

### Notebook 2: Systematic RAG Evaluation

**Summary**: In this notebook, we'll discuss how synthetic data can be used to quickly bootstrap an evaluation dataset and some practical considerations to consider when building a synthetic dataset. We'll then show you how to use two simple metrics - Mean Reciprocal Rank (MRR) and Recall - to establish baseline performance measurements for your RAG application.

**Key Takeaways**:

- Understanding the importance of synthetic data in RAG evaluation
- Creating synthetic datasets for testing retrieval quality
- Implementing key metrics to measure RAG system performance

### Notebook 3: Enhancing Retrieval with Metadata

**Summary**: In the last notebook, we'll implement metadata filtering when we recieve a user query. This allows us to filter for results based on implicit user requirements. We'll quantify this improvement by showing how MRR and Recall metrics improve as a result of this filtering before exploring how we might use these same metrics to evaluate the performance of better embedding chunks.

**Key Takeaways**:

- Implementing effective metadata filtering systems to complement semantic search
- Combining structured filters with semantic search for better retrieval
- Measuring and quantifying improvements in retrieval quality
