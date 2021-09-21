import pandas as pd
import matplotlib.pyplot as plt

gdp = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")


gdpsub = gdp[['Country Name', 'GDP per capita (constant 2010 US$)',
              'Mortality rate, infant (per 1,000 live births)']]
print(gdpsub)

gdpsub.plot.scatter(x='GDP per capita (constant 2010 US$)',
                    y='Mortality rate, infant (per 1,000 live births)')

plt.show()