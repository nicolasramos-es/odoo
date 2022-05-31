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

from openerp.osv import fields, osv, orm
from openerp import models, api


class purchase_order_line2(osv.osv):
    _inherit = "purchase.order.line"
    _columns = {
        'prodlot2_id': fields.many2one('stock.production.lot', "Lot No.")
    }


class stock_transfer_details2(models.TransientModel):
    _inherit = 'stock.transfer_details'

    def fields_view_get(self, cr, uid, view_id=None, view_type='form',
                        context=None, toolbar=False, submenu=False):
        result = super(stock_transfer_details2, self).fields_view_get(cr, uid, view_id,
                                                                      view_type, context, toolbar, submenu)
        return result

    def default_get(self, cr, uid, fields, context=None):
        res = super(stock_transfer_details2, self).default_get(cr, uid, fields, context=context)
        if context is None: context = {}
        picking_ids = context.get('active_ids', [])
        active_model = context.get('active_model')
        purchase_order_pool = self.pool.get('purchase.order')
        stock_pack_pool = self.pool.get('stock.pack.operation')
        purchase_ids = purchase_order_pool.search(cr, uid, [('picking_ids', '=', picking_ids[0])])

        if not picking_ids or len(picking_ids) != 1:
            # Procesamiento parcial del albarán que solo se podrá hacer una a la vez
            return res
        assert active_model in ('stock.picking'), 'Bad context propagation'
        picking_id, = picking_ids
        picking = self.pool.get('stock.picking').browse(cr, uid, picking_id, context=context)
        items = []
        packs = []
        if not picking.pack_operation_ids:
            picking.do_prepare_partial()
        # Código personalizado
        if purchase_ids:
            pack_op_ids = [x.id for x in picking.pack_operation_ids]
            for each_line in purchase_order_pool.browse(cr, uid, purchase_ids[0]).order_line:
                line_product_id = each_line.product_id.id
                line_lot_id = each_line.prodlot2_id.id
                if line_lot_id:
                    for each_op in picking.pack_operation_ids:
                        if each_op.product_id.id == line_product_id:
                            if not each_op.lot_id:
                                stock_pack_pool.write(cr, uid, each_op.id, {'lot_id': line_lot_id})
                                break

        # Código personalizado
        for op in picking.pack_operation_ids:
            item = {
                'packop_id': op.id,
                'product_id': op.product_id.id,
                'product_uom_id': op.product_uom_id.id,
                'quantity': op.product_qty,
                'package_id': op.package_id.id,
                'lot_id': op.lot_id.id,
                'sourceloc_id': op.location_id.id,
                'destinationloc_id': op.location_dest_id.id,
                'result_package_id': op.result_package_id.id,
                'date': op.date,
                'owner_id': op.owner_id.id,
            }
            if op.product_id:
                items.append(item)
            elif op.package_id:
                packs.append(item)
        res.update(item_ids=items)
        res.update(packop_ids=packs)
        return res
