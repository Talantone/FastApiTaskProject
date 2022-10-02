.PHONY: runserver

requirements:
	pip3 install -r requirements.txt
runserver:
	python3 main.py

.DEFAULT_GOAL := runserver