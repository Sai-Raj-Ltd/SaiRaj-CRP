# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    po_number = fields.Char(string='Job Po Number')


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    online_payment_method = fields.Selection(
        string='Digital Payment Method', selection=[('mpesa', 'Mpesa'), ('visa_card', 'Visa Card'), ('cash', 'Cash'), ('cheque', 'Cheque'), ('master_card', 'Master Card'), ('rtgs', 'RTGS & Transfer')])
    payment_reference = fields.Char(string='Payment Reference', readonly=False)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    online_payment_method = fields.Selection(
        string='Digital Payment Method', selection=[('mpesa', 'Mpesa'), ('visa_card', 'Visa Card'), ('cash', 'Cash'), ('cheque', 'Cheque'), ('master_card', 'Master Card'), ('rtgs', 'RTGS & Transfer')])
    payment_reference = fields.Char(string='Payment Reference', readonly=False)
