
# Vendor Management System with Performance Metrics

Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

## Run Locally

Clone the project

```bash
  git clone https://github.com/truptighadge/Vendor_Management_System
```

Go to the project directory

```bash
  cd Vendor_Management_System
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```
Visit http://127.0.0.1:8000/api in your web browser to access the application.

## API Reference

#### List all vendors

```http
  GET /api/vendors
```
#### Create a new vendor

```http
  POST /api/vendors
```

#### Retrieve a specific vendor's details

```http
  GET /api/vendors/{vendor_id}/
```

####  Update a vendor's details
```http
  PUT /api/vendors/{vendor_id}/
```

####  Delete a vendor.
```http
  DELETE /api/vendors/{vendor_id}/
```

#### Create a purchase order
```http
  POST /api/purchase_orders/
```

#### List all purchase orders
```http
  GET /api/purchase_orders/
```

#### Retrieve details of a specific purchase order
```http
  GET /api/purchase_orders/{po_id}/
```

####  Update a purchase order
```http
  PUT /api/purchase_orders/{po_id}/
```

####   Delete a purchase order
```http
  DELETE /api/purchase_orders/{po_id}/
```

####   vendors to acknowledge POs
```http
  POST /api/purchase_orders/{po_id}/acknowledge
```

####    Retrieve a vendor's performance metrics
```http
  GET /api/vendors/{vendor_id}/performance
```