import csv
from cola import Cola


archivo = open('Libros.csv', 'r')
lector = csv.reader(archivo, delimiter = ';')
dato = Cola()

for x in lector:
	dato.encolar(x)

autores = Cola()
for slist in dato.items:
	autores.encolar(slist[1])

titulos = Cola()
for slist in dato.items:
	titulos.encolar(slist[0])
	

paginas = Cola()
for slist in dato.items:
	paginas.encolar(slist[3])

tematicas = Cola()
for slist in dato.items:
	tematicas.encolar(slist[2])
	
editoriales = Cola()
for slist in dato.items:
	editoriales.encolar(slist[4])

ordenAutor = Cola()
while (not autores.es_vacia()):
	#Primer orden por titulos
	tempMin = min(autores.items)

	cTitulo = titulos.desencolar()
	cAutor = autores.desencolar()
	cTematica = tematicas.desencolar()
	cPagina = paginas.desencolar()
	cEditorial = editoriales.desencolar()

	if (cAutor != tempMin):
		titulos.encolar(cTitulo)
		autores.encolar(cAutor)
		tematicas.encolar(cTematica)
		paginas.encolar(cPagina)
		editoriales.encolar(cEditorial)
	else:
		ordenAutor.encolar([tempMin, cAutor, cTematica, cPagina, cEditorial])

archivo = open('Libros.csv', 'r')
lector = csv.reader(archivo, delimiter = ';')
dato = Cola()

for x in lector:
	dato.encolar(x)

autores = Cola()
for slist in dato.items:
	autores.encolar(slist[1])

titulos = Cola()
for slist in dato.items:
	titulos.encolar(slist[0])
	

paginas = Cola()
for slist in dato.items:
	paginas.encolar(slist[3])

tematicas = Cola()
for slist in dato.items:
	tematicas.encolar(slist[2])
	
editoriales = Cola()
for slist in dato.items:
	editoriales.encolar(slist[4])
ordenPaginas = Cola()
while (not tematicas.es_vacia()):
        #ordenado por paginas
        tempMin = min(tematicas.items)
        cTitulo = titulos.desencolar()
        cAutor = autores.desencolar()
        cTematica = tematicas.desencolar()
        cPagina = paginas.desencolar()
        cEditorial = editoriales.desencolar()

        if (cTematica != tempMin):
                titulos.encolar(cTitulo)
                autores.encolar(cAutor)
                tematicas.encolar(cTematica)
                paginas.encolar(cPagina)
                editoriales.encolar(cEditorial)
        else:
                ordenPaginas.encolar([tempMin, cAutor, cTematica, cPagina, cEditorial])


print('****************************************************************************************')
print('\n'.join(['\t'.join([str(cell) for cell in x]) for x in dato.items]))

print('\n****************************************************************************************')
print('\n'.join(['\t'.join([str(cell) for cell in x]) for x in ordenAutor.items]))

print('\n****************************************************************************************')
print('\n'.join(['\t'.join([str(cell) for cell in x]) for x in ordenPaginas.items]))
