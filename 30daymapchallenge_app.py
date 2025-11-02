import streamlit as st
if 'Municipio' in df_year.columns:
  hover_cols.append('Municipio')
if 'Departamento' in df_year.columns:
  hover_cols.append('Departamento')


hover_data = {c:True for c in hover_cols}
hover_data['Promedio'] = True


# Crear figura
fig = px.scatter_geo(
df_year,
lat='Latitud',
lon='Longitud',
color='Promedio',
size='Promedio',
hover_name='Estacion' if 'Estacion' in df_year.columns else None,
hover_data=hover_data,
color_continuous_scale=color_scale,
projection='mercator',
scope='south america',
)


fig.update_layout(
template='plotly_dark',
paper_bgcolor='rgb(10,10,15)',
plot_bgcolor='rgb(10,10,15)',
geo=dict(
bgcolor='rgb(10,10,15)',
center=dict(lat=4.5, lon=-74),
projection_scale=6,
showland=True, landcolor='rgb(25,25,25)',
showcountries=True, countrycolor='gray',
showocean=True, oceancolor='rgb(20,25,40)'
),
margin=dict(l=0, r=0, t=40, b=0),
)


# Añadir anotaciones: año grande y escala
fig.add_annotation(
text=str(int(selected_year)), x=0.5, y=0.5, xref='paper', yref='paper',
font=dict(size=80, color='rgba(255,255,255,0.18)'), showarrow=False
)


# Barra de escala (simulada)
fig.add_annotation(text='≈100 km', x=0.12, y=0.08, xref='paper', yref='paper', font=dict(size=12, color='white'), showarrow=False)
fig.add_shape(type='line', x0=0.05, y0=0.07, x1=0.19, y1=0.07, xref='paper', yref='paper', line=dict(color='white', width=3))


# Mostrar en Streamlit
st.plotly_chart(fig, use_container_width=True)


# Información adicional
st.sidebar.markdown("---")
st.sidebar.write(f"Estaciones mostradas: {len(df_year)}")
