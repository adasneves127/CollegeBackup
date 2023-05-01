dirName = $(shell date +'%m_%d_%Y')

all:
	latex Template.tex
	dvips Template.dvi
	ps2pdf Template.ps
	open Template.pdf

PHONY: clean
clean:
	rm *.aux
	rm *.fdb_latexmk
	rm *.fls
	rm *.log
	rm *.synctex.gz

PHONY: today
today:
	@echo 'Creating folder' $(dirName)
	@mkdir $(dirName)
	@echo Copying Template.tex to folder
	@cp Template.tex $(dirName)
	@cp makefile $(dirName)
	@cp .chktexrc $(dirName)
	@code-insiders $(dirName)/Template.tex

PHONY: save
save:
	git add .
	git commit -m "Notes From $(dirName)"
	git push

PHONY: clean
clean:
	-rm -r ./**/*.aux
	-rm -r ./**/*.fdb_latexmk
	-rm -r ./**/*.fls
	-rm -r ./**/*.log
	-rm -r ./**/*.synctex.gz
