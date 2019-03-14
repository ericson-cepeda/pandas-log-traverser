install-env:
	PIPENV_VENV_IN_PROJECT=1 pipenv install

app-run:
	pipenv shell | true
	python app.py