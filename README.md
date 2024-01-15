# Vendor Management System API

A Vendor Management System(VMS) apis  for efficient vendor profile management, purchase order tracking, and vendor performance metrics calculation.

![Python version](https://img.shields.io/badge/Python-3.8.10-4c566a?logo=python&&longCache=true&logoColor=white&colorB=pink&style=flat-square&colorA=4c566a) ![Django version](https://img.shields.io/badge/Django-4.2.9-4c566a?logo=django&&longCache=truelogoColor=white&colorB=pink&style=flat-square&colorA=4c566a) ![Django-RestFramework version](https://img.shields.io/badge/Django_Rest_Framework-3.14.0-red.svg?longCache=true&style=flat-square&logo=django&logoColor=white&colorA=4c566a&colorB=pink) 


## Table of Contents

- [Core Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/VidhanCodiatic/Vendor-Management-System.git
   cd VendorManagementSystem
   ```
2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application at http://localhost:8000.

6. Access DRF ui for VMS http://localhost:8000/api/schema/swagger-ui/


## API Endpoints

Below is a summary of the available API endpoints:

**Users**

| Endpoint             | Method      | Description                           |
| -------------------- | ----------- | ------------------------------------- |
| `/api/users/`        | POST        | Create a new User.                    |


**Tokens**

| Endpoint             | Method      | Description                           |
| -------------------- | ----------- | ------------------------------------- |
| `/api/token/`        | POST        | Generate token for User.              |
| `/api/token/refresh` | POST        | Refresh token .                       |


**Vendor Profile Management**

| Endpoint             | Method      | Description                           |
| -------------------- | ----------- | ------------------------------------- |
| `/api/vendors/`      | POST        | Create a new vendor.                  |
| `/api/vendors/`      | GET         | List all vendors.                     |
| `/api/vendors/{id}/` | GET         | Retrieve a specific vendor's details. |
| `/api/vendors/{id}/` | PUT / PATCH | Update a vendor's details.            |
| `/api/vendors/{id}/` | DELETE      | Delete a vendor.                      |

**Purchase Order Tracking**

| Endpoint                                | Method       | Description                        |
| --------------------------------------- | ------------ | ---------------------------------- |
| `/api/purchase_orders/`                 | POST         | Create a purchase order.                       |
| `/api/purchase_orders/`                 | GET          | List all purchase orders.                      |
| `/api/purchase_orders/{id}/`            | GET          | Retrieve details of a specific purchase order. |
| `/api/purchase_orders/{id}/`            | PUT / PATCH  | Update a purchase order.                       |
| `/api/purchase_orders/{id}/`            | DELETE       | Delete a purchase order.                       |

**Vendor Performance Evaluation**

| Endpoint                                | Method | Description                              |
| --------------------------------------- | ------ | ---------------------------------------- |
| `/api/vendors/{vendor_id}/performance/` | GET    | Retrieve a vendor's performance metrics. |

**Additional Docs**

| Endpoint                  | Method | Description                                       |
| ------------------------- | ------ | ------------------------------------------------- |
| `/api/schema/`            | GET    | List all the api's documentation format.          |
| `/api/schema/redoc/`      | GET    | List all the api's detailed documentation format. |
