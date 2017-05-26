Resultados_hw5.pdf: ej.jpg Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

c1.jpg: datos.txt plots_canal_ionico.py 
	python plots_canal_ionico.py

histo1.jpg: datos.txt plots_canal_ionico.py 
	python plots_canal_ionico.py

c2.jpg: datos.txt plots_canal_ionico.py 
	python plots_canal_ionico.py

histo2.jpg: datos.txt plots_canal_ionico.py 
	python plots_canal_ionico.py

carga.jpg:CircuitoRC.txt CircuitoRC.py
	python CircuitoRC.py

HistogramaCarga.jpg:CircuitoRC.txt CircuitoRC.py
	python CircuitoRC.py


datos.txt: Canal_ionico.txt Canal_ionico1.txt canal_ionico.c
	gcc -lm canal_ionico.c
	./a.out >felipe.txt

