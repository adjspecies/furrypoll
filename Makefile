devel:
	${MAKE} -j2 coffee flask-server

coffee:
	node_modules/coffee-script/bin/coffee -o static/js -cw static/coffee&

flask-server:
	python furrypoll.py

.PHONY: coffee devel flask-server
