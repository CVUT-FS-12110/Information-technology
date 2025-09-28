# Server for SSH connection testing

Build and run the container:

> docker-compose up --build -d

## Student workflow

Connect as student:

> ssh student@localhost -p 2222

Run script:

> runner <YourName>

## Teacher workflow

Connect as teacher:

> ssh teacher@localhost -p 2222

Run teacher script:

> python3 teacher_report.py


## Troubleshooting

SSH error after rebuild - remove the known key:

> ssh-keygen -R "[localhost]:2222"