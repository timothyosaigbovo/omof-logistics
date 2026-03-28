# Omofo Logistics — Full Stack Django Shipping Platform

A full-stack e-commerce web application built with Django for the Code Institute MS4 project. Omofo Logistics is a real logistics business platform where customers can request bespoke shipping quotes, negotiate pricing, pay securely via Stripe in multiple currencies, and track their shipments.

**Live site:** https://omof-logistics.onrender.com

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Strategy](#business-strategy)
- [User Stories](#user-stories)
- [Features](#features)
- [Data Models](#data-models)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Project Overview

Omofo Logistics offers freight forwarding, customs clearance, ocean and air freight, and e-commerce logistics services across Africa and beyond. Unlike standard e-commerce sites, pricing is bespoke — every shipment is different. This platform reflects that reality through a quote-negotiation-then-pay flow.

---

## Business Strategy

No prices are displayed on the site. Every customer submits a Request for Quote (RFQ). The admin reviews and issues a custom quote. Client and admin negotiate via a message thread. Once agreed, the client pays via Stripe in their chosen currency.

---

## User Stories

### Visitor
- Browse service descriptions without seeing prices
- Register for an account
- Read blog posts and testimonials
- Submit a contact form

### Authenticated Client
- Submit a Request for Quote with service, route, cargo, weight and urgency
- View all RFQs and their status on the dashboard
- Receive and view admin-issued quotes
- Negotiate price via a message thread
- Accept a quote and choose payment currency
- Pay securely via Stripe in GBP, USD, EUR, NGN, CAD or GHS
- Track shipment status via an animated timeline

### Admin
- View and manage all RFQs in Django admin
- Issue custom quotes with price, currency, validity and notes
- Reply to client negotiation messages
- Create shipments and add status updates

---

## Features

- **Quote request system** — clients submit detailed RFQs
- **Negotiation messaging** — threaded chat between client and admin
- **Multi-currency checkout** — Stripe PaymentIntent in 6 currencies
- **Shipment tracking** — animated timeline with status updates
- **Client dashboard** — live RFQ, order and shipment data
- **Blog** — published posts manageable via admin
- **Contact form** — saves messages to database
- **AWS S3** — media file storage in production
- **Allauth** — full authentication with email verification

---

## Data Models

### accounts
- UserProfile — extends User with company, phone, preferred currency

### services
- ServiceCategory — groups services by type
- Service — individual service with description and image, no price fields

### quotes
- QuoteRequest — client RFQ submission with status tracking
- Quote — admin-issued quote with price, currency and validity

### negotiations
- NegotiationMessage — threaded messages linked to a Quote

### checkout
- Order — confirmed payment record with Stripe payment intent ID

### tracking
- Shipment — linked to Order with tracking reference
- ShipmentUpdate — individual status update with location and timestamp

### blog
- BlogPost — published articles with image and author

### contact
- ContactMessage — contact form submissions

### reviews
- Testimonial — featured testimonials on home page

---

## Technologies Used

- **Python 3.12** / **Django 4.x**
- **PostgreSQL** — production database via Render
- **Stripe** — payment processing with multi-currency support
- **AWS S3** — media file storage via django-storages and boto3
- **Bootstrap 5** — responsive frontend framework
- **WhiteNoise** — static file serving
- **Gunicorn** — production WSGI server
- **Render** — cloud deployment platform
- **GitHub** — version control

---

## Testing

Run the test suite locally:

\\\ash
python manage.py test
\\\

Manual testing was performed on all pages, forms, and user flows including:
- Registration, login and logout
- RFQ submission and status updates
- Quote issuance and negotiation thread
- Currency selector on booking summary
- Stripe test payment (card: 4242 4242 4242 4242)
- Shipment tracking timeline
- Admin panel for all models

---

## Deployment

### Local setup

\\\ash
git clone https://github.com/timothyosaigbovo/omof-logistics.git
cd omof-logistics
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
\\\

Create a \.env\ file with:

\\\
SECRET_KEY=your-secret-key
DEBUG=True
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WH_SECRET=whsec_...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_STORAGE_BUCKET_NAME=omof-logistics-media
AWS_S3_REGION_NAME=eu-west-2
\\\

\\\ash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\\\

### Render deployment

The project deploys automatically via \ender.yaml\. Push to main branch triggers a new deploy.

Environment variables are set in the Render dashboard under the web service settings.

---

## Credits

- Code Institute — project framework and assessment criteria
- Stripe — payment processing documentation
- AWS — S3 storage documentation
- Bootstrap — frontend components
- Django documentation — models, views, authentication

---

## Acknowledgements

Special thanks to Code Institute for the project framework and to the open source community for the tools and libraries that made this project possible.

Project completed March 2026.
