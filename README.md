# E-Commerce Website

This repository contains the source code for a fully functional e-commerce website built with modern web technologies. The project is designed to provide a comprehensive platform for buying products online, featuring user authentication, product management, a shopping cart, order processing, and payment integration using Razorpay.

## Features

- **User Authentication:** Secure user registration and login.
- **Product Management:** Admin interface for adding, editing, and deleting products.
- **Shopping Cart:** Add, remove, and update products in the cart.
- **Order Processing:** Seamless order placement and tracking.
- **Payment Integration:** Secure payment gateway integration with Razorpay.
- **PDF Invoice Generation:** Generate and download order invoices in PDF format.

## Technologies Used

- **Backend:** Django, Django Rest Framework
- **Frontend:** HTML, CSS, JavaScript (with Django templates)
- **Database:** SQLite (or other Django-supported databases)
- **Payment Gateway:** Razorpay
- **PDF Generation:** xhtml2pdf

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.12.0 installed
- Django installed
- Razorpay account for payment integration

### Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-website.git
cd ecommerce-website
### Usage
Admin Interface:
Navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials.
Add products through the admin interface.

User Registration and Login:
Register a new account or log in with existing credentials.

Product Browsing:
Browse through the available products on the homepage.

Shopping Cart:
Add products to the shopping cart.

Checkout:
Proceed to checkout, enter payment details, and place the order.

PDF Invoice:
After successful payment, generate and download the order invoice in PDF format.

Project Structure
plaintext
ecommerce-website/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── core/
│   │   │   ├── index.html
│   │   │   ├── orderlist.html
│   │   │   ├── add_product.html
│   │   │   ├── product_desc.html
│   │   │   ├── checkout_address.html
│   │   │   ├── paymentsummaryrazorpay.html
│   │   │   ├── paymentfailed.html
│   │   │   └── invoice.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ecommerce_website/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
### API Endpoints
Home: GET /
Order List: GET /orderlist
Add Product: GET /add_product and POST /add_product
Product Description: GET /product/<int:pk>
Add to Cart: POST /add_to_cart/<int:pk>
Add Item: POST /add_item/<int:pk>
Remove Item: POST /remove_item/<int:pk>
Checkout: GET /checkout and POST /checkout
Payment: POST /payment
Handle Payment Request: POST /handlerequest
Render PDF Invoice: GET /render_pdf_view

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### Acknowledgements
Django
Razorpay
xhtml2pdf


This `README.md` file provides a comprehensive guide for anyone looking to understand, install, and contribute to your e-commerce website project. Adjust the sections as necessary to better reflect your project's specifics and any additional information you might want to include.

