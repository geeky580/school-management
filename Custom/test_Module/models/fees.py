from odoo import api, fields, models


class FeesData(models.Model):
    _name = "fees.data"
    _description = "Fees Data"

    dues = fields.Char(string='Amount', required=False)
    classs = fields.Char(string='Class', required=False)
    student_name = fields.Char(string='Student ', required=False)
    note = fields.Text(string='Description')
