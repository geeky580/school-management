from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.test_module.report_student_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("lines", lines)
        format = workbook.add_format({'font_size':14, 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('Student Card')

        # bold = workbook.add_format({'bold': True})

        # sheet.writer(1,1,lines.student_name,format)

        for i in range(10):
            sheet.write(i, 0, 'Name', format)
            sheet.write(i,1, 'Age', format)
            sheet.write(i,2, 'Gender', format)
            sheet.write(i,3, 'Description', format)
