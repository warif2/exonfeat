# ExonFeat Analysis Script
A collection of scripts for analysis rMATS data. 
Still in development.

## Hardware and Software Requirements
  * 64 bit Linux or Mac OS X
  * Python 3.6 or higher
  * bedtools suite in path
  
## Setting up a virtual environment (Optional)
It is recommended to create a virtual environment before setting
up the script to avoid errors with dependencies. To install Anaconda,
follow the instructions available here, https://docs.anaconda.com/anaconda/install/.

```bash
# Creating venv with the name 'exonfeat' using anaconda
conda create -n exonfeat python=3.6

# Activate venv
conda activate exonfeat
```
  
## Download and Installation

```bash
# Download the latest release of toolkit using git
git clone https://github.com/warif2/exonfeat.git

# Install python packages dependencies using
pip install -r /exonfeat/requirements.txt
```

Finally, run setup.py to obtain the license key needed to run the tools.
```bash
# Run setup.py
cd exonfeat/
python setup.py
```
*Note: enter the 'user' and 'pin' information provided. If you want to use the script and need a 'user' and 'pin', please contact me on waqar.github@gmail.com

## Quick Command Line Usage
Step 1: Create transcript database.
```bash
# Example on how to run command tx_db.py
python tx_db.py -gff <path_to_gff_file> -fa <path_to_fasta_genome> -out <output_path> -t <#_of_threads>
```

Once transcript database is created, exon feature analysis can be performed  
  
Step 2: Run exonfeat.py on filtered rMATS output file
```bash
# Example on how to run command exonfeat.py
python exonfeat.py -rf <path_to_rMATS> -o <output_path> -db <path_to_tx_db>
```

