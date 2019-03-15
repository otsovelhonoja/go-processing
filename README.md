# Go-Processing

My solution for Holm Group's coding test (summer 2019)

### Prerequisites

Requires only Python3 to run 

### Installation

To use go-processing, you can
```
git clone https://github.com/otsovelhonoja/go-processing
```
or just download `go_processing.py` and `go_processing_functions.py` to your desired folder.  

This repository also contains the sample data for which this program was initially built for. These files are located in compressed format in the `data/` folder. For simplicity's sake, it's best to download this folder and unzip the files.

### Usage

There are **three** possible ways to run the program:

#### 1.
With the example data uncompressed in `data/`, you can get the top 50 most common classes with:

```
python go_processing.py
```

#### 2.
With the example data uncompressed in `data/`, you can also specify how many classes to show. For example to get the top 100 classes:
```
python go_processing.py 100
```

#### 3.
You can also specify the path to two input files and the number of classes to show. Note however that this program is currently built only for the sample data, so it most likely wont work with other files.
```
python go_processing.py <file1> <file2> <n>
```