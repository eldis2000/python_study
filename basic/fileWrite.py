import pandas as pd

number = [1,2,3]
name = ["hong","kim","choi"]

data  = pd.DataFrame()
data['number'] = number
data['name'] = name

data.write_xls()


