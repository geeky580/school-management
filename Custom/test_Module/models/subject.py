from odoo import api, fields, models


class SubjectData(models.Model):
    _name = "subject.data"
    _description = "Subject Data"

    name = fields.Char(string='Subject_Name')
    note = fields.Text(string='Description')


    student_ids = fields.Many2many('student.data','student_subject_relation','student_id','subject_id')

    subject_id = fields.One2many('exam.data', 'exam_ids')
    create_exam_id = fields.One2many('create.exam', 'create_exam_id')

    def button_exam(self):
        return {
            'name': ('Create Form'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'create.exam',
            'type': 'ir.actions.act_window',
            'target':'new'


        }
