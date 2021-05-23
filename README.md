# ExonFeat Analysis Script
A collection of scripts for analysis rMATS data. 
Still in development.

## Hardware and Software Requirements
  * 64 bit Linux or Mac OS X
  * Python 3.6 or higher
  * bedtools suite in path
  
## Setting up a virtual environment (Optional)
It is recommended to create a virtual environment before setting
up the script to avoid errors with dependencies.

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

Finally, run setup.py to obtain the license key needed to run the tools. It also provides the
option of adding the directory to your PATH variable which allows calling the tool
from any directory.
```bash
# Run setup.py
cd exonfeat/
python setup.py

Note: After setup, refresh terminal for PATH update to take effect.
If exonfeat is still not callable, you might need to modify permissions of scripts.

# For example, change tx_db.py permission to allow system-wide execution.
chmod 755 tx_db.py
```

## Quick Command Line Usage
Step 1: Create transcript database.
```bash
# Example on how to run command tx_db.py
python tx_db.py -gff <path_to_gff_file> -fa <path_to_fasta_genome> -out <output_path> -t <#_of_threads>
```

Once transcript database is created, exon feature analysis can be performed  
  
Step 2: Run exonfeat.py on filtered rMATS output
```bash
# Example on how to run command exonfeat.py
python exonfeat.py -rf <path_to_rMATS> -o <output_path> -db <path_to_tx_db>
```

