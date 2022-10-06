#!/bin/bash

set -e
set -u
set -o

# test python scripts with pycodestyle
pycodestyle *.py

# run unit tests
python3 test_utils.py

# run functional tests
bash test_search.sh

# define variables
gene_reads=$1
sample_attributes=$2
gene=$3
output_file=$4

# run example python script
python3 plot_gtex.py \
  --gene_reads "$gene_reads" \
  --sample_attributes "$sample_attributes" \
  --gene "$gene" \
  --output_file "$output_file"

