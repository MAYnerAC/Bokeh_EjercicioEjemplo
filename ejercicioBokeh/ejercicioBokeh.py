import pandas as pd
import random
from bokeh.plotting import figure, output_file, save
from bokeh.palettes import Turbo256

# Cargar los datos desde el archivo CSV
df = pd.read_csv("co2_pcap_cons.csv")

# Eliminar filas con valores NaN
df = df.dropna()

# Obtener lista de países únicos
paises = df['country'].unique()

# Crear una lista de años de 1800 a 2023
años = [str(i) for i in range(1800, 2024)]

# Asignar colores aleatorios a cada país
colores = random.sample(Turbo256, len(paises))

# Crear un diccionario de colores para asignar un color único a cada país
dict_colores = dict(zip(paises, colores))

# Crear una figura de Bokeh
p = figure(title="Emisiones de CO2 per cápita por país (1800-2023)", x_axis_label="Año", y_axis_label="CO2 emissions per capita")

# Iterar sobre cada país en los datos
for pais in paises:
    try:
        # Obtener datos de emisiones de CO2 para el país y alinear longitud de datos
        datos_pais = df[df['country'] == pais].iloc[:, 1:].values.flatten()
        datos_pais = list(datos_pais) + [None] * (len(años) - len(datos_pais))
        
        # Trazar línea para el país
        p.line(x=años, y=datos_pais, line_color=dict_colores[pais], legend_label=pais)
    except KeyError:
        print(f"No se encontró el color para el país: {pais}")

# Ajustar la leyenda y el tamaño del gráfico
p.legend.location = "top_left"
p.legend.click_policy = "hide"
p.sizing_mode = "stretch_width"

# Guardar la visualización en un archivo HTML
output_file("emisiones_CO2_per_capita.html")
save(p)