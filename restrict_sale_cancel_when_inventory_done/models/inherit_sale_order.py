# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError



class RestrictSaleOrderCancel(models.Model):
    _inherit = "sale.order"

    is_receipt = fields.Boolean()

    def action_cancel(self):
        for sale_order in self:
            sale_order.is_receipt = any(picking.state == 'done' for picking in sale_order.picking_ids)
            if sale_order.is_receipt:
                raise ValidationError("You can't cancel this order because the inventory receipt is already completed.")

        cancel_warning = self._show_cancel_wizard()
        if cancel_warning:
            return {
                'name': _('Cancel Sales Order'),
                'view_mode': 'form',
                'res_model': 'sale.order.cancel',
                'view_id': self.env.ref('sale.sale_order_cancel_view_form').id,
                'type': 'ir.actions.act_window',
                'context': {'default_order_id': self.id},
                'target': 'new'
            }
        return self._action_cancel()



