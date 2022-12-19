

from base.models import VarModel, Variable
from pandas_datareader import wb

import pandas as pd



def run():

    a = pd.DataFrame(list(VarModel.objects.all().values()))

if __name__ == '__main__':
    run()