# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

# payment_stripe is an optional soft dependency: it is not declared in
# this module's manifest and is not bundled with every bringout Odoo
# install. Guard the import so website_payment still loads when
# payment_stripe is absent; the is_stripe_supported_country field then
# reports False for every country instead of blowing up module
# registration.
try:
    from odoo.addons.payment_stripe import const
except ImportError:
    const = None


class ResCountry(models.Model):
    _inherit = 'res.country'

    is_stripe_supported_country = fields.Boolean(compute='_compute_is_stripe_supported_country')

    @api.depends('code')
    def _compute_is_stripe_supported_country(self):
        for country in self:
            if const is None:
                country.is_stripe_supported_country = False
                continue
            country.is_stripe_supported_country = const.COUNTRY_MAPPING.get(
                country.code, country.code
            ) in const.SUPPORTED_COUNTRIES
