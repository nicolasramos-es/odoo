# -*- coding: utf-8 -*-
######################################################################################
#
#    NICOLASRAMOS.ES
#
#    Copyright (C) 2014-NOW Nicolás Ramos(<https://www.nicolasramos.es>).
#    Author: Nicolás Ramos (Contact : contacto@nicolasramos.es)
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

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def recalcular(self):
        for facturado in self:
            total = 0.0
            for line in facturado.order_line:
                total += line.qty_invoiced * \
                    (line.price_unit * (1 - (line.discount or 0.0) / 100.0))
                facturado.update({
                    'total_facturado': total,
                })

    @api.depends('order_line.qty_invoiced')
    def _total_facturado(self):
        for facturado in self:
            total = 0.0
            for line in facturado.order_line:
                total += line.qty_invoiced * \
                    (line.price_unit * (1 - (line.discount or 0.0) / 100.0))
                facturado.update({
                    'total_facturado': total,
                })

    @api.depends('order_line.qty_delivered')
    def _total_entregado(self):
        for facturado in self:
            total = 0.0
            for line in facturado.order_line:
                total += line.qty_delivered * \
                    (line.price_unit * (1 - (line.discount or 0.0) / 100.0))
                facturado.update({
                    'total_entregado': total,
                })

    @api.onchange('order_line')
    def _total_lineas(self):
        lineas = 0
        for cargas in self.order_line:
            lineas = lineas + 1
        self.numero_lineas = lineas

    total_facturado = fields.Float(string=_('Total invoiced'),
                                   store=True,
                                   readonly=True,
                                   compute='_total_facturado')
    total_entregado = fields.Float(string=_('Total delivered'),
                                   store=True,
                                   readonly=True,
                                   compute='_total_entregado')
    numero_lineas = fields.Integer(string='Number of lines',
                                   compute='_total_lineas')
