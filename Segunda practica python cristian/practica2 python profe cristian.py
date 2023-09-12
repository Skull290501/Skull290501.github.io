import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv")

prom = df['gross'].mean() #con esto se calcula el promedio de gross

df['gross'].fillna(prom, inplace=True)#llenando nulo con promedio de gross

df['facenumber_in_poster'].fillna(0, inplace=True)#llenar valores nulos de la columna facenumber_in_poster con 0

df.loc[df['facenumber_in_poster'] < 0, 'facenumber_in_poster'] = 0 #rellenar los valores negativos de la columna con 0 

df['TitleCode'] = df['movie_imdb_link'].str.extract('(/title/(tt\d+))').iloc[:, 1]#obtiene el valor de la columna title code

df['title_year'].fillna(0, inplace=True)#llenar valores nulos de la columna title_year con 0

jsjs = df[df['country'] == 'USA']#seleccionar solo usa

jsjs.to_csv("C:/Users/yeyos/OneDrive/Documentos/FilmTV_USAMovies.csv", index=False)

print("Datos importados")





