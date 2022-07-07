"""Transform the data set containing recorded population data values."""

from typing import List

# Reference for the data set:
# https://fred.stlouisfed.org/series/PACRAW0POP

# Sample of the data set:

# 1970-01-01,81.342
# 1971-01-01,83.300
# 1972-01-01,84.700
# 1973-01-01,85.500
# 1974-01-01,86.100
# 1975-01-01,87.000
# 1976-01-01,87.600
# 1977-01-01,87.600
# 1978-01-01,88.000
# 1979-01-01,88.100
# 1980-01-01,88.869


def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string of (date, float) values to a list of floats."""
    data_number_list = []
    # iterate through each line of the data set
    for line in data_text.splitlines():
        # extract the ordered pair this line
        # the ordered pair has the format:
        # (Date, population count in thousands of persons)
        ordered_pair = line.split(",")
        # convert the population count to a float and store it
        # in the data_number_list
        data_number_list.append(float(ordered_pair[1]))
    # return the data_number_list
    return data_number_list
