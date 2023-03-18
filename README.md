# Aggregating Text Similarity Measures for NLG Evaluation

## Introduction

This repository consists of a benchmark of various text similarity measures for Natural Language Generation (NLG) evaluation, on multiple datasets.

Measuring the similarity between two texts is a fundamental task in Natural Language Processing (NLP). It is used in many applications, such as machine translation, text summarization, and NLG evaluation. As it is very hard to formally define what a good similarity should be, we use the common gold standard of correlation with human judgement.

In this repository, we provide a Python module to easily compute these measures on specific datasets that are particularly relevant for NLG evaluation. Indeed, these datasets contain pairs of texts that are similar, and are annotated by humans to quantify the degree of similarity.

We also provide a way to aggregate these measures through Kemeny ranking consensus [WIP]

## Technical details

### Datasets

We used WMT2016, WMT2017. We provide a downloading script for WMT2016, and data can be found [here](aggregating_text_similarity_metrics/benchmark_datasets/data)

### Similarity Measures

We used the following similarity measures:
- BLEU
- CHRF
- METEOR
- ROUGE
- TER
- BERTScore
- BaryScore
- DepthScore
- InfoLM
- SacreBLEU

### Correlation

We provide results for the three classical correlation measures:
- Pearson
- Spearman
- Kendall


## Usage

### Getting the code

Clone the repository:

```sh
git clone https://github.com/greg2451/aggregating-text-similarity-metrics.git
```

### Configuration

1. Install conda locally following this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html).
   We recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html), it is more lightweight and will be sufficient for our usage.
2. Create a new conda environment by executing the following command in your terminal:

   ```sh
   conda create -n aggregating_text_similarity_metrics python=3.10
   conda activate aggregating_text_similarity_metrics
   conda install pip
   ```

3. Having the conda environnement activated, install the [requirements](requirements.txt):

   ```sh
   pip install -r requirements.txt
   ```

### Running the benchmark

To run the benchmark, you can use the [jupyter notebook](aggregating_text_similarity_metrics/wmt_experiment.ipynb) or run the [python file](aggregating_text_similarity_metrics/run_wmt_experiment.py):

```sh
cd aggregating_text_similarity_metrics
export PYTHONPATH=$PYTHONPATH:$(pwd)
python run_wmt_experiment.py
```

> Note that you need to have the `PYTHONPATH` set to the root of the repository, so that the `aggregating_text_similarity_metrics` module can be found.

The expected output is to create a folder `results` containing the results of the benchmark on all the WMT data we have, for all the similarity measures.
This folder will also contain the correlation results for all the similarity measures.


You can also install the package locally and run the benchmark:

```sh
pip install -e .
python -m aggregating_text_similarity_metrics.run_wmt_experiment
```


## Development setup

This section should only be necessary if you want to contribute to the project.

Start by installing the [dev-requirements](dev-requirements.txt):

```sh
pip install -r dev-requirements.txt
```

### Enabling the pre-commit hooks

Run the following command at the root of the repository:

```sh
pre-commit install
```
