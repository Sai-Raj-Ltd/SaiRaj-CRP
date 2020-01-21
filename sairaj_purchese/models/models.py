# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sairaj_purchese(models.Model):
    _inherit= 'res.partner'

    vendor_type = fields.Selection([('On Account Vendors','On Account Vendors'),('Non Account Vendors','Non Account Vendors')],copy=False, index=True, default='On Account Vendors',track_visibility='onchange')

