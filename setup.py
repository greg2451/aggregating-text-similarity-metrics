from setuptools import setup, find_packages

import os


DIR = os.path.realpath(os.path.dirname(__file__))


with open(os.path.join(DIR, "requirements.txt")) as f:
    requirements = [line.strip() for line in f.readlines()]


with open(os.path.join(DIR, "README.md"), encoding="utf-8") as readme_file:
    readme = readme_file.read()


setup(
    name="aggregating-text-similarity-metrics",
    version="0.0.2",
    url="https://github.com/greg2451/aggregating-text-similarity-metrics.git",
    author="Grégoire Retourné, Hugo Peltier",
    author_email="gregoire.retourne@gmail.com",
    short_description="Aggregating text similarity metrics",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    install_requires=requirements,
    packages=find_packages(),
    keywords=["natural language processing", "text similarity", "metrics aggregation"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={"": ["data/*"]},
    include_package_data=True,
)
