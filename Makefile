
build: clean
	python3 setup.py sdist bdist_wheel

release: build
	twine upload -s dist/*

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	rm -rf build
	rm -rf dist
	rm -rf notion.egg-info

install:
	python setup.py install

test:
	@pytest ./notion

test-coverage-report:
	@pytest --cov ./notion

test-coverage-report-html:
	@pytest --cov --cov-report=html ./notion

test-coverage-report-xml:
	@pytest --cov --cov-report=xml ./notion