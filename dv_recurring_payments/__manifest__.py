# -*- coding: utf-8 -*-
######################################################################################
#
#    DIFUSION VISUAL INTERACTIVO S.L.
#
#    Copyright (C) 2014-NOW Difusión Visual(<https://difusionvisual.com>).
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
    "name": "Account Recurring Payments",
    "version": "12.0.0.0.1",
    "summary": """Account Recurring Payments""",
    "description": """Account Recurring Payments""",
    "category": "Accounting",
    "author": "Difusion Visual Interactivo",
    "company": "Difusion Visual Interactivo SL",
    "website": "https://difusionvisual.com",
    "maintainer": "Difusion Visual Interactivo",
    "contributors": [
        "Nicolás Ramos <contacto@difusionvisual.com>",
    ],
    "depends": ["base", "account"],
    "data": [
        "security/ir.model.access.csv",
        "data/recurring_entry_cron.xml",
        "views/dv_recurring_payments_view.xml",
       
    ],
    "qweb": [],
    "license": "OPL-1",
    "installable": True,
    "auto_install": False,
    "application": False,
    "images": ["static/description/banner.png"],
}
