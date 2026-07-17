# CSV50

#### Video Demo:  [https://www.youtube.com/watch?v=aC1IX4-noSM](https://www.youtube.com/watch?v=aC1IX4-noSM)

#### Description:

The name of this project is CSV50. The goal of this project was to take any dataset as a csv file and then output a text file consisting of various summaries and general information about the dataset that can be helpful for getting an overview of the dataset before jumping onto the further analyses that can be done upon it. It is mainly a very basic tool for data analysis built using the Pandas library in Python. Let us go through the various functions of the project in the project.py file.

---

### `is_csv()`

This function takes the system path for any file and checks its validity making use of some string based function in python. While this may seem a simple function, it is essential for the next steps of the code. Originally it also used the os library to check if the file actually existed or not, but due to complications in testing, this functionality was moved over to main function.

---

### `load_csv()`

This block takes the valid csv file and then uses the pandas library to turn it into a dataframe (df), which is the pandas equivalent of a csv file upon which a myriad of data analysis can be done. It also reports back if the file is empty or not; if yes, the program exits upon stating it.

---

### `clean_column_name()`

This block takes the names of the columns in the dataset and strips any unnecessary whitespaces and replaces spaces between words with underscores. While initially it took all of the columns at once, for ease of testing I opted for single column names taken from the main function and then updated the names of the columns in the dataframe.

---

### `get_overview()`

Here we arrive at the first major summarizing function. This function takes the df and outputs the first few lines of it, and a bunch of general information about the data such as number of rows and columns, columns’ names and datatypes, number of NaN/Null values and duplicate rows, and compiles all of this into a string and reports it back to the main function.

---

### `numeric_summary()`

This function takes the dataframe, selects any of the columns that have numerical data associated with them and then outputs a statistical summary containing very basic information such as mean, median and data at various percentiles, i.e 25, 50, 75 etc. More detail could have been added to this function, but since this is a very general tool, I did not yet understand how to go into specifics.

---

### `categorical_summary()`

Since we have a numeric summary, a categorical summary was only appropriate. This function selects columns of `"object"`, `"category"`, `"bool"` or `"string"` type and outputs unique values, most common values, and their frequencies for each column. This function was the most challenging for me to implement because it required good knowledge of how the outputs in pandas worked and the formatting of the outputs of various methods in pandas.

---

### `save_file()`

This was a simple function to implement, whereby it took the various outputs from the above functions and stored it into a report text file, joining them using `'\n' + '\n'` to separate each of the summaries from one another.

---

### `main()`

This is the function which calls upon each of the custom functions. It checks whether the file exists and is valid or not, then whether the file is empty or not, then cleans the column names, gets the overview, gets the numeric summary and categorical summary, and finally saves all the information in a text file.

---

Now let us go through the various functions of the project in the `test_project.py` file.

As per the final project requirement, this tests 3 helper functions of the project. My chosen functions are the `is_csv()`, `clean_column_name()` and `numeric_summary()` functions.

---

### `test_is_csv()`

Checks for valid and invalid csv file names and verifies Boolean outputs as required.

---

### `test_clean_column_name()`

Checks if the column names are being properly cleaned and formatted for a standard look.

---

### `test_numeric_summary()`

Checks if the function is properly selecting the numeric columns, generating a summary, and whether the output contains the expected summary fields.
