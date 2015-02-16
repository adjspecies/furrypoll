NODE_TARGETS=node_modules/coffee-script node_modules/handlebars

build: clean deps templates coffee-build

devel:
	${MAKE} -j2 coffee flask-server

flask-server:
	python furrypoll.py

coffee: $(NODE_TARGETS)
	node_modules/coffee-script/bin/coffee -o static/js -cw static/coffee&

coffee-build: $(NODE_TARGETS)
	node_modules/coffee-script/bin/coffee -o static/js -c static/coffee

templates: $(NODE_TARGETS)
	node_modules/handlebars/bin/handlebars -f static/js/templates.js static/templates/*

.venv/bin/python:
	virtualenv .venv

$(NODE_TARGETS): package.json
	npm install

deps: .venv/bin/python $(NODE_TARGETS)
	.venv/bin/pip install -r requirements.pip

clean:
	find . -name '*.py[co]' -exec rm -f {} \;

clean-all: clean
	rm -rf .venv
	rm -rf node_modules

.PHONY: build clean clean-all coffee coffee-build deps devel flask-server templates
