filename=Rapport

build: 
	pdflatex ${filename}.tex
	biber ${filename}
	pdflatex ${filename}.tex
read: 
	evince ${filename}.pdf &

clean: 
	rm -f ${filename}.{ps,log,aux,out,dvi,bbl,blg}


