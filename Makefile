lint:
	sorti --check .
	black --check .
	flake8 .
	mypy .

clean:
	rm -rf .tox/ dist/ *.egg *.egg-info .coverage* .eggs build/

publish: lint clean
	pip install --upgrade wheel twine
	python setup.py sdist bdist_wheel
	twine upload dist/*
