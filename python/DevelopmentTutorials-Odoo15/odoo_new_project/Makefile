docker:
	sudo apt update
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
	apt-cache policy docker-ce
	sudo apt install docker-ce
	sudo systemctl status docker
pull :
	docker pull odoo:15.0
	docker pull postgres:13
	docker pull migorad/addons_test:1.0
push :
	
run :	
	docker stop odoo
	docker container prune
docker-build:
	make docker
	make pull
	make run

