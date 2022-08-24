start:
	sudo systemctl enable odoo.service
	sudo systemctl restart odoo.service
	sudo tail -f /var/log/odoo/odoo.log

reboot:
	sudo chown odoo: /etc/odoo.conf
	sudo chmod 640 /etc/odoo.conf
	sudo chown odoo:root /var/log/odoo
	sudo chmod 755 /etc/systemd/system/odoo.service
	sudo chown root: /etc/systemd/system/odoo.service
	sudo systemctl start odoo.service
	sudo systemctl status odoo.service
