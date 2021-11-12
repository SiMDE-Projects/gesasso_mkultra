ARG BASE=builder
#
#FROM node:alpine as front_builder
#WORKDIR /code
#
#ARG NODE_ENV=production
#ENV NODE_ENV=${NODE_ENV}
#ADD package.json /code/package.json
#RUN yarn install
#ADD . /code
#RUN yarn build

FROM python:3.8-buster AS builder
MAINTAINER Cesar Richard <cesar.richard2@gmail.com>

ENV PYTHONUNBUFFERED 1

# Setup working directory
RUN mkdir -p /code /home/gesasso/.ssh /static
WORKDIR /code

# Setup user
RUN groupadd -r gesasso && useradd -r -g gesasso gesasso

# Install tmate for shells
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev --no-install-recommends && rm -r /var/lib/apt/lists/*

# Setup SSH KEY for tmate
RUN ssh-keygen -b 2048 -t rsa -f /home/gesasso/.ssh/id_rsa -q -N ""
RUN chown gesasso:gesasso -R /home/gesasso

# Install uwsgi
RUN pip install --no-cache-dir uwsgi

# Install gesasso requirements (doing this before copying code improves caching)
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Uwsgi runs on port 8003
EXPOSE 8003

#COPY --from=front_builder /code/node_modules.bin.txt /code/node_modules.bin.txt

# Add code
ADD . /code/

# Collect static files
RUN GESASSO_DJANGO_SECRET=whatever python manage.py collectstatic --noinput --clear

# Switch to unprivileged user
USER gesasso

# Run uwsgi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
