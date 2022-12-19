

from base.models import VarModel, Variable
from pandas_datareader import wb

import pandas as pd



def run():

    a = pd.DataFrame(list(VarModel.objects.all().values()))
    df_country = wb.get_countries()    
    
    print(df_country.head())

if __name__ == '__main__':
    run()