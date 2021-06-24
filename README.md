# Regular Expressions

This is a simple implementation of regular expressions to extract simple dates (June 23, 2021) as well as deictic date information (next Friday) from a data set of new articles. The objective is to produce as many regular expressions as possible that are capable of extracting the highest number of valid date related pieces of information.

## Data

The assignment's development data can be found inside [data/dev](data/dev).

## 1. Members

- Scott Kavalinas - skavalin
- Fraser Redford - fredford

## 2. Listed Resources

- https://regexr.com/ - Used to test expressions on single files
- https://github.com/fredford/DataEng_Proj1 - Used for reading in files
- https://datatofish.com/export-dataframe-to-csv/ - Exporting to csv

## 3. Installation

### Requirements

- Python3
- Pandas

The program can be run directly from the project directory if the user has Pandas installed using:

```
$ python3 main.py
```

If the user does not have `pandas`, then they can run the program by first installing:

```
$ pip install pandas
```

The program will effectively operate within the confines of the `main.py` and the provided inputs. An CSV file `output.csv` will be generated when `main.py` is run.
