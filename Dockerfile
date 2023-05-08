# Fetching official base image for python
FROM python:3.10-alpine as base

# Setting up the work directory
WORKDIR /home/app/

# Preventing python from writing pyc to docker container
ENV PYTHONDONTWRITEBYTECODE 1

# Flushing out python buffer
ENV PYTHONUNBUFFERED 1

# Update os packages
RUN apk update && apk upgrade

# Install required os packages
RUN apk add --no-cache bash\
                       pkgconfig \
                       git \
                       gcc \
                       openldap \
                       libcurl \
                       python3-dev \
                       libpq-dev \
                       gpgme-dev \
                       libc-dev \
                       curl \
    && rm -rf /var/cache/apk/*

# Upgrade pip
RUN pip install --upgrade pip

# Add requirements file
COPY ./requirements.txt ./

# Install dependencies
RUN pip install -U --no-cache-dir -r ./requirements.txt

# Apparently, Alpine Linux does not support installing scikit-learn using pip
RUN apk add py3-scikit-learn

# Install NumPy
RUN apk add py3-numpy 

# Install Pandas
RUN apk add py3-pandas

# Add code to interpret in container
COPY ./fast_foods_app ./fast_foods_app/
COPY ./ml_demo_fast_foods ./ml_demo_fast_foods/
COPY ./manage.py ./

# List added files
RUN ls -al

# Expose port
EXPOSE 8000

# Run server
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
