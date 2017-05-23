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
# programmers who take the whole responsability of assessing all
# potential consequences resulting from its eventual inadequacies and
# bugs. End users who are looking for a ready-to-use solution with
# commercial garantees and support are strongly adviced to contract a
# Free Software Service Company.
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
# You should have received a copy of the GNU Affero General Public
# License along with this program; if not, see
# <http://www.gnu.org/licenses/> or write to the Free Software
# Foundation, Inc.,59 Temple Place - Suite 330, Boston,
# MA  02111-1307, USA.
#
###############################################

from odoo import fields, models


class TicOdooInstanceSupport(models.Model):
    _name = 'tic.odoo.instance.support'

    instance_name = fields.Char(
        string="Name of the Instance",
        required=True)
    instance_version = state = fields.Selection(
        string="Version of Odoo",
        selection=[('odoo8', 'Odoo 8'),
                   ('odoo9', 'Odoo 9'),
                   ('odoo10', 'Odoo 10')],
        required=True,
        default='odoo10')
    instance_type = fields.Selection(
        string="Type of server",
        selection=[
            ('vps', 'Virtual Private Server'),
            ('v-cloud', 'Virtual Private Cloud'),
            ('cpd', 'CPD'),
            ('local', 'Local Dedicated Server')],
        required=False)
    instance_os_host = fields.Selection(
        string="Operating System of Host",
        selection=[
            ('mswin_server', 'Microsoft Windows Server'),
            ('centos', 'CEntOS'),
            ('ubuntu_server', 'Ubuntu Server'),
            ('linux_debian', 'Other Debian based Linux'),
            ('linux_slackware', 'Other Slackware based Linux'),
            ('linux_redhat', 'Other RedHat based Linux'),
            ('others', 'Others')],
        required=False)
    instance_virtualized = fields.Boolean(string="Is virtualized?")
    instance_os_guest = fields.Selection(string="Operating System of Guest", selection=[
             ('mswin_server', 'Microsoft Windows Server'),
             ('centos', 'CEntOS'),
             ('ubuntu_server', 'Ubuntu Server'),
             ('linux_debian', 'Other Debian based Linux'),
             ('linux_slackware', 'Other Slackware based Linux'),
             ('linux_redhat', 'Other RedHat based Linux'),
             ('others', 'Others')], required=False)
    instance_rma_sr = fields.Char(string="RMA_SR", required=False)
    instance_nginxpowered = fields.Boolean(string='Uses NGINX?')
    instance_dn = fields.Char(string="Domain Name of the installed Odoo", required=False)
    instance_ipfailover = fields.Char(string="IP address failover", required=False, size=15)
    instance_connport = fields.Char(string='Connection Port')
    instance_ssl = fields.Boolean(string='SSL Enabled?')
    instance_managementport = fields.Integer(string="Management Port", required=False)
    instance_managementprotocol = fields.Selection(string="Management Protocol", selection=[
         ('ssh', 'Secure Shell'),
         ('telnet', 'Telecommunication Network'),
         ('rlogin', 'Remote Login'),
         ('other', 'Other Protocol')], required=False)
    instance_managementuser = fields.Char(string='User Management', required=False)
    instance_notes = fields.Text(string="Notes", required=False)


class Installations(models.Model):
    _inherit = 'res.partner'

    odooinstallation = fields.Boolean(string="Has an Odoo Installation?")
    odooinstance_ids = fields.Many2many(
        comodel_name="tic.odoo.instance.support",
        string="Odoo Installations", store=True)
