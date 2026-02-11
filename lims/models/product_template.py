# Copyright 2023 Dixmit
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    laboratory_uom_id = fields.Many2one("uom.uom")
    sample_type_ids = fields.Many2many("lims.sample.type")
    service_tracking = fields.Selection(
        selection_add=[
            ("laboratory", "Laboratory"),
        ],
        ondelete={
            "laboratory": "set default",
        },
    )
