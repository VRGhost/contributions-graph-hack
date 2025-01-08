shell:
	pyenv exec poetry shell

autoformat:
	ruff format ./src 
	ruff check --fix ./src