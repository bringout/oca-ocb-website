# Customer Portal


This module adds required base code for a fully integrated customer portal.
It contains the base controller class and base templates. Business addons
will add their specific templates and controllers to extend the customer
portal.

This module contains most code coming from odoo v10 website_portal. Purpose
of this module is to allow the display of a customer portal without having
a dependency towards website editing and customization capabilities.

## Installation

```bash
pip install odoo-bringout-oca-ocb-portal
```

## Dependencies

- web
- html_editor
- http_routing
- mail
- auth_signup

## Source

- Repository: https://github.com/OCA/OCB
- Branch: 19.0
- Path: addons/portal

## License

This package preserves the original LGPL-3 license.
