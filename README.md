# MyBits_Web_Project

# Introduction
This project contains the backend for the MyBits App that was used in Web Project subject in [Computer Science Engineering](https://grauinformatica.udl.cat/en) at [Universitat de Lleida (UdL)](https://www.udl.cat/ca/en/).

# Project Idea
Our proposed project is a web-based application that enables registered users to showcase their restaurants and allows other users to review them. In essence, it is a platform that connects restaurant owners with potential customers.

The primary goal of our project is to develop a comprehensive understanding of how web-based applications work, specifically those that relate to the food industry.

To put it simply, our plan is to create a website where restaurant owners can register and promote their businesses, while users can share their reviews and experiences. This project will help us learn how to develop web applications that cater to the food industry.

# How to run the web application with Docker
If you have an application that you want to run, one way to do it is with Docker. Docker is a tool that allows you to package your application and all its dependencies into a container, which can then be run on any system that has Docker installed.

Here are the steps to follow to run an application with Docker:

## Step 1: Install Docker
The first step is to install Docker on your system. Docker is available for Windows, macOS, and Linux, so make sure you download the appropriate version for your operating system. You can download Docker from the official website:
[www.docker.com](https://www.docker.com/products/docker-desktop)

## Step 2: Write a Dockerfile
The next step is to write a Dockerfile. A Dockerfile is a text file that describes the steps needed to build a Docker image. The Docker image is a packaged version of your application and its dependencies.
Here's our Dockerfile content:
```
FROM python:3.10-slim
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
RUN adduser -u 1000 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
This Dockerfile uses Python as the base image, installs the dependencies listed in requirements.txt, copies the application code into the container, and specifies the command to run the application.

## Step 3: Create a docker-compose.yml file
Create a file named **_docker-compose.yml_** in the root directory of your project. This file is used to define and configure the containers that make up your application. Here's is our **_docker-compose.yml_** file content for our application:
```
version: '3.4'

services:
  db:
    image: postgres
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: mydatabaseuser
      POSTGRES_PASSWORD: mypassword
  djangoapp:
    image: djangoapp
    build:
      context: .
      dockerfile: ./Dockerfile
    ports:
      - 8000:8000
    depends_on:
      - db
    env_file:
      - key.env
      
  nginx:
    image: nginx
    ports:
      - 80:80
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - djangoapp
```
This **_docker-compose.yml_** file defines three services (db, djangoapp, and nginx) that are interconnected. The db service is used to store data, while the djangoapp service runs a Django web application that depends on the db service. The nginx service acts as a reverse proxy that forwards HTTP requests from port 80 to the djangoapp service running on port 8000.

## Step 4: Start the containers
To start the containers, open a terminal window in the root directory of your project and run the following command:
```
docker-compose up
```
The **_docker-compose up_** command will build the Docker image if it doesn't already exist, and then start the container.

## Step 5: Access the application
Once the containers are running, you can access the application by opening a web browser and navigating to **_https://localhost:8000_**. You should see your Python application running in the browser.

That's it! You've successfully run your Python application as a Docker container orchestration using docker-compose.

# How to run the web application in Fly.io

## Step 1: Sign up for a Fly.io Account
Before you start, make sure you have signed up for an account on Fly.io.

## Step 2: Install the Flyctl CLI Tool

You'll need the Flyctl CLI tool to deploy your application. Install it on your local machine by following the instructions provided on the Fly.io website.

## Step 3: Create a New Fly.io Application
Create a new Fly.io application using the Flyctl CLI tool. You can do this by running the following command in your terminal:
```
flyctl apps create <APP-NAME>
```
Replace **_<APP-NAME>_** with a name of your choice.

## Step 4: Navigate to Your Docker Compose File
Navigate to the directory where your **_docker-compose.yml_** file is located.

## Step 5: Deploy Your Application
Use the Flyctl CLI tool to configure your Fly.io application to use your Docker Compose file. You can do this by running the following command:
```
flyctl deploy
```

## Step 6: Access Your Application
Once the deployment is complete, you can access your application by using the URL provided by Fly.io. Open your web browser and enter the URL to view your application.

That's it! You have now successfully deployed your Docker Compose application to Fly.io.

# Built With

* [Django](https://www.djangoproject.com/) - The web framework used.
* [Docker](https://www.docker.com/) - Container management.
* [Fly.io](https://fly.io/) - Cloud Application Platform.
* [PostgreSQL](https://www.postgresql.org/) - Open Source Database.
* [Travis](https://travis-ci.org/) - Test CI.
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) - For more crispy forms.
* [Bootstrap 4](https://getbootstrap.com/) - A pretty css.

# Teachers
The teachers who have guided this project are:
- [Carles Mateu](https://github.com/carlesm)
- [Roberto Garcia](https://github.com/rogargon)

# Authors

* [Àlex Codina Braceros](https://github.com/Codinab)
* [Mario Fernández Rodríguez](https://github.com/marioferro2002)
* [Adrián Sanz Fernández](https://github.com/adriansanzzzz)
* [Enric Tobeña Casanovas](https://github.com/Enric-Tobena)
* [Pol Triquell Lombardo](https://github.com/poltriquell)

# License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details
