import os
import tarfile
import urllib.request
from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

WMT_2016_PATH = os.path.join(DATA_PATH, "wmt2016-seg-metric-dev-5lps")


@dataclass_json
@dataclass
class SimilarityEvaluationDataset:
    references: List[str]
    candidates: List[str]
    human_scores: List[float]

    @classmethod
    def load_wmt_2016(cls, only_english: bool = True):
        if not os.path.exists(WMT_2016_PATH):
            download_wmt16()
        human_scores = []
        candidates = []
        references = []
        for language in [
            lang
            for lang in os.listdir(WMT_2016_PATH)
            if (not only_english or lang.endswith("en"))
        ]:
            with (
                open(
                    os.path.join(
                        WMT_2016_PATH,
                        language,
                        f"newstest2015.human.{language}",
                    ),
                    "r",
                ) as human_scores_file,
                open(
                    os.path.join(
                        WMT_2016_PATH,
                        language,
                        f"newstest2015.mt-system.{language}",
                    ),
                    "r",
                ) as candidates_file,
                open(
                    os.path.join(
                        WMT_2016_PATH,
                        language,
                        f"newstest2015.reference.{language}",
                    ),
                    "r",
                ) as references_file,
            ):
                human_scores += [
                    float(score.strip()) for score in human_scores_file.readlines()
                ]
                candidates += [
                    candidate.strip() for candidate in candidates_file.readlines()
                ]
                references += [
                    reference.strip() for reference in references_file.readlines()
                ]

        assert (
            len(human_scores) == len(candidates) == len(references)
        ), "The number of human scores, candidates and references should be the same"

        return cls(references, candidates, human_scores)


def download_dataset(url: str, name: str):
    urllib.request.urlretrieve(url, name)
    with tarfile.open(name) as tar:
        tar.extractall(DATA_PATH)
    os.remove(name)


def download_wmt16():
    url = "https://www.statmt.org/wmt16/metrics-task/wmt2016-seg-metric-dev-5lps.tar.gz"
    name = "wmt2016-seg-metric-dev-5lps.tar.gz"
    download_dataset(url, name)


if __name__ == "__main__":
    download_wmt16()
