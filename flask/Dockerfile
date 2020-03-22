FROM python:3.8-alpine

RUN apk add py-pip
RUN pip3 install Flask-Cors
RUN pip3 install mysql-connector

# Nastavenie pracovného adresára kontajnera
WORKDIR /app

# Inštalácia  závislostí aplikácie
RUN pip install flask

# Kopírovanie aplikácie súborov do obrazu
COPY ./app.py /app

# Nastavenie premennej prostredia
ENV FLASK_APP app.py

# Program na spustenie
ENTRYPOINT [ "flask" ]
# Argumenty 
CMD ["run", "--host", "0.0.0.0"]