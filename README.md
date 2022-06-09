# CORPORATE MASTER IN APPLIED DATA SCIENCE
# TEXT MINING & NATURAL LANGUAGE PROCESSING
# TAREA1 - Scrapping de texto clasificado

**********************************************
*** PUNTO 1 - INSTALAR Y CORRER CÓDIGO *******
**********************************************

# TOMANDO EN CUENTA QUE SE TIENE ANACONDA O CONDA INSTALADO
# SI SE TIENE INSTALADO CON EL PATH INCLUIDO EN EL PATH DE WINDOWS SE PUEDE DESDE CMD
# SI EL PATH NO FUE INCLUIDO, ENTONCES ABRIR UNA CONSOLA DESDE LA INSTALACION DE CONDA/ANACONDA

# PRIMERO CREAR VIRTUAL ENV

	conda create -n wiki_tarea
	
	# Se genera directorio
	 ../wiki_tarea

# ACTIVAR V ENV

	conda activate wiki_tarea

# INSTALAR SCRAPY y BEAUTIFULSOUP

	conda install scrapy -c conda-forge
	conda install beautifulsoup4
	conda install lxml

# CREAR PROYECTO

	scrapy startproject wiki_tarea

	# Se genera directorio
	 ../wiki_tarea/wiki_tarea

# INGRESAR AL DIRECTORIO DEL PROYECTO DE SCRAPY

	cd wiki_tarea/wiki_tarea

# CREAR CRAWLER

	scrapy genspider article host_base

	# Se genera crawler en directorio 
	../wiki_tarea/spiders/article.py

# SUSTITUIR LOS SIGUIENTES ARCHIVOS DEL PROYECTO DE SCRAPY
# Sustituir por los archivos de nuestro GIT (mismo directorio)

	../wiki_tarea/items.py
	../wiki_tarea/spiders/article.py

# EJECTURAR EL SCRAPPING

	scrapy crawl article -o tarea1.json

# VISUALIZAR OUTPUT (desde directorio general de venv)

	../wiki_tarea/tarea1.json

**********************************************
*** PUNTO 2 - FORMATO Y ESTRUCTURA ***********
**********************************************

Como se observó anteriormente, el output es un archivo .JSON

El mismo contiene la siguiente estructura:

[{"link": "https://en.wikipedia.org/wiki/7_World_Trade_Center", 
  "body": { "title": "7 World Trade Center", 
	     "paragraph": ["7 World Trade Center - Wikipedia ....."]
	  }
}]

**********************************************
*** PUNTO 3 - DESCRIPCIÓN Y CONTENIDO ********
**********************************************

Para este scrapping, se ha utilizado el sitio wikipedia.org

Dentro del mismo, se ha elegido revisar cada uno de los "featured_articles" de la misma página,

Los fragmentos de texto representan la descripción de wikipedia para cada uno de estos "featured_articles"

El texto está clasificado por una categoría general, que forma el cuerpo del artículo

**********************************************
*** PUNTO 4 - CONTRIBUCIONES *****************
**********************************************

Se trabaja en conjunto para realizar la tarea

**********************************************
*** PUNTO 5 - INFORMACION ADICIONAL **********
**********************************************

Dado que existe una gran cantidad de "featured_articles" y para evitar mucho esfuerzo y tiempo de procesamiento, se ha colocado un contador que limita la cantidad de artículos a "scrapear"

Esta modificación puede verse desde el directorio:

	../wiki_tarea/wiki_tarea/spiders/article.py

Y modificando la linea #19 (i.e.):

17      for link in response.css('.featured_article_metadata > a'):
18          # CANTIDAD DE ARTICULOS A REVISAR
19          if counter >= 1:
20              break
