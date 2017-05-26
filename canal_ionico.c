#include <stdlib.h>
#include <stdio.h>
#include <math.h>

//Los metodos a usar se definen antes de la funcion principal que sera la distancia que esta separado al centro y el radio minimo

//si quieremos saber el radio minimo calculando cuanta distancia hay entre una molecula cualquiera y el c
double radiom(double yant,double xant, double *x, double *y, int dat);


//si quiero encontrar la separacion entre dos puntos para nuestra separacion del centro
double CentroSeparacion(double yant,double xant, double x1, double y1);

int main(void){

//declaro donde voy a guardar en la memoria
	FILE *num;
	FILE *num2;

//definimos las variables actuales o anteriores inicializadas en 0
	
double xant=0;
double yant=0;

//al actualizar debemos tener un xfuturo y un yfuturo
double xfut; 
double yfut; 
//para llegar a nuestro radio optimo debemos dejar pasar algunos menores en esa busqueda por ello creamos esta variable 
	double error; 

	
//los puntos de las moleculas
	double *x;
	double *y;
//una "posicion"	
int i;
//al igual que para x  para el radio tambien se debe inicializar las variables para el metodo con un ranterior y un rfuturo
double rfut; 
double rant;

//numero de moleculas o datos se tomaran con la variable dat	
	int dat=42; 
//definimos el numero de iteraciones que realizara
int numit=1500; 	
	
	double paso=0.4; //paso
	
	double likelihood;
	
	x=malloc(84*sizeof(double));
	y=malloc(84*sizeof(double));
	
	num=fopen("Canal_ionico.txt","r");
	for(i=0;i<dat;i++){
		fscanf(num,"%lf %lf \n",&x[i],&y[i]);
	//printf("%lf %lf\dat", x[i],y[i]);
	}
	rant=radiom(xant,yant,x,y,dat);
	for(i=0; i<numit;i++){
		
		xfut=xant+(drand48()*2.0*paso)-paso;
		yfut=yant+(drand48()*2.0*paso)-paso;
		rfut=radiom(xfut, yfut,x,y, dat); //calcula el nuevo r
		likelihood=rfut/rant;
		if (likelihood>1.0){
			xant=xfut;
			
			yant=yfut;
			rant=rfut;
		}
		
		else{
// se deben aceotar algunos errores pasando por radios pequeños antes del optimo 
// https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipynb
			error=drand48();
			if(error<likelihood){
				xant=xfut;
				yant=yfut;
				rant=rfut;
			}
		}
	printf("%lf %lf %lf\n", xant,yant,rant);	
	}
// se repite el procedimiento con el siguiente paquete de datos para imprimir un archivo txt con las iteraciones de los dos 
	numit=1500; 	
	
	paso=0.5; //cambiar paso
	

	num=fopen("Canal_ionico1.txt","r");
	for(i=0;i<dat;i++){
		fscanf(num,"%lf %lf \n",&x[i],&y[i]);
	//printf("%lf %lf\dat", x[i],y[i]);
	}
	rant=radiom(xant,yant,x,y,dat);
	for(i=0; i<numit;i++){
		
		xfut=xant+(drand48()*2.0*paso)-paso;
		yfut=yant+(drand48()*2.0*paso)-paso;
		rfut=radiom(xfut, yfut,x,y, dat); //calcula el nuevo r
		likelihood=rfut/rant;
		if (likelihood>1.0){
			xant=xfut;
			
			yant=yfut;
			rant=rfut;
		}
		
		else{
// se deben aceotar algunos errores pasando por radios pequeños antes del optimo 
// https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/14.MonteCarloMethods/bayes_MCMC.ipynb
			error=drand48();
			if(error<likelihood){
				xant=xfut;
				yant=yfut;
				rant=rfut;
			}
		}
	printf("%lf %lf %lf\n", xant,yant,rant);	
	}
	
	
}



double CentroSeparacion(double xant,double yant, double x1, double y1){

	double cuadrados=(pow(xant-x1,2))+(pow(yant-y1,2));
	

return pow(cuadrados,0.5);
}
//radio otptimo en el cual exista un centro maximo que no llegue a tocar las demas moleculas 
double radiom(double xant,double yant, double *x, double *y, int dat){ 

	double r=CentroSeparacion(xant, yant, x[0], y[0]);
	
	double dis;
	
	for (int i=0; i<dat;i++){
		dis=CentroSeparacion(xant, yant, x[i], y[i]);
		if(dis<r){
			r=dis;
		}
	}
	return r-1; // radio ionico de cada particula.
}
