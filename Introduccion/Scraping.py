from bs4 import BeautifulSoup
import requests


# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'



URL = "https://www.minutouno.com/"

# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")
    # <article class="simple-note-square-image
    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('article', {'class': 'simple-note-square-image'})
    #entrada2 = html.find_all('h2.title')
    #entrada3 = html.text
    #entrada4 = html.getText
    #entrada3 = entrada3.replace('\n', " ")
    #print(entrada3)
    # Recorremos todas las entradas para extraer el título, autor y fecha



    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        #titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        ## Sino llamamos al método "getText()" nos devuelve también el HTML
        #autor = entrada.find('a', {'title'})
        #fecha = entrada.find('a').getText()
        print(entrada.text)
        # Imprimo el Título, Autor y Fecha de las entradas
        #print (i + 1, titulo, autor, fecha)

#else:
#    print (status_code)
