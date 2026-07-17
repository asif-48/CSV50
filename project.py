import os
import pandas as pd


def is_csv(pathstr):
        if pathstr.lower().endswith(".csv"):
            return True
        else:
            return False

def load_csv(pathstr):
    df=pd.read_csv(pathstr)
    load_csv_op=(df,df.empty)
    return load_csv_op

def get_overview(df):
    print(df.head(5))
    files=[]
    files.append("Basic information about the dataset:")
    files.append("Number of rows:" + str(df.shape[0]))
    files.append("Number of columns:" + str(df.shape[1]))
    files.append("Columns: " + str(df.columns.tolist()))
    files.append("Datatypes: " + str(df.dtypes))
    files.append("No. of NaN/Null values: " + str(df.isna().sum()))
    files.append("No. of duplicate rows: " + str(df.duplicated().sum()))
    return "\n".join(files)

def clean_column_name(col):
    col=col.strip()
    col=col.replace(" ","_")
    return col

def numeric_summary(df):
    num_df=df.select_dtypes(include="number")
    if not num_df.empty:
        num_sum=num_df.describe()
        return str(num_sum)
    else:
        return 'No numeric columns in data'

def categorical_summary(df):
    cat_df = df.select_dtypes(include=["object", "category", "bool","string"])
    if not cat_df.empty:
        cat_sum = []
        for col in cat_df:
            data = cat_df[col]
            counts = data.value_counts()
            cat_sum.append(col)
            cat_sum.append("Unique points: " + str(data.nunique()))
            if counts.empty:
                cat_sum.append("Most common value: None")
                cat_sum.append("Occurences of Most common value: 0")
            else:
                cat_sum.append("Most common value: " + str(counts.idxmax()))
                cat_sum.append("Occurences of Most common value: " + str(counts.max()))
            cat_sum.append("")
        return "\n".join(cat_sum)
    else:
        return "No categorical columns in data"

def save_file(lines,num_sum,cat_sum):
    with open("report.txt","w") as f:
        f.write(lines+"\n"+"\n"+num_sum+"\n"+"\n"+cat_sum)

def main():
    while True:
        pathstr=input("Enter the path of the csv file to be analysed:")
        if not os.path.exists(pathstr) or not is_csv(pathstr):
            print('File does not exist or file is not of csv type. Please try again')
        else:
            break
    print("Valid file:",pathstr)

    load_csv_op=load_csv(pathstr)
    if load_csv_op[1]:
        print('File is empty.')
        return
    else:
        df=load_csv_op[0]

    cols=[]
    for col in df.columns.tolist():
        col=clean_column_name(col)
        cols.append(col)
    df.columns=cols

    lines=get_overview(df)
    print("\n")
    print(lines)

    num_sum=numeric_summary(df)
    print("\n")
    print("Numeric data summary:")
    print(num_sum)

    cat_sum=categorical_summary(df)
    print("\n")
    print("Categorical data summary:")
    print(cat_sum)

    save_file(lines,num_sum,cat_sum)



if __name__=='__main__':
    main()

