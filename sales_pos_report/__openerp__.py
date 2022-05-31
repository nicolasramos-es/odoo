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

{
    'name': 'POS Report Advanced',
    'version': '1.1',
    'summary': 'Advanced POS report with costs, margin and more',
    'description': 'Advanced POS report with costs, margin and more',
    'category': 'Point Of Sale',
    'author': 'Difusión Visual Interactivo S.L.',
    'company': 'Difusión Visual Interactivo S.L.',
    'contributors': [
        "Nicolás Ramos <contacto@difusionvisual.com>",
    ],
    'website': 'www.difusionvisual.com',
    'license': 'AGPL-3',
    'depends': ['point_of_sale',
                'sale',
                'account',
                ],
    'data': [
        'report/sales_pos_report.xml',
        'views/product_view.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
    'auto_install': False,
    'images':  ['static/description/banner.png'],
    'price': 19.00,
    'currency': 'EUR',
}