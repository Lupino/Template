all:
	latex main
	#bibtex main
	latex main
	./bin/touni.py main
	latex main
	dvipdfm main
clean:
	rm -f *.aux
	rm -f *.bak
	rm -f *.log
	rm -f *.bbl
	rm -f *.dvi
	rm -f *.blg
	rm -f *.thm
	rm -f *.toc
	rm -f *.out
	rm -f *~ pages/*~

