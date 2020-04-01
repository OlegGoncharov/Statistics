import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_excel(r'C:\Users\CAM350\Desktop\Statistics\table.xlsx', na_values=[],keep_default_na = False,index_col=0)
x = data.index
tk = [12.7060, 4.3020, 3.182, 2.776, 2.570, 2.4460, 2.3646,\
      2.3060, 2.2622, 2.2281, 2.201, 2.1788, 2.1604, 2.1448]
x_lower = np.mean(x)-tk[len(x)-1]*np.std(x)/(len(x)**0.5)
x_upper = np.mean(x)+tk[len(x)-1]*np.std(x)/(len(x)**0.5)
mean_value = np.mean(x);
print(f'Среднее = {mean_value:.2f}')
print(f'Нижняя граница = {x_lower:.2f}')
print(f'Верхняя граница = {x_upper:.2f}')
