#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################
#
# Difusión Visual
# Copyright (C) Difusión Visual
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

from openerp import api, fields, models

class ContactLink(models.Model):
    _inherit = 'res.partner'

    link = fields.Char()

    @api.multi
    def go_to_partner(self):
        self.ensure_one()
        action = {
            'name': self.env['res.partner']._description,
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner',
            'view_type': 'form',
            'view_mode': 'form,tree,kanban',
            'target': 'current',
            'res_id': self[0].id,
        }
        return action
