from odoo.addons.web.controllers.main import Home
import odoo
import odoo.modules.registry
from odoo import http
from odoo.http import request
_logger = logging.getLogger(__name__)


class LoginHome(Home):

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        return super(LoginHome, self).web_login(redirect, **kw)


