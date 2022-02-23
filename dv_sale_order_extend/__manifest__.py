# -*- coding: utf-8 -*-
######################################################################################
#
#    DIFUSION VISUAL INTERACTIVO S.L.
#
#    Copyright (C) 2014-NOW Difusión Visual(<https://www.difusionvisual.com>).
#    Author: Nicolás Ramos (Contact : contacto@difusionvisual.com)
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
{
    'name': "Sale Order Extend",
    'summary': """
        Adds to the sales order the units and total invoiced, shipped and total lines. """,
    'author': 'Difusión Visual Interactivo',
    'contributors': [
        "Nicolás Ramos <contacto@difusionvisual.com>",
    ],
    'website': "https://difusionvisual.com",
    'category': 'Sales',
    'version': "14.0.1.0.0",
    'license': 'OPL-1',
    'depends': [
        'base',
        'sale_management'
    ],
    'images': ['static/description/banner.png'],
    'data': [
        'view/dv_sale_order_extend.xml'
    ],
    'installable': True,
    'application': False,
}
