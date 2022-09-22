# Plot Gene Read Counts by Tissue for Specified Gene 

## Description 

This script takes two files: one containing sample metadata and the other containing read counts for different genes by 
sample. It will also take a user picked gene and plot a box plot of gene read counts by tissue type.

## Workflow 

### Arguments 

Here is a list of required and optional arguments that can be accessed by typing **python .\plot_gtex.py -h** from the 
terminal in the directory containing the *plot_gtex.py* file.

```text
usage: plot_gtex.py [-h] --gene_reads GENE_READS --sample_attributes SAMPLE_ATTRIBUTES --gene GENE [--output_file OUTPUT_FILE]

This script plots tissue by gene read counts for a gene

optional arguments:
  -h, --help            show this help message and exit
  --gene_reads GENE_READS, -gr GENE_READS
                        file path to zipped file containing gene read counts
  --sample_attributes SAMPLE_ATTRIBUTES, -sa SAMPLE_ATTRIBUTES
                        file path to text file containing sample metadata
  --gene GENE, -g GENE  gene of interest's name
  --output_file OUTPUT_FILE, -of OUTPUT_FILE
                        output file path for plot
```

### Inputs 

This script requires two types of input files. The first is a text file containing samples metadata (e.g. tissues 
samples were collected from), such as: 

```text
SAMPID	SMATSSCR	SMCENTER	SMPTHNTS	SMRIN	SMTS	SMTSD	SMUBRID	SMTSISCH	SMTSPAX	SMNABTCH	SMNABTCHT	SMNABTCHD	SMGEBTCH	SMGEBTCHD	SMGEBTCHT	SMAFRZE	SMGTC	SME2MPRT	SMCHMPRS	SMNTRART	SMNUMGPS	SMMAPRT	SMEXNCRT	SM550NRM	SMGNSDTC	SMUNMPRT	SM350NRM	SMRDLGTH	SMMNCPB	SME1MMRT	SMSFLGTH	SMESTLBS	SMMPPD	SMNTERRT	SMRRNANM	SMRDTTL	SMVQCFL	SMMNCV	SMTRSCPT	SMMPPDPR	SMCGLGTH	SMGAPPCT	SMUNPDRD	SMNTRNRT	SMMPUNRT	SMEXPEFF	SMMPPDUN	SME2MMRT	SME2ANTI	SMALTALG	SME2SNSE	SMMFLGTH	SME1ANTI	SMSPLTRD	SMBSMMRT	SME1SNSE	SME1PCTS	SMRRNART	SME1MPRT	SMNUM5CD	SMDPMPRT	SME2PCTS
GTEX-1117F-0003-SM-58Q7G		B1			Blood	Whole Blood	0013756	1188		BP-38516	DNA isolation_Whole Blood_QIAGEN Puregene (Manual)	05/02/2013	LCSET-4574	01/15/2014	Standard Exome Sequencing v3 (ICE)	WES																																														
GTEX-1117F-0003-SM-5DWSB		B1			Blood	Whole Blood	0013756	1188		BP-38516	DNA isolation_Whole Blood_QIAGEN Puregene (Manual)	05/02/2013	GTEx_OM25_Dec_01	01/28/2014	Illumina OMNI SNP Array	OMNI																																														
```

The second file should be a *.gz* tab delimited file containing gene read counts for gene in each sample. For example: 

![image of gene read counts file](https://github.com/cu-swe4s-fall-2022/assignment-3-parallel-arrays-acolorado1/blob/7614a7d95ea6afc97f0f848bea42cf0303a08e79/gene_read_counts.png)

### Command 

To run this program in the command line interface type: 

```text
python .\plot_gtex.py --gene_reads ".\GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz" --sample_attributes ".\GTEx_Analysis_v
8_Annotations_SampleAttributesDS.txt" --gene "SDHB" [--output_file "SDHB.png"]

```

Note: The output_file argument is the only one that is not required as it has a default. All other arguments the user 
must input. User MUST put in their own file paths for the input files. 

### Output 

The output of this script is a boxplot that is saved in the form of a *.png*. Example outputs using genes ACTA2 and SDHB
look like: 

![Example Boxplot using gene ACTA2](https://github.com/cu-swe4s-fall-2022/assignment-3-parallel-arrays-acolorado1/blob/7614a7d95ea6afc97f0f848bea42cf0303a08e79/ACTA2.png)

![Example Boxplot using gene SDHB](https://github.com/cu-swe4s-fall-2022/assignment-3-parallel-arrays-acolorado1/blob/7614a7d95ea6afc97f0f848bea42cf0303a08e79/SDHB.png)

## Release History
+ 1.0 
  + ADD: Linear search function
  + ADD: Binary search function 
  + ADD: Indexing function that is needed for the binary search. It takes a list and creates a list of tuples containing each value in the list (x) and its original index (y). It then sorts this list by the first value (x) in the tuple.
  + ADD: Boxplot visualizing function using package matplotlib. 
  + ADD: Functions for data read in. 
  + ADD: Functions for obtaining gene expression counts per sample by tissue. 
  + ADD: Parser so user is able to run script through the command line. 

## Installation and Dependencies 

You must have Python 3 installed. Any Python 3 version should work, but it was written in Python 3.9 using a Windows-based 
operating system. Packages matplotlib 3.6.0, and argparse 1.4.0 will need to be installed. 

## Contact 

Angela Sofia Burkhart Colorado - angelasofia.burkhartcolorado@cuanschutz.edu



