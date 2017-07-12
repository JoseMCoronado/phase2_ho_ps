# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Harbour July 2017 Phase 2 Customization',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
A Variet of improvements to sales...
        """,
    'depends': ['base_action_rule','base_import','sale','purchase','stock','website_quote','account'],
    'data': [
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_actions_server.xml',
        'data/ir_ui_view.xml',
        'data/ir_ui_menu.xml',
        'data/base_automation.xml',
    ],
    'installable': True,
    'application': True,
}
