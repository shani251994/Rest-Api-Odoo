# Partner REST API for Odoo

This module provides a simple, public REST API for managing customers (`res.partner`) in Odoo.  
It allows external systems to **create**, **update**, **delete**, and **fetch** customer records without authentication.

> ⚠️ This API is **public** and has no authentication — use it in a **secure environment** only (e.g., behind a firewall or local network).

---

## 🔧 Installation

1. Copy the module folder (e.g., `rest_partner_api/`) to your Odoo `addons/` directory.
2. Update the app list in Odoo.
3. Install the module via Apps menu.

---

## 📡 API Endpoints

All endpoints accept and return `application/json`.

| Method | Endpoint                    | Description                  |
|--------|-----------------------------|------------------------------|
| `POST` | `/partner/create`           | Create a new customer        |
| `PUT`  | `/partner/update/<id>`      | Update a customer by ID      |
| `DELETE` | `/partner/delete/<id>`    | Delete a customer by ID      |
| `GET`  | `/partner/<id>`             | Fetch customer by ID         |
| `GET`  | `/partner/all`              | Fetch all customers          |

---

## 📤 Request Examples

### ➕ Create a Customer

`POST /partner/create`

```json
{
  "name": "Ali Zer",
  "email": "ali@example.com",
  "phone": "1234567890"
}
