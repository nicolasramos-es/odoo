# -*- coding: utf-8 -*-
######################################################################################
#
#    NICOLASRAMOS.ES
#
#    Copyright (C) 2014-NOW Nicolás Ramos(<https://www.nicolasramos.es>).
#    Author: Nicolás Ramos (Contact : contacto@nicolasramos.es)
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
    'name': "Warning another Sales order",
    'summary': """
        Create warning in sales order and another one is already open and pending invoiced. """,
    'author': 'Nicolás Ramos',
    'contributors': [
        "Nicolás Ramos <contacto@nicolasramos.es>",
    ],
    'website': "https://nicolasramos.es",
    'category': 'Sales',
    'version': "14.0.1.0.0",
    'license': 'OPL-1',
    'depends': ['base', 'sale_management'],
    'images': ['static/description/banner.png'],
    'data': [],
    'installable': True,
    'application': False,
}
