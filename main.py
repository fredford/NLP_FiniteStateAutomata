import os
import pandas as pd

from extractor import Extractor


def get_filenames(filepath):
    """
    Function used to get all of the file names in the specified directory.

    Arguments:
        filepath -- String specifying the root directory

    Return:
        dataFiles -- Dictionary with keys as file name and value as file path
    """

    dataFiles = {}

    for root, dirs, filenames in os.walk(filepath):

        filenames = sorted(filenames, key=lambda x: int(x.split(".")[0]))
        for filename in filenames:
            dataFiles[filename] = os.path.join(root, filename)

    return dataFiles

def main ():

    # Directory storing data files to be processed
    path = "data/dev"

    # Call function to receive dictionary of filenames in the specified directory
    dataFiles = get_filenames(path)

    # Counter for adding rows to Pandas DataFrame
    counter = 0

    # Initialize Pandas DataFrame
    df = pd.DataFrame(columns=["article_id", "expr_type", "value", "char_offset"])

    # Iterate through every file in the directory
    for filename, filepath in dataFiles.items():

        # Open the current file
        dataFile = open(filepath, "r")

        # Initialize Extractor object
        ext = Extractor(dataFile, filename)

        # Process RegEx
        ext.process_data()

        # Output the data returned from the extraction
        output_data = ext.get_data()

        # Add all output data to the DataFrame
        for row in output_data:
            df.loc[counter] = [row[0], row[1], row[2], row[3]]
            counter+=1

        # Close the current file
        dataFile.close()

    # Write the data to a CSV file
    df.to_csv("output.csv", index=False)

main()