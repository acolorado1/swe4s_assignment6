import gzip
import argparse as arg
import viz_lib
import utils


# get sample information
def ReadInSamples(file_path, sample_info_header=None):
    samples = []

    try:
        # get header and each line of sample information
        for line in open(file_path):
            if sample_info_header is None:
                sample_info_header = line.rstrip().split("\t")
            else:
                samples.append(line.rstrip().split("\t"))
    except FileNotFoundError:
        print("File path not found")
        exit()
    except PermissionError:
        print("File permissions preventing file read in")
        exit()

    return [sample_info_header, samples]


# get expression information
def ReadInExpressionInfo(file_path):
    samples = []
    line_number = 0

    try:
        # get header and each line of sample information
        for line in gzip.open(file_path, "rt"):
            if line_number == 2:
                sample_info_header = line.rstrip().split("\t")
            if line_number > 2:
                samples.append(line.rstrip().split("\t"))
            line_number += 1
    except FileNotFoundError:
        print("File path not found")
        exit()
    except PermissionError:
        print("File permissions preventing file read in")
        exit()

    return [sample_info_header, samples]


# for each tissue type get list of sample IDs
def GetSampleInfo(header_samples):
    sample_info_header = header_samples[0]
    samples = header_samples[1]
    tissue_types = []
    sample_ids = []

    # find index of sample type column and sample ID column
    tissue_column = utils.linear_search(sample_info_header, "SMTS")
    ID_column = utils.linear_search(sample_info_header, "SAMPID")

    # for each tissue type get list of sample IDs
    for sample in samples:
        current_ID = sample[ID_column]
        tissue = sample[tissue_column]
        # if tissue not in list append and create tissue and sample IDs
        if tissue not in tissue_types:
            tissue_types.append(tissue)
            sample_ids.append([current_ID])
        # else find index of current tissue and append sample ID to list
        else:
            tissue_index = utils.linear_search(tissue_types, tissue)
            sample_ids[tissue_index].append(current_ID)

    return [tissue_types, sample_ids]


# get expression values of each gene for specific sample
def GetSampleExpression(header_rows_expression, samples_list, gene):
    header_exp = header_rows_expression[0]
    rows_exp = header_rows_expression[1]
    header_exp_sorted = utils.index_list(header_exp)
    gene_exp = []
    sample_exps = []

    # find line containing specified gene expression
    for gene_exp_line in rows_exp:
        if gene_exp_line[1] == gene:
            gene_exp = gene_exp_line
    if len(gene_exp) == 0:
        print(gene + ": was not found ")
        raise ValueError

    # get list of samples in each tissue
    for tissue in samples_list:
        tissue_exp = []

        # for each sample
        for sample in tissue:
            sample_index = utils.binary_search(header_exp_sorted, sample)

            # if no index for the sample is found continue
            if sample_index == -1:
                continue
            else:
                sample_exp = int(gene_exp[sample_index])
                tissue_exp.append(sample_exp)
        sample_exps.append(tissue_exp)
    return sample_exps


def main():
    parser = arg.ArgumentParser(
        description="This script plots tissue by gene read counts for a gene"
    )
    parser.add_argument(
        "--gene_reads",
        "-gr",
        type=str,
        required=True,
        help="file path to zipped file containing gene read counts",
    )
    parser.add_argument(
        "--sample_attributes",
        "-sa",
        type=str,
        required=True,
        help="file path to text file containing sample metadata",
    )
    parser.add_argument(
        "--gene",
        "-g",
        type=str,
        required=True,
        help="gene of interest's name"
    )
    parser.add_argument(
        "--output_file",
        "-of",
        type=str,
        required=False,
        help="output file path for plot",
        default='figure.png'
    )

    args = parser.parse_args()

    header_samples_attributes = ReadInSamples(args.sample_attributes)
    tissues_samples = GetSampleInfo(header_samples_attributes)
    header_samples_expression = ReadInExpressionInfo(args.gene_reads)
    tissue_counts = GetSampleExpression(
        header_samples_expression, tissues_samples[1], args.gene
    )
    viz_lib.make_box_plot(
        tissues_samples[0], tissue_counts, args.gene, output_file=args.output_file
    )

    exit()


if __name__ == "__main__":
    main()
