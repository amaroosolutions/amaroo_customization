# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'


    default_expense_account_id = fields.Many2one('account.account', string="Default Expense Account")
    default_expense_taxes_id = fields.Many2many('account.tax', 'vendor_taxes_rel', 'vendor_id', 'tax_id', domain=[('type_tax_use','=','purchase')], string='Default Expense Taxes')

