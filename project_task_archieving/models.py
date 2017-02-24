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

from openerp import models, fields, api


class project_task_order(models.Model):
    _inherit = 'project.task'

    archivebool = fields.Boolean('Archive', store=True, track_visibility='onchange')


    def _track_subtype(self, init_values):
        if 'archivebool' in init_values:
            return 'mail.mt_comment'
        return False

    @api.one
    def archive_task(self):
        self.date_deadline = False
        self.write({'archivebool': 'True'})
        return True

    @api.one
    def unarchive_task(self):
        self.write({'archivebool': ''})
        return True
