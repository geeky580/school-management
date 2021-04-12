from odoo import api, fields, models


class ExamData(models.Model):
    _name = "exam.data"
    _description = "Exam Data"

    subject_name = fields.Char(string='Subject Name', required=True)
    percentage = fields.Integer(string='Percentage', required=True)
    date = fields.Char(string='Date', required=True)
    note = fields.Text(string='Description')

    exam_id = fields.Many2one('student.data',string='Students')
    exam_ids = fields.Many2one('subject.data',string='Subject')










