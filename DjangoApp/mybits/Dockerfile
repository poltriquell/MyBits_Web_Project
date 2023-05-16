# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install environt variables
COPY key.env /app/
ENV SECRET_KEY=$SECRET_KEY
ENV DATABASE_URL=$DATABASE_URL

RUN apt-get update && apt-get install -y curl gnupg

# Descarga y agrega la clave GPG para la fuente de Google Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

# Agrega la fuente de Google Chrome al archivo de fuentes del sistema
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Actualiza la lista de paquetes e instala Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable


# Install pip requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 1000 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENV SECRET_KEY=$SECRET_KEY

# Run the migrations
RUN python3 data_fill.py
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found. Please enter the Python path to wsgi file.
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pythonPath.to.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD [ "bash", "./djangoStart.sh" ]