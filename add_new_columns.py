
import pandas as pd
import click

@click.command()
@click.argument('files', nargs=-1)

def add_new_columns(files):
    for file in files:
        df = pd.read_csv(file)
        df["column1"] = ""
        df["column2"] = ""
        df["column3"] = ""
        df["column4"] = ""
        df["column5"] = ""
        df["column6"] = ""
        df.to_csv(file, index=False)

if __name__=="__main__":
    add_new_columns()
