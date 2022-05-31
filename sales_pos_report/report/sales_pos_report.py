#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Difusión Visual Interactivo S.L.
# Copyright (C) Difusión Visual Interactivo S.L.
# all rights reserved
# http://difusionvisual.com
# contacto@difusionvisual.com
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/> or
# write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
###############################################

from openerp import tools
from openerp.osv import fields, osv


class sale_pos_report(osv.osv):
    _name = "sale.pos.report"
    _description = "POS orders report advanced"
    _auto = False

    _columns = {
        'date': fields.datetime('Date', readonly=True),
        'partner_id': fields.many2one('res.partner', 'Partner', readonly=True),
        'product_id': fields.many2one('product.product', 'Product', readonly=True),
        'state': fields.selection(
            [('draft', 'New'), ('paid', 'Closed'), ('done', 'Synchronized'), ('invoiced', 'Invoiced'),
             ('cancel', 'Cancelled')],
            'State'),
        'user_id': fields.many2one('res.users', 'Salesperson', readonly=True),
        'price_total': fields.float('Total Sale', readonly=True),
        'cost_total': fields.float('Total Cost', readonly=True),
        'total_discount': fields.float('Total Discount', readonly=True),
        'average_price': fields.float('Average Price', readonly=True, group_operator="avg"),
        'location_id': fields.many2one('stock.location', 'Location', readonly=True),
        'company_id': fields.many2one('res.company', 'Company', readonly=True),
        'nbr': fields.integer('# of Lines', readonly=True),  # TDE FIXME master: rename into nbr_lines
        'product_qty': fields.integer('Qty', readonly=True),
        'journal_id': fields.many2one('account.journal', 'Journal'),
        'delay_validation': fields.integer('Delay Validation'),
        'product_categ_id': fields.many2one('product.category', 'Category', readonly=True),
        'standard_price_unit': fields.float('Cost Price', readonly=True, group_operator="avg"),
        'margin': fields.float('Margin', readonly=True),
        'tax_total': fields.float('Cost with tax', readonly=True),
        'margin_total_percentage': fields.float(
            string="Margin (%)", readonly=True,
            group_expression="( 1 - (sum(cost_total) / sum(price_total)) ) * 100")
    }
    _order = 'date desc'

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'sale_pos_report')
        cr.execute("""
            create or replace view sale_pos_report as (
                select
                    min(l.id) as id,
                    count(*) as nbr,
                    s.date_order as date,
                    sum(l.qty * u.factor) as product_qty,
                    sum(l.qty * l.price_unit) as price_total,
                    sum((l.qty * l.price_unit) * (l.discount / 100)) as total_discount,
                    (sum(l.qty*l.price_unit)/sum(l.qty * u.factor))::decimal as average_price,
                    sum(cast(to_char(date_trunc('day',s.date_order) - date_trunc('day',s.create_date),'DD') as int)) as delay_validation,
                    s.partner_id as partner_id,
                    s.state as state,
                    s.user_id as user_id,
                    s.location_id as location_id,
                    s.company_id as company_id,
                    s.sale_journal as journal_id,
                    l.product_id as product_id,
                    pt.categ_id as product_categ_id,
                    (sum(l.qty*l.cost_price)/sum(l.qty * u.factor))::decimal as standard_price_unit,
                    sum(l.cost_price * l.qty) as cost_total,
                    sum((l.cost_price * at.amount) + (l.cost_price * l.qty)) as tax_total,
                    (coalesce((1.0 - (sum(l.cost_price * l.qty) / NULLIF(sum(l.qty * l.price_unit *
                    (100.0 - l.discount) / 100.0), 0))) * 100.0, 0.0)) as margin_total_percentage,
                    sum((l.price_unit * l.qty) - (l.cost_price * l.qty)) as margin
                from pos_order_line as l
                    left join pos_order s on (s.id=l.order_id)
                    left join product_product p on (p.id=l.product_id)
                    left join product_template pt on (pt.id=p.product_tmpl_id)
                    left join product_uom u on (u.id=pt.uom_id)
                    left join product_supplier_taxes_rel pst on (pst.prod_id=p.product_tmpl_id)
                    left join account_tax at on (at.id=pst.tax_id)
                group by
                    s.date_order, s.partner_id,s.state, pt.categ_id,
                    s.user_id,s.location_id,s.company_id,s.sale_journal,l.product_id,s.create_date
                having
                    sum(l.qty * u.factor) != 0)""")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
