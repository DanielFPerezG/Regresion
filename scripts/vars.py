from pandas_datareader import wb
import world_bank_data as wbd
#import pandas as pd

from base.models import Variable, Country


def run():

    Variable.objects.all().delete()
    Country.objects.all().delete()

    df_country = wb.get_countries()    
    df_vars = wbd.get_indicators(source=2)
    df_vars.reset_index(level=0,inplace=True)

    for var in range(len(df_vars)):

        variable = Variable(
            var_id = df_vars.iloc[var]['id'],
            name = df_vars.iloc[var]['name']
        )
        variable.save()
    
    for count in range(len(df_country)):

        country = Country(
            country_id = df_country.iloc[count]['iso2c'],
            name = df_country.iloc[count]['name']
        )
        country.save()
    
if __name__ == '__main__':
    run()