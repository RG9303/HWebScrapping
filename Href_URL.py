import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import helpers as hp
from selenium.webdriver.common.by import By


def href(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url)

    href = driver.find_elements(By.CSS_SELECTOR, 'a.href-link.tile-title-text')

    datahref = []
    df = pd.DataFrame([vars(i) for i in datahref])

    for i in href:
        datahref.append(i.get_attribute('href'))
    return datahref
