# Security

Access control and security definitions in website_crm_iap_reveal.

## Access Control Lists (ACLs)

Model access permissions defined in:
- **[ir.model.access.csv](../website_crm_iap_reveal/security/ir.model.access.csv)**
  - 4 model access rules

## Record Rules

Row-level security rules defined in:
- **[ir_rules.xml](../website_crm_iap_reveal/security/ir_rules.xml)**

## Security Groups & Configuration

Security groups and permissions defined in:
- **[ir_rules.xml](../website_crm_iap_reveal/security/ir_rules.xml)**

```mermaid
graph TB
    subgraph "Security Layers"
        A[Users] --> B[Groups]
        B --> C[Access Control Lists]
        C --> D[Models]
        B --> E[Record Rules]
        E --> F[Individual Records]
    end
```

Security files overview:
- **[ir.model.access.csv](../website_crm_iap_reveal/security/ir.model.access.csv)**
  - Model access permissions (CRUD rights)
- **[ir_rules.xml](../website_crm_iap_reveal/security/ir_rules.xml)**
  - Security groups, categories, and XML-based rules

Notes
- Access Control Lists define which groups can access which models
- Record Rules provide row-level security (filter records by user/group)
- Security groups organize users and define permission sets
- All security is enforced at the ORM level by Odoo
