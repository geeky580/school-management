from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.test_module.report_student_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("lines", lines)
        format = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Student Card')

        # bold = workbook.add_format({'bold': True})

        # sheet.writer(1,1,lines.student_name,format)
        sheet.write(0, 0, 'Name', format)
        sheet.write(0, 1, 'Age', format)
        sheet.write(0, 2, 'Gender', format)
        sheet.write(0, 3, 'Description', format)

        for i, line in enumerate(lines):
            sheet.write(i+1, 0, line.name, format1)
            sheet.write(i+1, 1, line.age, format1)
            sheet.write(i+1, 2, line.gender, format1)
            sheet.write(i+1, 3, line.note, format1)
