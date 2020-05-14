
import pandas as pd
import click

@click.command()
@click.argument('files', nargs=-1)


def add_new_columns(files):
    
    new_columns = ["column1", "column2", "column3", "column4", "column5", "column6"]
    
    for file in files:
        df = pd.read_csv(file)
        for column in new_columns:
            df[column] = ""

       #df.rename({'old_column1':'new_column1','old_column2':'new_column2'},axis=1) #this is used to rename columns
        df.to_csv(file, index=False)

if __name__=="__main__":
    add_new_columns()
