# this was my current python version. May need to be adjusted at later time as dependencies are added
FROM python:3.8.5


# set the working directory to app
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# install python dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]