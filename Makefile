default: ui

clean: clean-build clean-pyc clean-installer
c: clean

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -f .coverage
	rm -f *.log

clean-installer:
	rm -fr output/
	rm -fr app.spec
	rm -f smb3splitoffsetter.spec
	rm -f smb3splitoffsetter.zip

clean-pyc: ## remove Python file artifacts
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*~' -exec rm -f {} +

init:
	pip install -r .

pyinstaller: clean
	pyinstaller --noconfirm --onefile --windowed \
		-n smb3splitoffsetter \
		app.py
	cp -r img/ dist/
	cp README.* dist/
	7z a smb3splitoffsetter.zip dist/*
	7z rn smb3splitoffsetter.zip dist smb3splitoffsetter


release-test: clean
	python setup.py sdist bdist_wheel
	twine upload --repository pypitest dist/*

release-prod: clean
	python setup.py sdist bdist_wheel
	twine upload --repository pypi dist/*

release: release-test release-prod clean

cli:
	python -m smb3splitoffsetter.cli

ui:
	python -m smb3splitoffsetter.ui
