

from base.models import VarModel, Variable
from pandas_datareader import wb

import pandas as pd



def run():

    a = pd.DataFrame(list(VarModel.objects.all().values()))
    
    df_model = wb.download(
    indicator = ast.literal_eval(a['variable'].to_string(index=False)),
    country = ast.literal_eval(a['country'].to_string(index=False)),
    start = int(a['initial_date'].to_string(index=False)),
    end = int(a['initial_date'].to_string(index=False))
    )
    
    print(df_model)

if __name__ == '__main__':
    run()