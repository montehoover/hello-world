# Hello Parse

For parsing anything simply do:
```python
with open("myfile.txt") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            print(word)
```

For parsing yaml use the yaml module (pip install pyyaml):
```python
import yaml
with open("myfile.yml") as f:
    d = yaml.safe_load(f)
    print(d["expected_entry"])
    for item in d["expected_list"]:
        print(item)
```

For parsing cvs, use [Pandas](hello-ml/hello_numpy_pandas.ipynb):
```python
import pandas as pd
df = pd.read_csv("myfile.csv"):
# Print the first row:
print(df.iloc[0])
# Print one of the columns:
print(df.loc[:, ["some_column"]])
# Another way to print columns:
for row in df.itertuples():
    print(row.some_column, row.some_other column)
```

Try it with
```
python parse_yaml.py
```

or

```
python parse.csv.py
```