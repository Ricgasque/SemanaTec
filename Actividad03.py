import pandas as pd

def top_uno():
    archivo = pd.read_csv('netflix_titles.csv')
    for col in archivo.columns:
        print(col)  
    return

def row_number():
    archivo = pd.read_csv('netflix_titles.csv')
    print(len(archivo.index))
    
def released_year():
    year = int(input("Introduzca el año: "))
    archivo = pd.read_csv('netflix_titles.csv')
    print([archivo['release_year'] == year])
        
def country_year():
    pais = input("Introduzca el año: ")
    archivo = pd.read_csv('netflix_titles.csv')
    print([archivo['country'] == pais])
