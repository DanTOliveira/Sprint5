import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header('Dashboard de Veículos')


if st.checkbox('Criar histograma'):
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer", title='Quantidade de veículos vendidos acordo com a Quilometragem do Veículo')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Criar gráfico de dispersão'):
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price", title='Preço de acordo com a Quilometragem do Veículo')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    
if st.checkbox('Criar gráfico de barras'):

     # escrever uma mensagem
    st.write('Criando um gráfico de barras para o conjunto de dados de anúncios de vendas de carros ')

    # Criar um gráfico de barras
    fig = px.bar(car_data, x='condition', y='price', title='Preço Médio por Condição do Veículo')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)