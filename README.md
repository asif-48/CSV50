# CSV50

A Python-based CSV dataset analysis tool that automatically generates useful summaries of a dataset before further analysis.

## Video Demo

[Watch the demo video](https://www.youtube.com/watch?v=aC1IX4-noSM)

---

## Description

CSV50 is a basic data analysis tool built using Python and the Pandas library.

The goal of this project is to take any dataset in CSV format and generate a text report containing useful information about the dataset before performing further analysis.

The generated report includes:
- General dataset information
- Numerical summaries
- Categorical summaries
- Data quality information

---

# Features

- CSV file validation
- CSV file loading using Pandas
- Dataset overview generation
- Column name cleaning
- Numerical statistical summary
- Categorical data summary
- Automatic report generation
- Unit testing using Pytest

---

# Technologies Used

- Python
- Pandas
- Pytest

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/CSV50.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run:

```bash
python project.py
```

Enter the path of a CSV file when prompted.

Example:

```
Enter the path of the csv file to be analysed:
sample_data.csv
```

The program generates:

```
report.txt
```

containing dataset information and statistical summaries.

---

# Project Functions

## is_csv()

Checks whether the provided file has a valid CSV extension.

It helps ensure that only CSV datasets are processed.

---

## load_csv()

Loads the CSV file using the Pandas library and converts it into a DataFrame.

It also checks whether the dataset is empty before continuing the analysis.

---

## clean_column_name()

Cleans column names by:

- Removing unnecessary spaces
- Replacing spaces between words with underscores

Example:

```
Spending Score 1-100
```

becomes:

```
Spending_Score_1-100
```

---

## get_overview()

Generates general information about the dataset, including:

- First few rows
- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate rows

---

## numeric_summary()

Analyzes numerical columns and generates statistical information including:

- Count
- Mean
- Standard deviation
- Percentiles
- Minimum and maximum values

---

## categorical_summary()

Analyzes categorical columns and provides:

- Number of unique values
- Most common value
- Frequency of the most common value

---

## save_file()

Combines all generated summaries and saves them into:

```
report.txt
```

---

## main()

The main function controls the complete workflow:

1. Checks CSV validity
2. Loads the dataset
3. Cleans column names
4. Generates dataset overview
5. Creates numerical and categorical summaries
6. Saves the final report

---

# Testing

The project includes automated testing using Pytest.

The tested functions are:

## test_is_csv()

Checks valid and invalid CSV file names.

Examples:

- `.csv` files → True
- Other file types → False

---

## test_clean_column_name()

Checks whether column names are cleaned correctly.

Example:

```
Price
Spending_Score_1-100
CustomerID
```

---

## test_numeric_summary()

Checks whether numerical columns are correctly selected and whether statistical summaries are generated properly.

---

# Project Structure

```
CSV50

├── README.md
├── project.py
├── test_project.py
├── requirements.txt
└── sample_data.csv
```

---

# Author

Mohammad Asiful Islam
