from email.policy import default
from odoo import api, fields, models, _
from werkzeug.urls import url_encode
from odoo.exceptions import ValidationError, AccessError, UserError


class HrEmployeePrivate(models.Model):
    _inherit = "hr.employee"
    confirmed_user_id  = fields.Many2many('res.users', string= "Confirmed user")
    user_name = fields.Char(string="User Name")
    staff_id = fields.Char(string="Staff ID")
    status  = fields.Selection([('active', 'Active'),('inactive', 'Inactive')],default="inactive")
    command = fields.Char(string="Command")
    password = fields.Char(string="Password")
    role = fields.Char(string="Role")

    def unlink(self):
        super(HrEmployeePrivate,self).unlink()


    def read_button(self):
        resources = self.mapped('resource_id')
        load = '_classic_read'
        private_fields = set(resources).difference(self.env['hr.employee.public']._fields.keys())
        if private_fields:
            raise AccessError(_('The fields "%s" you try to read is not available on the public employee profile.') % (','.join(private_fields)))   
        return self.env['hr.employee.public'].browse(self.ids).read_button(resources, load=load)

    # def read(self):
    #     super(HrEmployeePrivate,self).read()
        # resources_fields = set(resources).difference(self.env['hr.employee.public']._fields.keys())
        # return resources
    # def read(self, fields, load='_classic_read'):
    #     super(HrEmployeePrivate, self).read(fields, load=load)

    # def name_get(self):
    #     super(HrEmployeePrivate,self).name_get()
    

    # def toggle_active(self):
    #     super(HrEmployeePrivate,self).toggle_active()

    # def get_formview_id(self, access_uid=None):
    #     super(HrEmployeePrivate,self).get_formview_id(access_uid)

    # def read(self, fields, load='_classic_read'):
    #     super(HrEmployeePrivate,self).read(fields, load)






