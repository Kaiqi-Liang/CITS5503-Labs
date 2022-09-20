# Practical Worksheet 6

## Create an EC2 instance

Create an EC2 micro instance using Ubuntu and SSH into it.

![update](images/update.png)
![upgrade](images/upgrade.png)
![venv](images/venv.png)
![pip](images/pip.png)

Create a directory with the path `/opt/wwc/mysites` and `cd` into that.

Set up a virtual environment and activate it.

Install `django` and use it to create a project and an app called `polls`.

![django](images/django.png)

## Install and configure nginx

Install `nginx`.

![nginx](images/nginx.png)

Edit `/etc/nginx/sites-enabled/default` and restart `nginx`.

Run the server in the `/opt/wwc/mysites/lab` directory.

![run server](images/runserver.png)

Go to a browser now and use the IP address of the ec2 instance.

![browser](images/browser.png)

## Changing the code

Following the steps outlined in the lecture, edit the following files then rerun the server.

![edit](images/edit.png)

Go to a browser again and add `/polls/` at the end of the URL.

![instance](images/instance.png)

## Adding the load balancer

Create an application load balancer.

![load balancer](images/balancer.png)

For the target group, in the health check, specify `/polls/` for the path.

![health check](images/health.png)

Add the instance as a registered target.

![target](images/target.png)

Go to the browser again and change the instance public IP address in the URL to the load balancer DNS name.

![dns name](images/lb.png)

Health check is fetching the `/polls/` page every 30 seconds.

![server](images/server.png)

## Web interface for CloudStorage application

Set up aws cli in the instance.

![awscli](images/awscli.png)
![configure](images/configure.png)

Create a local version of DynamoDB.

![scp](images/scp.png)
![unzip](images/unzip.png)

Run DynamoDB locally on port 5000.

![run DynamoDB](images/run.png)

Open another terminal and scp `lab3.py` into the instance then `pip install boto3` so that `lab3.py` can be run to populate the DynamoDB that i runs running in the same instance.

![lab3.py](images/lab3.png)
![boto3](images/boto3.png)

Scan the table to check that data has been populated successfully.

![scan1](images/scan1.png)
![scan2](images/scan2.png)

Create a `templates` directory under `polls` and then add to the `TEMPLATES` section of `lab/settings.py`.

![templates](images/templates.png)

In the templates directory, add a file `files.html`.

![files.html](images/files.png)

Render the template in `views.py`.

![views.py](images/views.png)

Refresh the load balancer page on the browser.

![table](images/table.png)

Delete the load balancer.

![delete](../lab5/images/delete.png)
