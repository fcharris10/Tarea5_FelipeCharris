import numpy as np
import matplotlib.pyplot as plt
#Felipe Charris Leal
#201318114
#Punto1. Canales ionicos





#Importamos los datos producidos por c donde tenemos x,y,r para buscar el maximo de cada parametro y graficarlo 
# se van a realizaar dos graficas por paquete de datos a cada una leyendo desde la mitad del archivo txt generado en c
cirmax=np.genfromtxt("felipe.txt",skip_footer=1500)
max_x=cirmax[:,0]
max_y=cirmax[:,1]
max_r=cirmax[:,2]

#importamos los datos de las moleculas para graficarlas en xy
datos=np.loadtxt("Canal_ionico1.txt")
molecx=datos[:,0]
molecy=datos[:,1]
#contadores para buscar
ubica=0

radio_maxi=0


#se va a recorrer en maxr de los obtenidos en c para buscarlo en la ubicacion
for i in range(len(max_r)):
	if (max_r[i]>radio_maxi):
		radio_maxi=max_r[i]
		ubica=i
print max_r[i]
print max_x[i]
print max_y[i]
#moleculas de color negro
fig, ax=plt.subplots()

circle1=plt.Circle((max_x[ubica],max_y[ubica]),max_r[ubica], color='g',fill=False)
ax.add_artist(circle1)
ax.set_aspect('equal','datalim')
plt.scatter(molecx,molecy, color='black')
#plt.text(x = 1, y = 0.0, s = u'T = 0.05', fontsize = 24)
ax.annotate('Parametros: x=0.657586,y=5.236146, r=4.440524', xy=(0.657586,5.236146), xytext=(2,2),arrowprops=dict(facecolor='black', shrink=1),horizontalalignment='left',
            verticalalignment='bottom',)
plt.savefig('c1.jpg')
plt.show()

histogramax=plt.hist([max_x,max_y],label=['Coordenadas en X', 'Coordenadas en Y'],color=['crimson',  'chartreuse'] )
#'burlywood',
plt.legend()
#histogramay=plt.hist(max_y)
plt.savefig('histo1.jpg')
plt.show()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#Importamos los datos producidos por c donde tenemos x,y,r para buscar el maximo de cada parametro y graficarlo 
cirmax=np.genfromtxt("felipe.txt",skip_header=1500)
max_x=cirmax[:,0]
max_y=cirmax[:,1]
max_r=cirmax[:,2]

#importamos los datos de las moleculas para graficarlas en xy
datos=np.loadtxt("Canal_ionico1.txt")
molecx=datos[:,0]
molecy=datos[:,1]
#contadores para buscar
ubica=0

radio_maxi=0


#se va a recorrer en maxr de los obtenidos en c para buscarlo en la ubicacion
for i in range(len(max_r)):
	if (max_r[i]>radio_maxi):
		radio_maxi=max_r[i]
		ubica=i
print max_r[i]
print max_x[i]
print max_y[i]
#moleculas de color negro
fig, ax=plt.subplots()

circle1=plt.Circle((max_x[ubica],max_y[ubica]),max_r[ubica], color='g',fill=False)
ax.add_artist(circle1)
ax.set_aspect('equal','datalim')
plt.scatter(molecx,molecy, color='black')
#plt.text(x = 1, y = 0.0, s = u'T = 0.05', fontsize = 24)
ax.annotate('Parametros: x=0.657586,y=5.236146, r=4.440524', xy=(5.80329,8.013071), xytext=(2,2),arrowprops=dict(facecolor='black', shrink=1),horizontalalignment='left',
            verticalalignment='bottom',)
plt.savefig('c2.jpg')
plt.show()

histogramax=plt.hist([max_x,max_y],label=['Coordenadas en X', 'Coordenadas en Y'],color=['crimson',  'chartreuse'] )
#'burlywood',
plt.legend()
#histogramay=plt.hist(max_y)
plt.savefig('histo2.jpg')
plt.show()


