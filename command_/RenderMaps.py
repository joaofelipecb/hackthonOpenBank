import pymysql
import pandas as pd
import geopandas as gpd
import subprocess
import os
import matplotlib.pyplot as plt
from pointpats import PointPattern
from pointpats.centrography import mean_center, weighted_mean_center, std_distance
from sklearn.cluster import KMeans
from numpy import random

random.seed(1234);

def inicial():
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    bairros = gpd.read_file("bairros.shp")
    base = bairros.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    base.set_axis_off()
    chart = base.get_figure()
    filepath = os.path.join('mapa1.jpg')
    chart.savefig(filepath, dpi=300)

def carregar_dados_demanda():
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    demanda =gpd.read_file("demanda.shp")
    restaurante = gpd.read_file("restaurante.shp")
    limite = gpd.read_file("bairros.shp")
    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'yellow', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    fig = demanda.plot(column = 'preco_tot', cmap = 'rainbow',ax=base, marker='o', markersize=3, zorder=5)
    fig.set_aspect(1)
    fig.set_axis_off()

    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)

def analise1():
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    limite = gpd.read_file("bairros.shp")
    restaurante = gpd.read_file("restaurante.shp")
    demanda =gpd.read_file("demanda.shp")
    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    abrangencia1 = restaurante.buffer(3000)
    bfr = abrangencia1.plot(ax=base, facecolor = 'none', edgecolor='red')
    bfr.set_aspect(2)
    fig = demanda.plot(column = 'preco_tot', cmap = 'rainbow', ax=base, marker='o', markersize=3, zorder=5)
    fig.set_aspect(1)

    fig.set_axis_off()

    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)
    
def analise2 ():
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    limite = gpd.read_file("bairros.shp")
    restaurante = gpd.read_file("restaurante.shp")
    demanda =gpd.read_file("demanda.shp")
    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    abrangencia1 = restaurante.buffer(3000)
    bfr = abrangencia1.plot(ax=base, facecolor = 'none', edgecolor='red')
    bfr.set_aspect(2)
    
    polygon = abrangencia1.geometry[0]

    demanda_r1 = demanda[demanda.within(polygon)]

    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    bfr = abrangencia1.plot(ax=base, facecolor = 'none', edgecolor='red')
    brf.set_aspect(1)
    fig = demanda_r1.plot(column = 'preco_tot', cmap = 'rainbow', ax=base, marker='o', markersize=3, zorder=5)
    fig.set_aspect(1)
    fig.set_axis_off()
    
    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)
          
        
def analise3 ():
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    limite = gpd.read_file("bairros.shp")
    restaurante = gpd.read_file("restaurante.shp")
    demanda =gpd.read_file("demanda.shp")
    
    abrangencia1 = restaurante.buffer(3000)
    polygon = abrangencia1.geometry[0]
    demanda_r2 = demanda[demanda.disjoint(polygon)]

    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    bfr = abrangencia1.plot(ax=base, facecolor = 'none', edgecolor='red')
    bfr.set_aspect(1)
    fig = demanda_r2.plot(column = 'preco_tot', cmap = 'rainbow', ax=base, marker='o', markersize=3, zorder=5)
    fig.set_aspect(1)

    fig.set_axis_off()

    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)

    demanda_r2.reset_index(inplace=True, drop=True) 

def analise4 ():
    

    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    limite = gpd.read_file("bairros.shp")
    restaurante = gpd.read_file("restaurante.shp")
    demanda =gpd.read_file("demanda.shp")
    
    abrangencia1 = restaurante.buffer(3000)
    polygon = abrangencia1.geometry[0]    
    demanda_r2 = demanda[demanda.disjoint(polygon)]

    demanda_r2_geo = gpd.GeoDataFrame(demanda_r2)
    demanda_r2.reset_index(inplace=True, drop=True) 


    demanda_r2_geo['longitude'] = demanda_r2.centroid.map(lambda p: p.x)
    demanda_r2_geo['latitude'] = demanda_r2.centroid.map(lambda p: p.y)

    demanda_r2_geo = demanda_r2_geo[['longitude', 'latitude']]

    kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10)
    pred_y = kmeans.fit_predict(demanda_r2_geo)

    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    demanda_r2_geo.plot.scatter(x='longitude', y='latitude', cmap = 'rainbow', c = pred_y, ax=base, colorbar =None,zorder=5)
    
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=70, c='black', zorder=15)

    base.set_axis_off()

    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)



def analise5 ():

    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    limite = gpd.read_file("bairros.shp")
    restaurante = gpd.read_file("restaurante.shp")
    demanda =gpd.read_file("demanda.shp")
      
    abrangencia1 = restaurante.buffer(3000)
    polygon = abrangencia1.geometry[0]
    demanda_r2 = demanda[demanda.disjoint(polygon)]
    
    demanda_r2.reset_index(inplace=True, drop=True) 

    demanda_r2_geo = gpd.GeoDataFrame(demanda_r2)


    demanda_r2_geo['longitude'] = demanda_r2.centroid.map(lambda p: p.x)
    demanda_r2_geo['latitude'] = demanda_r2.centroid.map(lambda p: p.y)

    demanda_r2_geo = demanda_r2_geo[['longitude', 'latitude']]
    
    kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10)
    pred_y = kmeans.fit_predict(demanda_r2_geo)
    demanda_r2['pred'] = pred_y

    demanda_r2_up = demanda_r2.query('pred == [0, 1, 3]')
    demanda_r2_up.reset_index(inplace=True, drop=True) 
    
    #Ponto médio geográfico da demanda excedente ponderado pelo preco total
    colunas_selecionadas = ['longitude','latitude']
    points = pd.DataFrame(demanda_r2_up.filter(items=colunas_selecionadas))
    points[['longitude', 'latitude']].to_numpy()

    #centrografia
    pp = PointPattern(points)

    #Media 
    media = mean_center(pp.points)

    #media ponderada
    pesos_a = ['preco_tot']
    pesos = pd.DataFrame(demanda_r2_up.filter(items=pesos_a))

    mediapond = weighted_mean_center(pp.points, pesos)

    #Standard Distance
    stdd = std_distance(pp.points)
    
    #Plot

    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=75, zorder=10)
    restaurante1.set_aspect(1)
    fig = demanda_r2.plot(ax=base, marker = 'o', color = 'grey', markersize=10, zorder=8)
    fig.set_aspect(1)

    circle1 = plt.Circle((media[0], media[1]),stdd,fill=False, color='c', label='1', zorder=10)
    circle2 = plt.Circle((mediapond[0], mediapond[1]),stdd,fill=False, color='b', label='2', zorder=10)

    plt.plot(media[0], media[1], 'c^', label='Médio', zorder=10)
    plt.plot(mediapond[0], mediapond[1], 'b^', label='Médio Ponderado', zorder=10)

    plt.gcf().gca().add_artist(circle1)
    plt.gcf().gca().add_artist(circle2)

    plt.suptitle('Centrografia - Círculo', fontsize=16)

    plt.legend(loc='best', title='Centro', numpoints=1, facecolor='white', edgecolor='black')

    #Plot do local ideal para o novo empreendimento
    base = limite.plot(color='white', edgecolor='black')
    base.set_aspect(1)
    restaurante1 = restaurante.plot(ax=base, marker = '*', color = 'red', markersize=180, label = 'Empreendimento existente',zorder=10)
    restaurante1.set_aspect(1)

    restaurante2 = plt.plot(mediapond[0], mediapond[1], '*',  color = 'green', label = 'Novo empreendimento',markersize=15,zorder=10)

    fig = demanda.plot(color='grey', ax=base, marker='o', markersize=2, zorder=5)
    fig.set_aspect(1)

    fig.set_axis_off()

    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)



def analise6 ():
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" fishnet_clip.shp MYSQL:"openbanking,host=localhost,user=root,password=" "fishnet_clip"'
    subprocess.check_call(command, shell=True)
    potencial_consumo = gpd.read_file("fishnet_clip.shp") 
    lista_anos = ['2000', '2005', '2010', '2015', '2020']

    for i in lista_anos:
      fig = potencial_consumo.plot(column=('pcon_')+i, cmap='rainbow', legend='True')
      fig.set_aspect(1)
      fig.set_axis_off()

      filepath = os.path.join('PotConsumo_'+i+'.jpg')
      chart = fig.get_figure()
      chart.savefig(filepath, dpi=300)
      
    filepath = os.path.join('mapa1.jpg')
    chart = fig.get_figure()
    chart.savefig(filepath, dpi=300)

def analise7 ():
    #Determinar o crescimento e/ou diminuição do potencial de consumo ao longo dos anos
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" fishnet_clip.shp MYSQL:"openbanking,host=localhost,user=root,password=" "fishnet_clip"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" bairros.shp MYSQL:"openbanking,host=localhost,user=root,password=" "bairros"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" demanda.shp MYSQL:"openbanking,host=localhost,user=root,password=" "demanda"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile" restaurante.shp MYSQL:"openbanking,host=localhost,user=root,password=" "restaurante"'
    subprocess.check_call(command, shell=True)
    limite = gpd.read_file("bairros.shp")
    restaurante = gpd.read_file("restaurante.shp")
    demanda =gpd.read_file("demanda.shp")
      
    abrangencia1 = restaurante.buffer(3000)
    polygon = abrangencia1.geometry[0]
    demanda_r2 = demanda[demanda.disjoint(polygon)]
    
    demanda_r2.reset_index(inplace=True, drop=True) 

    demanda_r2_geo = gpd.GeoDataFrame(demanda_r2)


    demanda_r2_geo['longitude'] = demanda_r2.centroid.map(lambda p: p.x)
    demanda_r2_geo['latitude'] = demanda_r2.centroid.map(lambda p: p.y)

    demanda_r2_geo = demanda_r2_geo[['longitude', 'latitude']]
    
    kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10)
    pred_y = kmeans.fit_predict(demanda_r2_geo)
    demanda_r2['pred'] = pred_y

    demanda_r2_up = demanda_r2.query('pred == [0, 1, 3]')
    demanda_r2_up.reset_index(inplace=True, drop=True) 
    
    #Ponto médio geográfico da demanda excedente ponderado pelo preco total
    colunas_selecionadas = ['longitude','latitude']
    points = pd.DataFrame(demanda_r2_up.filter(items=colunas_selecionadas))
    points[['longitude', 'latitude']].to_numpy()

    #centrografia
    pp = PointPattern(points)

    #Media 
    media = mean_center(pp.points)

    #media ponderada
    pesos_a = ['preco_tot']
    pesos = pd.DataFrame(demanda_r2_up.filter(items=pesos_a))

    mediapond = weighted_mean_center(pp.points, pesos)

    #Standard Distance
    stdd = std_distance(pp.points)
    
    potencial_consumo = gpd.read_file("fishnet_clip.shp") 
    
    potencial_consumo['cresc_1'] = potencial_consumo['pcon_2005'] - potencial_consumo['pcon_2000']
    potencial_consumo['cresc_2'] = potencial_consumo['pcon_2010'] - potencial_consumo['pcon_2005']
    potencial_consumo['cresc_3'] = potencial_consumo['pcon_2015'] - potencial_consumo['pcon_2010']
    potencial_consumo['cresc_4'] = potencial_consumo['pcon_2020'] - potencial_consumo['pcon_2015']
    
    potencial_consumo_crescimento = potencial_consumo[(potencial_consumo.cresc_1 >= 0) & (potencial_consumo.cresc_2 >= 0) & (potencial_consumo.cresc_3 >= 0) & (potencial_consumo.cresc_4 >= 0)]
    base1 = potencial_consumo.plot(color='None')
    base1.set_aspect(1)
    base = limite.plot(ax = base1, color='white', edgecolor='black')
    base.set_aspect(1)
    pc = potencial_consumo_crescimento.plot(ax=base1, color='lime')
    pc.set_aspect(1)
    restaurante2 = plt.plot(mediapond[0], mediapond[1], '*',  color = 'green', label = 'Novo empreendimento',markersize=15,zorder=10)
    

    base1.set_axis_off()

    filepath = os.path.join('mapa1.jpg')
    chart = base.get_figure()
    chart.savefig(filepath, dpi=300)
analise7()
