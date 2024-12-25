# todoist_to_postgres
This project is to get data from [Todoist](https://www.todoist.com) to a Postgres database. 

This is a project for me to learn with. Don't expect anything big here.

## Setup
1. Get a postgres database up and running. Could use [the official Docker](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/).
    1. Need to configure user and tables    
2. Configure a .env file like env.example
3. Run `python todoist_to_postgres.py` in main directory