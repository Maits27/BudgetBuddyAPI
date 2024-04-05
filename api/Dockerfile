FROM python:3.10

WORKDIR /budgetbuddy_api

RUN pip install --upgrade pip

COPY requirements.txt /budgetbuddy_api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /budgetbuddy_api/requirements.txt

COPY ./app /budgetbuddy_api/app
COPY ./images /budgetbuddy_api/images

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]