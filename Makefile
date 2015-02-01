NODE_TARGETS=node_modules/coffee-script node_modules/handlebars

devel:
	${MAKE} -j2 coffee flask-server

coffee:
	node_modules/coffee-script/bin/coffee -o static/js -cw static/coffee&

flask-server:
	python furrypoll.py

templates:
	node_modules/handlebars/bin/handlebars -f static/js/templates.js static/templates/*

# If you're interested in hacking, here's the default environment setup;
# feel free to do the same thing with your own setup!
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

.PHONY: clean clean-all coffee deps devel flask-server
