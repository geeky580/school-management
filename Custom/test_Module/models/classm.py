from odoo import api, fields, models


class ClassData(models.Model):
    _name = "class.data"
    _description = "Class Data"

    name = fields.Char(string='Name', required=True)
    note = fields.Text(string='Description')

    student_id = fields.One2many('student.data', 'classs_id')
    teacher_id = fields.Many2one('hr.employee', string='Teacher ID')








