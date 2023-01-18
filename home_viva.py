import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import helpers as hp

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


def DetailHome(url):

    class vivanuncios(object):
        precio = 0
        propiedad = ''
        tipo = ''
        visualizaciones = 0
        metros_total = 0
        metros_construido = 0
        banos = 0
        medio_banos = 0
        estacionamientos = 0
        recamaras = 0
        antiguedad = 0
        tiempo_de_publicacion = ''
        status_desarrollo = ''

    datos_de_viviendas = []

    driver.get(url)

    soup = bs(driver.page_source, 'html.parser')
    article_container = soup.find('div', id='wrapper')
    #title_container = article_container.find('div', class_='title title-urgent-ad')
    #user_views_container = article_container.find('span', id='view-count')

    # Data
    datos = vivanuncios()

    # Price
    price_element = article_container.find('span', class_='ad-price')
    #article_container.find('div', class_='price').find('span', class_='ad-price')
    #print(price_element)

    if price_element:
      datos.precio = hp.get_number_from_string(price_element.text)

    # Title
    title_element = article_container.find('div', class_='title')
    #print(title_element)

    if title_element:
      datos.propiedad = title_element.text.strip()

    # Views
    views_element = article_container.find('span', class_='view-count') #user_views_container.find('span').find_all('div')[-1]
    #print(views_element)

    if views_element:
      datos.visualizaciones = hp.get_number_from_string(views_element.text)

    # M2 total
    feature_elements = article_container.find('span', class_='pri-props-value') #title_container.find('div', class_='category-inner-container').find_all('span', class_='pri-props-value')
    #print(feature_elements)

    if feature_elements:
      datos.metros_total = hp.get_number_from_string(feature_elements.text)

    # Published date
    date_element = article_container.find('span', class_='creation-date')

    if date_element:
      datos.tiempo_de_publicacion = date_element.text.strip()

    datos_de_viviendas.append(datos)

    #df = pd.DataFrame([vars(vivienda) for vivienda in datos_de_viviendas])
    #print(df)

    return datos_de_viviendas

    #df.to_csv("Vivanuncios.csv", index=False)