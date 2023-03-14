# Download the dataset
wget https://www.statmt.org/wmt16/metrics-task/wmt2016-seg-metric-dev-5lps.tar.gz

# Unzip the dataset
tar -xvzf wmt2016-seg-metric-dev-5lps.tar.gz

# Move the dataset to the data/ directory. If the data/ directory already exit, overwrite it.
rm -rf data/wmt2016-seg-metric-dev-5lps
mv wmt2016-seg-metric-dev-5lps data/

# Remove the compressed file
rm wmt2016-seg-metric-dev-5lps.tar.gz
