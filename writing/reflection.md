# Data Analysis

## Gregory M. Kapfhammer

## Program Input and Output

### What is the output from running the following commands?

Note: Use a fenced code block to provide the output for this command.

`poetry run dataanalysis --data-file input/data.txt`

```
📦 The data file contains 50 data values in it!

🚀 Let's do some sophisticated data analysis!

🧮 Here are the results of the data analysis:

    The computed mean is 87.80!
    The computed median is 88.05!

    The computed variance is 3.69!
    The computed standard deviation is 1.92!

💡 What does this tell you about the population of this city?
```

### What are the first five lines of the contents of the file that is input into the `datasummarizer`?

Note: Use a fenced code block to provide the contents of the file.

```
1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
```

### What is the output from running the test suite with the command `poetry run task test`?

Note: Use a fenced code block to provide the output from running the test suite.

```
=========================== test session starts ============================
platform linux -- Python 3.9.2, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/gkapfham/working/teaching/github-classroom/proactive-programmers/discrete-structures/solutions/engineering-efforts/data-analysis-solution/dataanalysis
collected 13 items

tests/test_summarize.py ...........
tests/test_transform.py ..

============================ 13 passed in 0.02s ============================
```

## Source Code

### Describe in detail how your provided source code works

#### What is a function that analyzes a data set by computing the standard deviation? How does it work?

Note: Use a fenced code block to provide the requested source code
Note: Write at least one paragraph to explain the requested source code

```
def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    # call the function to calculate the variance
    variance = compute_variance(numbers)
    # calculate the standard deviation as the square root of the variance
    return variance ** 0.5
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

#### What is the purpose of the following function in the context of the `display` module?

Note: Write at least one paragraph to explain the provided source code

```
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
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.

#### What is the purpose of the following function in the context of the `summarize` module?

Note: Write at least one paragraph to explain the provided source code

```
def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # compute the mean
    mean = compute_mean(numbers)
    # compute the differences from the mean
    differences = []
    for number in numbers:
        differences.append(number - mean)
    return differences
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.

## Professional Development

### What are some examples of computer science skills that were important 30 years ago but are less important to learn now? Why are they less important now?

Note: Provide a one-paragraph response to this question, using source code or commands for reference as needed

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.

### What are some examples of computer science skills that were important 30 years ago but are just as important to learn now? Why are they as important now as in the past?

Note: Provide a one-paragraph response to this question, using source code or commands for reference as needed

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum
dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.
