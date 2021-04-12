from odoo import api, fields, models

class StudentData(models.Model):
    _name = "student.data"
    _description = "Student Data"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')

    classs_id = fields.Many2one(
        'class.data', string='class'
    )


    subject_ids = fields.Many2many('subject.data','student_subject_relation','subject_id','student_id')

    student_id = fields.Many2one('exam.data', string='exam')
    student = fields.Many2one('class.data', string='Class')


