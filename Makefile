SRC = $(wildcard nbs/*.ipynb)

docs_serve: docs
	cd docs && bundle exec jekyll serve
