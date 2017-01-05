python3:
	echo "Installing Python 3 and pip3" &&\
	sudo apt install -y python3 python3-pip &&\
	echo "Successfully installed"

prepare: python3
	echo "Installing python dependencies" &&\
	sudo pip3 install -r requirements.txt &&\
	echo "Successfully installed"

prepare-dev: prepare
	echo "Installing dev dependencies" &&\
	sudo pip3 install -r requirements-dev.txt &&\
	echo "Successfully installed"

install-mongo:
	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 &&\
  echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list &&\
  sudo apt update &&\
  sudo apt install -y mongodb-org &&\

install: prepare install-mongo
	echo "Execute make run to production environment"

install-dev: prepare-dev install-mongo
	echo "Execute make run-dev to development environment"

pep8:
	pep8 src

run-dev: pep8 prepare-dev
	cd src &&\
	export FLASK_DEBUG=1 &&\
	export FLASK_APP=server.py &&\
	flask run

run: prepare
	cd src &&\
	export FLASK_DEBUG=0 &&\
	export FLASK_APP=server.py &&\
	flask run
