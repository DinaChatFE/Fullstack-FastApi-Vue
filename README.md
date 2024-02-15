# Get started

## About

The event news project is a project feature that was intended to make it easier to manage, produce, and register events in a matter of minutes.
The disadvantage of not using this project is that individuals will go to a certain location and register by hand. They may have taken their time to arrive and spent money on transportation. etc.. 
## Project Structure
- Create and Update List News, Event on admin panel including some feature in web client 
- Admin could manage whole system
- Admin could see the report
- User could register there interested event

## Tools 
- **Fast API**: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Vue**: is a JavaScript framework used to create user interfaces. It is built on top of conventional HTML, CSS, and JavaScript and provides a declarative and component-based programming approach that allows you to rapidly construct basic or sophisticated user interfaces.

## Pre requirement

- database / postgresql
- npm install node v14.*
- pip 21.*
- python v3.*

## Installation (Docker & Docker compose)
In the nested directory we're going to see the Dockerfile, Ex: `/Back-End/Dockerfile`. It's possible that we can run it individually using below command
> Example running Backend code
```bash
# cd to current directory
cd Back-End
# Build an image
docker build . -t [DOCKER-IMAGE-NAME]
# Run docker on port 8000, as default inner contianer it ran on port 8000, but we can expose outside using port 8001
docker run [DOCKER-IMAGE-NAME] --name my-docker-process-container -d -p 8001:8000
# -d for detach mode
```
If we ran individual, we have to setup our required process such as database, web server

> ! We can instead running all in one by using `docker compose`

Look at the root directory, we're going to see docker compose file. we're having 4 services.
1. frontend-admin
2. frontend-client
3. backend-python
4. postgres (database)
   
In order to run these 4 containers, we can command the belows:
```bash
# Using docker compose command
# Make sure you are in root directory
docker compose up -d --build
# This above will create it's own container and connect it using network we specify
```

So now we can access those 3 websites, by access these 3 port
1. Backend http://localhost:8082
2. Frontend client http://localhost:3002
3. Frontend Admin http://localhost:3003

## Installation ( Individual machine )
   * The root directory has three primary folders, the first of which represents the back end. The first folder contains the API that connects to the database, while the second and third folders include the Vue framework, which represents the front end for both admin and clients.
#### Install postgres
- On the mac (has brew install), command a few
 ```
brew doctor
brew update
 ```
In your command-line run the command: 
 ```
brew install postgres
```
Run the command: ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
```
alias pg_start="launchctl load ~/Library/LaunchAgents"
alias pg_stop="launchctl unload ~/Library/LaunchAgents"
```
Run the command: 
```
createdb `event_news_project # Database name
```
On window you can install [pgadmin4](https://www.pgadmin.org/download/) as your app current
#### Running web server
- For backend
- go to Back-End folder or command `cd Back-End`
- run command: 
```
 python3 -m venv env #in mac
 py -m venv env # in window
# It use to generate folder environment that use only in its sub folder
```
##### Activate venv
```
source env/bin/activate # in mac
.\env\Scripts\activate $ in window
```
##### Install all package which require in the project
- run
```
- pip install -r requirement.txt
```
- Serve web browser
```
 uvicorn main:app --reload
```
##### Serve Fronend (Vue js app)
- Go to individual folder (Front-End-Admin, Front-End-Client) And install by command
```
  npm install
```
- Run it by command
```
  npm run serve
```
> Note: all the frontend using vue js, must be installed by node js 14, specified by [Pre-requirement](#pre-requirement)
