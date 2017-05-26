import numpy as np
import matplotlib.pyplot as plt

#Felipe Charris Leal
#Tarea 5 Punto2. Este codigo se hizo basado en el cuaderno del repositorio del curso que se encuentra en https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipynb
#cargar los puntos
datos = np.loadtxt("CircuitoRC.txt")
t = datos[:,0]
carga = datos[:,1]

def likelihood(carga, carga_model):
    chi = (1.0/2.0)*(np.sum((carga-carga_model)**2.0))/100000

    return np.exp(-chi)

#se define la duncion de carga tal como lo muestra en el enunciado
def func_carga(t, c, R):
    return c*10*(1-np.exp(-t/R*c))

#acontinuacion se inicializan listas vacias para cada una de las variables 
c_vector = [] 
R_vector = []
vec_l = []


#para estos se deben inicializar con valores aleatorios
c_vector = np.append(c_vector, np.random.random())

R_vector = np.append(R_vector, np.random.random())

#para nuestra ecuacion modeladora se pondran valores iniciales tambien

carga0 = func_carga(t, c_vector[0], R_vector[0])

vec_l = np.append(vec_l, likelihood(carga, carga0))

#print c_vector
#print R_vector
#print vec_l



 #numero de iteraciones a realizar 
iter = 30000 

for i in range(iter):
#basados en las iteraciones se usa la funcion normal para crear una distribucion aleatoria normal 
    c_nuev = np.random.normal(c_vector[i], 0.1) 
    r_nuev = np.random.normal(R_vector[i], 0.1)
#se actualizan los valores 
    carga0 = func_carga(t, c_vector[i], R_vector[i])
    carga_prime = func_carga(t, c_nuev, r_nuev)
#como en el punto 1 usamos el likelihood para ves que tan buenos nos dan los valores probables y por ello se plantean las siquientes condiciones
    #si obtenemos un likelihood bueno o malo vamos a dejar pasar alguos errores aceptables para obtener el mejor
    l_nuev = likelihood(carga, carga_prime)
    l_0 = likelihood(carga, carga0)
    
    alf = (l_nuev/l_0)

    if(alf >=1.0):
        c_vector  = np.append(c_vector,c_nuev)

        R_vector  = np.append(R_vector,r_nuev)

        vec_l = np.append(vec_l, l_nuev)
    else:
        beta = np.random.random()
        if(beta<=alf):
            c_vector = np.append(c_vector,c_nuev)
            R_vector = np.append(R_vector,r_nuev)
            vec_l = np.append(vec_l, l_nuev)
        else:
            c_vector = np.append(c_vector,c_vector[i])

            R_vector = np.append(R_vector,R_vector[i])

            vec_l = np.append(vec_l, l_0)

#se obtienen los mejores valores para cada 
#max_likelihood=np.argmax(vec_l)
#mejor_r=r_nuev[max_likelihood]
#mejor_c=c_nuev[max_likelihood]


#se realizan las graficas
plt.scatter(t,carga, color='LightSeaGreen')

plt.scatter(c_vector,R_vector, color='r')
plt.scatter(c_vector,vec_l)
plt.savefig('carga.jpg')
#plt.show()
plt.close()
histogramax=plt.hist([c_vector,R_vector],label=['C', 'R'],color=['Firebrick',  'chartreuse'] )
plt.legend()
plt.savefig('HistogramaCarga.jpg')
#plt.show()
