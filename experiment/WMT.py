from metrics import load_all_metrics
from benchmark_datasets import get_wmt_data
import pandas as pd

if __name__ == "__main__":
    dataset = get_wmt_data()
    metrics = load_all_metrics()
    results = pd.DataFrame()
    results["human_scores"] = dataset.human_scores
    for name, metric in metrics.items():
        results[name] = metric(dataset.references, dataset.candidates)
        results.to_csv("results.csv", index=False)

    # Pearson correlation coefficient
    results.corr(method="pearson")

    # Spearman correlation coefficient
    results.corr(method="spearman")

    # Kendall's tau
    results.corr(method="kendall")
