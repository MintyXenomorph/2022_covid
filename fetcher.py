import pandas as pd
import datetime as datetime
from datetime import datetime as dt
import os
today=dt.today()

def fetch():
    if os.path.exists(f"world_{today.strftime('%b-%d-%Y')}.csv"):
        print(f"File ~ world_{today.strftime('%b-%d-%Y')}.csv ~ Already Exists")
    else:
        print("COVID FILE does NOT EXIST. \nCreating...\n..............\n..............\n..............")
        data_path='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
        df = pd.read_csv(data_path,index_col='date', parse_dates=True)
        df.to_csv(f"world_{today.strftime('%b-%d-%Y')}.csv")
        print(f"CREATED: world_{today.strftime('%b-%d-%Y')}.csv")



