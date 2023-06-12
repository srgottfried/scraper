.ONESHELL:

install:
	@sudo apt update > /dev/null 2>&1
	@sudo apt -y upgrade > /dev/null 2>&1
	@sudo apt install python3 -y > /dev/null 2>&1
	@sudo apt install python3-pip > /dev/null 2>&1
	@make venv > /dev/null

venv:
	@python3 -m venv env
	@. env/bin/activate
	@pip install -r requirements.txt > /dev/null