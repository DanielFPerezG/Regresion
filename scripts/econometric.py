

from base.models import VarModel, Variable
from pandas_datareader import wb

import pandas as pd



def run():

    a = pd.DataFrame(VarModel.objects.all().values())
    b = VarModel.objects.all()

    ind = a['variable'].to_string(index=False)
    print(a['variable'].to_string(index=False))
    
    # df_model = wb.download(
    # indicator = {a['variable'].to_string(index=False)},
    # country = a['country'].to_string(index=False),
    # start = int(a['initial_date'].to_string(index=False)),
    # end = int(a['initial_date'].to_string(index=False))
    # )
    
    # print(df_model)

if __name__ == '__main__':
    run()