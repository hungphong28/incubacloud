from odoo import api, models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    @api.model
    def _visible_menu_ids(self, debug=False):
        visible = super()._visible_menu_ids(debug=debug)

        old = self.env.ref(
            "incubacloud.incubacloud_menu_root",
            raise_if_not_found=False,
        )

        new = self.env.ref(
            "incubacloud_extension.menu_cloud_manager",
            raise_if_not_found=False,
        )

        if old and new and old.id in visible and new.id in visible:
            if not any(
                child.id in visible
                for child in old.sudo().child_id
            ):
                return frozenset(visible) - {old.id}

        return visible
