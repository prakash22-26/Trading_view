# 📌 TV IB Project – Django Trading with Interactive Brokers

## 🔍 Overview

TV IB Project is a backend application built with Django that integrates with the Interactive Brokers (IB) API.
It provides REST API endpoints to place, track, and manage trades, while storing information in a database.

This code is a foundation for building a trading automation system or integrating with a frontend dashboard.

## ⚙️ Requirements

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (default database, can be switched to PostgreSQL/MySQL)
- Virtualenv (recommended)
- Interactive Brokers API / ib_insync (if used in ib.py)

## 🚀 Installation & Setup

### Clone the repository

```
git clone <repo-url>
cd tv_ib_project
```

### Create & activate a virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### Install dependencies

```
pip install -r requirements.txt
```

If no requirements.txt exists:

```
pip install django djangorestframework
```

### Set up environment variables

Create a `.env` file in the root folder:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
IB_API_KEY=your_ib_api_key
```

### Apply database migrations

```
python manage.py migrate
```

### Run the development server

```
python manage.py runserver
```

Access the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## ▶️ Usage

Once the server is running, you can use the provided REST API endpoints to interact with Interactive Brokers.

Some possible features include: Placing Buy/Sell orders

Checking order status Managing and storing trade history Extending with portfolio tracking or market data feeds

Example (pseudo API usage):

```
curl -X POST http://127.0.0.1:8000/trading/order/      -H "Content-Type: application/json"      -d '{"symbol": "AAPL", "action": "BUY", "quantity": 10}'
```

## 📂 Project Structure

```
tv_ib_project/
│── manage.py              # Django management script
│── db.sqlite3             # Default SQLite database
│── .env                   # Environment variables
│
├── tv_ib_project/         # Main Django config
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL routing
│   ├── wsgi.py            # WSGI entry point
│   └── asgi.py            # ASGI entry point
│
└── trading/               # Trading app
    ├── models.py          # Database models
    ├── views.py           # API views (endpoints)
    ├── serializers.py     # DRF serializers
    ├── urls.py            # App-level routes
    ├── ib.py              # Interactive Brokers integration logic
    └── admin.py           # Django admin integration
```

## 🧪 Testing

```
python manage.py test
```

## 💡 What You Can Do With This Code

- Run a local backend service for trading with IB.
- Use REST APIs to buy/sell stocks or manage trades.
- Extend it into a fully automated trading system.
- Connect it to a React / Angular / Vue frontend for dashboards.
- Replace SQLite with PostgreSQL/MySQL for production use.

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it with attribution.
