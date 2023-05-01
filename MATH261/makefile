dirName = $(shell date +'%m_%d_%Y')


PHONY: clean
clean:
	-@rm -r **/*.aux
	-@rm -r **/*.fdb_latexmk
	-@rm -r **/*.fls
	-@rm -r **/*.log
	-@rm -r **/*.synctex.gz

PHONY: today
today:
	@echo 'Creating folder' $(dirName)
	@mkdir ./$(dirName)
	@echo Copying Template.tex to folder
	@cp Template.tex ./$(dirName)/
	@code-insiders ./$(dirname)/Template.tex

PHONY: save
save:
	git add .
	git commit -m "Notes From $(dirName)"
	git push
