import matplotlib.pyplot as plt


def make_box_plot(
    tissues,
    expression_values,
    figure_name,
    xaxis_name="SMTS",
    yaxis_name="Gene Read Counts",
    figure_size=(10, 4),
    output_file="figure.png",
):
    # get the data ready for figure
    tissue_types = [tissue for tissue in tissues]
    sample_values = [values for values in expression_values]

    # set up the figure
    _, ax = plt.subplots(figsize=figure_size, dpi=300)

    # plot the values
    plt.boxplot(sample_values)

    # set axis labels and formats
    ax.set_xticklabels(tissue_types)
    ax.ticklabel_format(style="plain", axis="y")
    plt.xticks(rotation=90)

    # set figure names
    plt.title(figure_name)
    plt.xlabel(xaxis_name)
    plt.ylabel(yaxis_name)

    plt.tight_layout()
    plt.savefig(output_file)
