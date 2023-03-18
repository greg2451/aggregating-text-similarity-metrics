import os

from metrics import load_all_metrics
from benchmark_datasets import get_wmt_data
import pandas as pd
from datetime import datetime

DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    # Create result dir
    now = str(datetime.now())[:19]
    os.makedirs(os.path.join(DIR, f"results/run_{now}"))

    # Load dataset and metrics
    dataset = get_wmt_data()
    metrics = load_all_metrics()
    results = pd.DataFrame()
    results["human_scores"] = dataset.human_scores

    # Loop over metrics
    for name, metric in metrics.items():
        scores = metric(dataset.references, dataset.candidates)
        for sub_metric_name, sub_score in scores.items():
            results[sub_metric_name] = sub_score

        # Save checkpoint, this is very useful in case of crash
        results.to_csv(
            os.path.join(DIR, f"results/run_{now}/checkpoint.csv"), index=False
        )

    # Save final result and delete checkpoints
    columns_in_right_order = ["human_scores"] + [
        column for column in sorted(results.columns) if column != "human_scores"
    ]
    results = results.reindex(columns_in_right_order, axis=1)
    results.to_csv(os.path.join(DIR, f"results/run_{now}/final.csv"), index=False)
    os.remove(os.path.join(DIR, f"results/run_{now}/checkpoint.csv"))

    # Compute correlations and save them
    os.makedirs(os.path.join(DIR, f"results/run_{now}/correlations"))
    for correlation_type in ["pearson", "spearman", "kendall"]:
        results.corr(method=correlation_type).to_csv(
            os.path.join(DIR, f"results/run_{now}/correlations/{correlation_type}.csv")
        )
