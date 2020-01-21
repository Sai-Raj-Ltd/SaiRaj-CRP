# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (https://opensource.org/licenses/LGPL-3.0).
#
# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, or if you have received a written
# agreement from the authors of the Software (see the COPYRIGHT section below).
#
# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
#########COPYRIGHT#####
# © 2016 Bernard K Too<bernard.too@optima.co.ke>
from odoo import models, fields, api


class hr_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.user.company_id.id)
    payslip_logo = fields.Binary(
        string='Payslip Logo',
        attachment=True,
        help="Default Logo for Payslips",
        related='company_id.payslip_logo')
    template_id = fields.Many2one(
        'ir.ui.view',
        'Payslip Template',
        related='company_id.ptemplate_id')
    detailed_template_id = fields.Many2one(
        'ir.ui.view',
        'Detailed Payslip Template',
        related='company_id.pdetailed_template_id')
    odd = fields.Char(
        'Odd parity Color',
        help="The background color for Odd lines in the payslip",
        related='company_id.podd',
        required=True)
    even = fields.Char(
        'Even parity Color',
        help="The background color for Even lines in the payslip",
        related='company_id.peven',
        required=True)
    theme_color = fields.Char(
        'Theme Color',
        help="The Main Theme color of the payslip",
        related='company_id.ptheme_color',
        required=True)
    theme_txt_color = fields.Char(
        'Theme Text Color',
        help="The font color of the areas with the theme color",
        related='company_id.ptheme_txt_color')
    text_color = fields.Char(
        'Text Color',
        help="The Text color of the payslip",
        related='company_id.ptext_color',
        required=True)
    name_color = fields.Char(
        'Company Name Color',
        help="The Text color of the Company Name",
        related='company_id.pname_color',
        required=True)
    cust_color = fields.Char(
        'Employee Name Color',
        help="The Text color of the Employee Name",
        related='company_id.pcust_color',
        required=True)
    header_font = fields.Selection([(x,
                                     str(x)) for x in range(1,
                                                            51)],
                                   string="Header Font-Size(px):",
                                   related='company_id.pheader_font',
                                   required=True)
    body_font = fields.Selection([(x,
                                   str(x)) for x in range(1,
                                                          51)],
                                 string="Body Font-Size(px):",
                                 related='company_id.pbody_font',
                                 required=True)
    footer_font = fields.Selection([(x,
                                     str(x)) for x in range(1,
                                                            51)],
                                   string="Footer Font-Size(px):",
                                   related='company_id.pfooter_font',
                                   required=True)
    font_family = fields.Char(
        'Font Family:',
        related='company_id.pfont_family')
