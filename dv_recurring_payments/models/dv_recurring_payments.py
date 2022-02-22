# -*- coding: utf-8 -*-
######################################################################################
#
#    DIFUSION VISUAL INTERACTIVO S.L.
#
#    Copyright (C) 2014-NOW Difusión Visual(<https://difusionvisual.com>).
#    Author: Nicolás Ramos (Contact : contacto@difusionvisual.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################

from datetime import datetime, date

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class FilterRecurringEntries(models.Model):
    _inherit = 'account.move'

    recurring_ref = fields.Char()


class RecurringPayments(models.Model):
    _name = 'account.recurring.payments'
    _description = 'Accounting Recurring Payment'

    def get_company_id(self):
        return self.env.user.company_id.id

    def _get_next_schedule(self):
        if self.date:
            recurr_dates = []
            today = datetime.today()
            start_date = datetime.strptime(str(self.date), '%Y-%m-%d')
            while start_date <= today:
                recurr_dates.append(str(start_date.date()))
                if self.recurring_period == 'days':
                    start_date += relativedelta(days=self.recurring_interval)
                elif self.recurring_period == 'weeks':
                    start_date += relativedelta(weeks=self.recurring_interval)
                elif self.recurring_period == 'months':
                    start_date += relativedelta(months=self.recurring_interval)
                else:
                    start_date += relativedelta(years=self.recurring_interval)
            self.next_date = start_date.date()

    name = fields.Char('Name')
    debit_account = fields.Many2one('account.account', 'Debit account',
                                    required=True,
                                    domain="['|', ('company_id', '=', False), "
                                           "('company_id', '=', company_id)]")
    credit_account = fields.Many2one('account.account', 'Credit account',
                                     required=True,
                                     domain="['|', ('company_id', '=', False), "
                                            "('company_id', '=', company_id)]")
    journal_id = fields.Many2one('account.journal', 'Journal', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account',
                                          'Analytic Account')
    date = fields.Date('Start date', required=True, default=date.today())
    next_date = fields.Date('Next generation', compute=_get_next_schedule,
                            readonly=True, copy=False)
    date_creation = fields.Date('Create from', required=True, default=date.today())
    recurring_period = fields.Selection(selection=[('days', 'Days'),
                                                   ('weeks', 'Weeks'),
                                                   ('months', 'Months'),
                                                   ('years', 'Years')],
                                        store=True, required=True)
    amount = fields.Float('Amount')
    description = fields.Text('Description')
    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('running', 'Running')],
                             default='draft', string='State')
    journal_state = fields.Selection(selection=[('draft', 'Draft'),
                                                ('posted', 'Posted')],
                                     required=True, default='draft',
                                     string='Generate journal as')
    recurring_interval = fields.Integer('Recurring interval', default=1)
    partner_id = fields.Many2one('res.partner', 'Partner')
    pay_time = fields.Selection(selection=[('pay_now', 'Pay now'),
                                           ('pay_later', 'Pay later')],
                                store=True, required=True)
    company_id = fields.Many2one('res.company',
                                 default=get_company_id)
    recurring_lines = fields.One2many('account.recurring.entries.line', 'tmpl_id')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id.property_account_receivable_id:
            self.credit_account = self.partner_id.property_account_payable_id

    @api.model
    def _cron_generate_entries(self):
        data = self.env['account.recurring.payments'].search(
            [('state', '=', 'running')])
        entries = self.env['account.move'].search(
            [('recurring_ref', '!=', False)])
        journal_dates = []
        journal_codes = []
        remaining_dates = []
        for entry in entries:
            journal_dates.append(str(entry.date))
            if entry.recurring_ref:
                journal_codes.append(str(entry.recurring_ref))
        today = datetime.today()
        for line in data:
            if line.date:
                recurr_dates = []
                start_date = datetime.strptime(str(line.date_creation), '%Y-%m-%d')
                while start_date <= today:
                    recurr_dates.append(str(start_date.date()))
                    if line.recurring_period == 'days':
                        start_date += relativedelta(
                            days=line.recurring_interval)
                    elif line.recurring_period == 'weeks':
                        start_date += relativedelta(
                            weeks=line.recurring_interval)
                    elif line.recurring_period == 'months':
                        start_date += relativedelta(
                            months=line.recurring_interval)
                    else:
                        start_date += relativedelta(
                            years=line.recurring_interval)
                for rec in recurr_dates:
                    recurr_code = str(line.id) + '/' + str(rec)
                    if recurr_code not in journal_codes:
                        remaining_dates.append({
                            'date': rec,
                            'template_name': line.name,
                            'amount': line.amount,
                            'tmpl_id': line.id,
                        })
        child_ids = self.recurring_lines.create(remaining_dates)
        for line in child_ids:
            tmpl_id = line.tmpl_id
            recurr_code = str(tmpl_id.id) + '/' + str(line.date)
            line_ids = [(0, 0, {
                'account_id': tmpl_id.credit_account.id,
                'partner_id': tmpl_id.partner_id.id,
                'credit': line.amount,
                'analytic_account_id': tmpl_id.analytic_account_id.id,
            }), (0, 0, {
                'account_id': tmpl_id.debit_account.id,
                'partner_id': tmpl_id.partner_id.id,
                'debit': line.amount,
                'analytic_account_id': tmpl_id.analytic_account_id.id,
            })]
            vals = {
                'date': line.date,
                'recurring_ref': recurr_code,
                'company_id': self.env.user.company_id.id,
                'journal_id': tmpl_id.journal_id.id,
                'ref': line.template_name,
                'narration': 'Entrada recurrente',
                'line_ids': line_ids
            }
            move_id = self.env['account.move'].create(vals)
            if tmpl_id.journal_state == 'posted':
                move_id.post()


    class GetAllRecurringEntries(models.TransientModel):
        _name = 'account.recurring.entries.line'
        _description = 'Account Recurring Entries Line'

        date = fields.Date('Date')
        template_name = fields.Char('Name')
        amount = fields.Float('Amount')
        tmpl_id = fields.Many2one('account.recurring.payments', string='id')


