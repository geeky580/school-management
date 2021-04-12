from odoo import models, fields, api


class Create_exam(models.TransientModel):
    _name = "create.exam"

    student_exam_id = fields.Many2many("student.data")
    create_exam_id = fields.Many2one("subject.data", string="subject")
    exam_bnao = fields.Char(string="Marks Obtained", copy=False)
    total_marks = fields.Char(string="Total Marks", copy=False)

    def button_exam(self):
        for rec in self.student_exam_id:
            vals = {
                'total_marks': self.total_marks,
                'marks_obtained': self.exam_bnao,
                'subject_id': self.subject_exam_id.id,
                'student_id': rec.id,

            }
            record = self.env['exam.profile'].create(vals)
            print(record)







