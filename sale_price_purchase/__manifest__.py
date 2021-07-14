##############################################
#
# Ibérica Sistemas
# Copyright (C) Ibérica Sistemas
# all rights reserved
# http://ibericasistemas.com
# contacto@ibericasistemas.com
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
    "name": "Sale Price in purchase order",
    "summary": "Add sale price in purchase order",
    "version": "12.0.1.0.0",
    "category": "Purchase",
    "website": "http://www.ibericasistemas.com",
    "author": "Ibérica Sistemas",
    'contributors': [
        "Nicolás Ramos <contacto@ibericasistemas.com>",
    ],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "purchase",
    ],
    "data": [
        "views/sale_price_purchase.xml",
    ],
    'images': ['static/description/banner.jpg'],
}
