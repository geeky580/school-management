from odoo import api, fields, models


class HrInherit(models.Model):
    _inherit = "hr.employee"

    gautam = fields.Char(string='Inherited Row')


    teacher_id = fields.One2many('class.data','student_id')


