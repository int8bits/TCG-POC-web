FROM python:3.12-slim

RUN apt-get update && apt upgrade -y && apt autoclean && apt autoremove -y

# Set the working directory
WORKDIR /opt/app

# Copy the current directory contents into the container at /opt/app
COPY . /opt/app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade --user pip --no-cache-dir
RUN pip install --user --no-cache-dir pipenv
RUN pipenv install --deploy --ignore-pipfile

# Make port 8000 available to the world outside this container
EXPOSE 8000

# migrate the database
RUN pipenv run python manage.py migrate

# Run django app
# CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
