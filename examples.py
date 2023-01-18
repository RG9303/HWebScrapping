import glob
from Href_URL import href
import seaborn
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import helpers as hp
from selenium.webdriver.common.by import By
from home_viva import DetailHome
from selenium.webdriver.chrome.service import Service


url_list = [f'https://www.vivanuncios.com.mx/s-casas-en-venta/pachuca-de-soto/page-{i}/v1c1293l10488p{i}' for i in range(1, 3)] #50

#url_list = [f'https://www.vivanuncios.com.mx/s-casas-en-venta/tulum/page-{i}/v1c1293l14909p{i}' for i in range(1,3)]

dataref = []
datahome = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

for j in url_list:
    driver.get(j)
    dataref.append(href(j))

df = pd.DataFrame(dataref)

print(df)

dfh = []
dfv = []
result = []
n = list(range(1, df.shape[0] * df.shape[1]))
namecsv = [f'Vivanuncios{i}.csv' for i in n] #50

set_dataf = {}
for s in range(df.shape[0]):
    for r in range(df.shape[1]):
        datahome = DetailHome(df.iloc[s, r])
        dfv = [vars(vivienda) for vivienda in datahome]
        dfh = pd.DataFrame(dfv)
        filename = 'Vivanuncios' + str(r) + '.csv'
        dfh.to_csv(filename, index=False)

csv_files = glob.glob('*.{}'.format('csv'))
df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)
print(df_concat)

df_concat.to_csv("VivanunciosTotal.csv", index=False)
