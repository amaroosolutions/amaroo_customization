# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'


    @api.model
    def default_get(self, fields):
        rec = super(AccountInvoiceLine, self).default_get(fields)
        self.env.context = dict(self.env.context) or {}
        if 'vendor' in self.env.context and self.env.context['vendor']:
            vendor = self.env['res.partner'].browse(self.env.context['vendor'])
            if vendor.default_expense_account_id:
                rec['account_id'] = vendor.default_expense_account_id.id
            if vendor.default_expense_taxes_id:
                rec['invoice_line_tax_ids'] = [(6, 0, vendor.default_expense_taxes_id.ids)]
        return rec
    
    @api.onchange('account_id')
    def _onchange_account_id(self):
        if 'vendor' in self.env.context and self.env.context['vendor']:
            vendor = self.env['res.partner'].browse(self.env.context['vendor'])
            if vendor.default_expense_account_id and vendor.default_expense_account_id == self.account_id:
                return 
        return super(AccountInvoiceLine, self)._onchange_account_id()
