import os
from dataclasses import dataclass
from typing import List
import pkg_resources

from dataclasses_json import dataclass_json


DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
WMT_PATH = os.path.join(DATA_PATH, "DAseg-wmt-newstest")


@dataclass_json
@dataclass
class SimilarityEvaluationDataset:
    references: List[str]
    candidates: List[str]
    human_scores: List[float]

    def __len__(self):
        return len(self.references)


def get_wmt_data(only_english: bool = True) -> SimilarityEvaluationDataset:
    human_scores = []
    candidates = []
    references = []
    for year in [2016, 2017]:
        for language in [
            lang
            for lang in os.listdir(
                pkg_resources.resource_stream(__name__, f"{WMT_PATH}{year}")
            )
            if (not only_english or lang.endswith("en"))
        ]:
            with (
                open(
                    pkg_resources.resource_stream(
                        __name__,
                        os.path.join(
                            f"{WMT_PATH}{year}",
                            language,
                            f"newstest{year}.human.{language}",
                        ),
                        "r",
                    )
                ) as human_scores_file,
                open(
                    pkg_resources.resource_stream(
                        os.path.join(
                            f"{WMT_PATH}{year}",
                            language,
                            f"newstest{year}.mt-system.{language}",
                        ),
                        "r",
                    )
                ) as candidates_file,
                open(
                    pkg_resources.resource_stream(
                        os.path.join(
                            f"{WMT_PATH}{year}",
                            language,
                            f"newstest{year}.reference.{language}",
                        ),
                        "r",
                    )
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

        return SimilarityEvaluationDataset(references, candidates, human_scores)


if __name__ == "__main__":
    wmt_dataset = get_wmt_data()
    print(len(wmt_dataset))
