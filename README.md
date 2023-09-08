# Producer - Consumer
Мікросервіс “Producer - Consumer” на основі технологій Django + PostgreSQL + Celery.
Завдання полягає в тому, щоб створити простий сервіс, в якому Celery один раз на хвилину кластиме в модель запис, а через деякий час юзеру потрібно буде видаляти ці записи з таблиці в браузері, натискаючи на відповідну кнопку.


## Installing using GitHub:
Install PostgresSQL and create db

1. Clone the repository:

```bash
git clone https://github.com/your-username/producer_consumer
```
2. Change to the project's directory:
```bash
cd producer_consumer
```
3. Сopy .env_sample file with your examples of env variables to your .env
file


4. Once you're in the desired directory, run the following command to create a virtual environment:
```bash
python -m venv venv
```
5. Activate the virtual environment:

On macOS and Linux:

```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Set up the database:

Run the migrations

```bash
python manage.py migrate
```

6. Start the development server

```bash
python manage.py runserver
```

7. Access the website locally at http://localhost:8000.

## Run with Docker

Docker should be installed

```
docker-compose up --build
```

## Getting access

 
```
username = admin
password = admin123123
```

Change in users models telegram_id field with your telegram id for test teelgram notification