import numpy as np
from bokeh.plotting import figure, output_file, show

x = np.random.rand(100)
y = np.random.rand(100)

output_file("ejemplo.html")

p = figure(title="Gráfico de Dispersión", x_axis_label='X', y_axis_label='Y')

p.circle(x, y, size=5, color="navy", alpha=0.5)

show(p)

