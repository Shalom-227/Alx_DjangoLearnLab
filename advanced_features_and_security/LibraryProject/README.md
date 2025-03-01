Django Application Access Control

## Permissions Defined:
- `can_view`: View articles
- `can_create`: Create new articles
- `can_edit`: Edit existing articles
- `can_delete`: Delete articles

## User Groups:
- **Admins**: Can view, create, edit, and delete articles.
- **Editors**: Can view, create, and edit articles.
- **Viewers**: Can only view articles.

## Setup:
1. Migrate the models.
2. Create groups in the admin interface.
3. Assign permissions to groups.
4. Assign users to these groups.


# Security Features in Django Project

## Key Security Measures Implemented:

1. **CSRF Protection**: All forms include CSRF tokens using `{% csrf_token %}` to prevent CSRF attacks.
2. **SQL Injection Protection**: All database queries use Django's ORM to ensure queries are parameterized and protected from SQL injection.
3. **Content Security Policy (CSP)**: A restrictive CSP is enforced to prevent unauthorized content from being loaded.
4. **Secure Cookies**: CSRF and session cookies are set to be secure (only sent over HTTPS).
5. **HSTS and SSL**: The site is configured to enforce HTTPS with HSTS headers to protect from man-in-the-middle attacks.

## Testing:
1. Test CSRF tokens in form submissions.
2. Test input fields for XSS attacks by attempting to inject JavaScript code.
3. Test form submission and data retrieval for SQL injection vulnerabilities.
