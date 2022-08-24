{
    'name': "Weather",
    'category': 'Weather',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,

    'author': "Employee",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',

    'depends': ['base'],
    'data':[
        "security/weather_security.xml",
        "security/ir.model.access.csv",
        'views/weather_xml.xml',
        "views/form_post.xml",
        'views/weather_forecast_views.xml',
        'views/employee_views.xml',
        'views/menu.xml',
        # 'views/te.xml',
        # 'views/employee_views.xml',
    ]
}

# start:
# 	sudo systemctl enable odoo.service
# 	sudo systemctl restart odoo.service
# 	sudo tail -f /var/log/odoo/odoo.log

