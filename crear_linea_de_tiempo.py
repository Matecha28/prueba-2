import plotly.express as px
import pandas as pd

# Datos para la línea de tiempo
data = {
    "Tarea": [
        "Investigación y Concienciación",
        "Publicación de Resultados",
        "Proyecto con la Cooperación Española",
        "Desarrollo de la Propuesta de Ley",
        "Testimonios en el Congreso",
        "Debate y Votación",
        "Programas de Educación y Sensibilización"
    ],
    "Inicio": [
        "2018-01-01", "2019-01-01", "2020-01-01", "2021-01-01", "2022-01-01", "2023-11-02", "2024-01-01"
    ],
    "Fin": [
        "2018-12-31", "2019-12-31", "2020-12-31", "2021-12-31", "2022-12-31", "2023-11-02", "2024-12-31"
    ],
    "Descripción": [
        "Estudio inicial de Plan Internacional, UNFPA y Universidad Peruana Cayetano Heredia",
        "Mapear la prevalencia y comprender las dinámicas del matrimonio infantil",
        "Fortalecimiento de la incidencia política",
        "Asistencia técnica al Congreso",
        "Lideresas indígenas y afroperuanas compartieron sus testimonios",
        "Aprobación de la ley que prohíbe el matrimonio infantil sin excepciones",
        "Implementación efectiva de la ley y monitoreo"
    ],
    "Imagen": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
        "https://example.com/image4.jpg",
        "https://example.com/image5.jpg",
        "https://example.com/image6.jpg",
        "https://example.com/image7.jpg"
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Convertir las columnas de fechas a datetime
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])

# Crear la línea de tiempo interactiva como un gráfico de Gantt
fig = px.timeline(df, x_start="Inicio", x_end="Fin", y="Tarea", text="Descripción", title="Línea de Tiempo Interactiva: Proceso para la Aprobación de la Ley Contra el Matrimonio Infantil en Perú")

# Mejorar la interactividad y estética
fig.update_traces(marker_color="blue", opacity=0.6)
fig.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Tarea",
    showlegend=False,
    hovermode="x unified",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(color="black"),
    title_font=dict(size=24, color='darkblue', family="Arial"),
    xaxis=dict(
        showline=True,
        showgrid=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        gridcolor='rgb(230, 230, 230)',
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        gridcolor='rgb(230, 230, 230)'
    )
)

# Añadir descripciones en hover
fig.update_traces(textposition='inside', insidetextanchor='middle')

# Añadir imágenes como anotaciones
for i, row in df.iterrows():
    fig.add_layout_image(
        dict(
            source=row["Imagen"],
            x=row["Inicio"].timestamp() * 1000,  # Convertir datetime a milisegundos
            y=i,  # Usar el índice para la posición y
            xref="x",
            yref="y",
            sizex=60*24*60*60*1000,  # Ajustar el tamaño de la imagen (en milisegundos)
            sizey=0.5,  # Ajustar el tamaño de la imagen
            xanchor="center",
            yanchor="middle"
        )
    )

# Guardar la figura como un archivo HTML
fig.write_html("linea_de_tiempo_interactiva.html")

# Mostrar la figura
fig.show(renderer="browser")


