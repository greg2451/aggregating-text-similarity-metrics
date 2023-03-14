# Aggregating Text Similarity Measures for NLG Evaluation

## Introduction

This repository consists of a benchmark of various text similarity measures for Natural Language Generation (NLG) evaluation, on multiple datasets.

Measuring the similarity between two texts is a fundamental task in Natural Language Processing (NLP). It is used in many applications, such as machine translation, text summarization, and NLG evaluation. As it is very hard to formally define what a good similarity should be, we use the common gold standard of correlation with human judgement.

In this repository, we provide a Python module to easily compute these measures on specific datasets that are particularly relevant for NLG evaluation. Indeed, these datasets contain pairs of texts that are similar, and are annotated by humans to quantify the degree of similarity.

We also provide a way to aggregate these measures [WIP]

## Technical details

### Datasets

[WIP]

### Similarity Measures

[WIP]

### Correlation

[WIP]


## Usage

### Installation

First, install the module
```shell
pip install torch numpy "git+https://github.com/PierreColombo/nlg_eval_via_simi_measures"
```