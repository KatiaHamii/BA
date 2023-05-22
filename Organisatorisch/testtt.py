import pandas as pd

# Read the CSV file
df = pd.read_csv('SemanticshesNetsNaturkatastrophen.csv')

# Divide the data by rows
row_chunks = [df[i:i+10] for i in range(0, len(df), 10)]

# Divide the data by columns
column_chunks = [df.iloc[:, i:i+5] for i in range(0, len(df.columns), 5)]

# Process the divided data (example: print each row chunk)
for chunk in row_chunks:
    print(chunk)

# Process the divided data (example: print each column chunk)
for chunk in column_chunks:
    print(chunk)
