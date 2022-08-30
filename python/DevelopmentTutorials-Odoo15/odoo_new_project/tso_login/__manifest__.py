{
    'name': 'TSO LOGIN',
    'version': '1.0.0',
    'category': 'ORM/TSO',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'website': '',
    'depends': [
        "web",
    ],
    'data': [
        # 'views/website_templates.xml',
            'views/login_layout.xml',
    
    ],
    'demo': [
    ],
    "assets": {
        "web.assets_frontend": [
            "tso_login/static/src/css/web_login_style.css"
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False
}