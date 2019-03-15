# Go-Processing

My solution for the Holm Group's coding test (summer 2019)

### Prerequisites

Requires only Python3 to run 

### Installation

To use go-processing, you can:
```
git clone https://github.com/s1xgill/go-processing
```
or just download `go_processing.py` and `go_processing_functions.py` to your desired folder. This repository also contains the sample data for which this program was initially built for. These files are located in the `data/` folder.

### Usage

To run, you need to supply `go_processing.py` with two files:

```
python go_processing.py <file1> <file2> 
```
`<file1>` should contain the GO-ids for specific genes in a table format. This program currently only works when the gene names are in the 2nd column and the GO-ids in the 4th column. Check `data/gene_association.mgi` for reference.  
`<file2>` should contain the GO-ids (3rd column) with their class names (4th column) as well as their parent classes (5th column). Check `data/mergeGO.out` for reference.