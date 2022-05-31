#!/usr/bin/python
##############################################
#
# Nicolás Ramos S.L.
# Copyright (C) Nicolás Ramos S.L.
# all rights reserved
# http://nicolasramos.es
# contacto@nicolasramos.es
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
    "name": "stock_limit_order_lines",
    "summary": """
        stock_limit_order_lines""",
    # 'description': put the module description in README.rst
    "author": "Nicolás Ramos",
    "website": "https://nicolasramos.es",
    "category": "Extra Rights",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "base",
        "stock",
    ],
    "data": [
        "views/stock_limit_order_lines.xml",
    ],
}
