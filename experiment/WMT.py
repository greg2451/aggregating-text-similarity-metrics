from metrics import load_all_metrics
from benchmark_datasets import get_wmt_data
import numpy as np
import pandas as pd

if __name__ == "__main__":
    dataset = get_wmt_data()
    metrics = load_all_metrics()
    scores = np.zeros((len(metrics), len(dataset)))
    for index, metric in enumerate(metrics.values()):
        scores[index] = metric(dataset.references, dataset.candidates)

    results = pd.DataFrame(scores.T, columns=list(metrics.keys()))
    results["human_scores"] = dataset.human_scores
    results.to_csv("results.csv", index=False)

    # Pearson correlation coefficient
    results.corr(method="pearson")

    # Spearman correlation coefficient
    results.corr(method="spearman")

    # Kendall's tau
    results.corr(method="kendall")
