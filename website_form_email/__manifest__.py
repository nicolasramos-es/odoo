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
    'name': 'Website Contact Form Notification',
    'version': '0.1',
    'summary': 'Send an email when the Web contact form is sent',
    'description': 'Send an email when the Web contact form is sent',
    'category': 'Website',
    'author': 'DV Interactivo',
    'company': 'DV Interactivo',
    'website': 'www.dvinteractivo.com',
    'license': 'AGPL-3',
    'depends': ['website_crm'],
    'data': ['data/website_form_email_data.xml'],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.jpg'],
}
