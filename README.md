# Apollo

Learning platform

## Project Requirements:

In order to get the project running you need to install:

* docker

#### Install Docker:

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

[Get Docker](https://docs.docker.com/get-docker/).

## Setting the Project Locally:

#### Cloning the project:

Once you have all the needed requirements installed, clone the project:

``` bash
git clone https://github.com/er5bus/apollo-back.git
```

#### Configure .env file:

Before you can run the project you need to set the envirment varibles:

``` env
$ cp .env.example .env
```

#### Run the Project:

to run the project type:

``` bash
docker-compose up --build -d
```

1. Initialize base DB-schema**

```bash
$ aerich init-db # inside the container
```

**2. Create superuser**

```bash
$ ./bin/createsuperuser  # inside the container
```

**(3. Optional: Generate fake data)**

```bash
$ ./bin/fakedata  # inside the container
```

## Migrations

1. Create migrations after initializing new models / changing existing models
```bash
aerich migrate # inside the container
```

2. Apply migrations
```bash
aerich upgrade  # inside the container
```

Check 0.0.0.0:5000 on your browser!

That's it.
