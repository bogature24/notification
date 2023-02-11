# # # FROM python:3.9
# # #
# # # ENV PYTHONUNBUFFERED 1
# # #
# # # EXPOSE 8000
# # #
# # # RUN mkdir /app
# # # WORKDIR /app
# # #
# # # COPY requirements.txt /app/
# # # RUN pip install -r requirements.txt
# # #
# # # COPY . /app/
# # #
# # # CMD celery -A notification worker -l info
# #
# # # FROM python:3.8
# # #
# # # ENV PYTHONUNBUFFERED 1
# # #
# # # WORKDIR /app
# # #
# # # COPY requirements.txt .
# # #
# # # RUN pip install -r requirements.txt
# # #
# # # COPY . .
# # #
# # # CMD gunicorn notification.wsgi:application --bind 0.0.0.0:8000
# #
# # FROM python:3.8
# #
# # ENV PYTHONUNBUFFERED 1
# #
# # WORKDIR /app
# #
# # COPY requirements.txt .
# #
# # RUN pip install -r requirements.txt
# #
# # COPY . .
# # # Expose the default Nginx port
# # EXPOSE 80
# #
# # # Copy the Nginx configuration file to the container
# # COPY nginx.conf /etc/nginx/nginx.conf
# #
# # # Start the Nginx server and run the Gunicorn server
# # CMD ["nginx", "-g", "daemon off;"]
#
# # Use an existing image as the base image
# # FROM python:3.8-alpine
# #
# # # Set the working directory in the container
# # WORKDIR /app
# #
# # # Copy the requirements file to the container
# # COPY requirements.txt /app/
# #
# # # Install the required packages
# # RUN pip install --no-cache-dir -r requirements.txt
# #
# # # Copy the rest of the application files to the container
# # COPY . /app/
# #
# # # Run the collectstatic command to gather static files
# # RUN python manage.py collectstatic --no-input
# #
# # # Expose the default Nginx port
# # EXPOSE 80
# #
# # # Copy the Nginx configuration file to the container
# # COPY nginx.conf /etc/nginx/nginx.conf
# #
# # # Start the Nginx server and run the Gunicorn server
# # CMD ["nginx", "-g", "daemon off;"]
#
# FROM python:3.8
#
# ENV PYTHONUNBUFFERED 1
#
# WORKDIR /app
#
# COPY requirements.txt .
#
# RUN pip install -r requirements.txt
#
# COPY . .
#
# CMD gunicorn notification.wsgi:application --bind 0.0.0.0:8000
#
# EXPOSE 80
#
# COPY ./nginx.conf /etc/nginx/nginx.conf

# FROM python:3.8.5-alpine
#
# RUN pip install --upgrade pip
#
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
#
# COPY ./notification /app
#
# WORKDIR /app
#
# COPY ./entrypoint.sh /
# ENTRYPOINT ["sh", "/entrypoint.sh"]

FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY swap-face.xyz.cert /etc/nginx/certificate.cert
COPY swap-face.xyz.key /etc/nginx/certificate.key
COPY static .

# CMD gunicorn notification.wsgi:application --bind 0.0.0.0:8000
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]