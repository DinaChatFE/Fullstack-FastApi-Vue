<p align="center" style="margin-bottom: 40px"><a href="https://laravel.com" target="_blank"><img src="https://staging.z1mobile.com/assets/Zillennium-logo.png" width="400"></a></p>


# About Project

The event news project is a project feature that was intended to make it easier to manage, produce, and register events in a matter of minutes.
The disadvantage of not using this project is that individuals will go to a certain location and register by hand. They may have taken their time to arrive and spent money on transportation. etc.. 
# Project Structure
- Create and Update List News, Event on admin panel including some feature in web client 
- Admin could manage whole system
- Admin could see the report
- User could register there interested event

# Tool Using 
* Fast API: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* Vue: is a JavaScript framework used to create user interfaces. It is built on top of conventional HTML, CSS, and JavaScript and provides a declarative and component-based programming approach that allows you to rapidly construct basic or sophisticated user interfaces.

# Pre requirement

- database / postgresql
- npm install node v14.*
- pip 21.*
- python v3.*


# Installation
   * The root directory has three primary folders, the first of which represents the back end. The first folder contains the API that connects to the database, while the second and third folders include the Vue framework, which represents the front end for both admin and clients.
   * Install postgres
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
    * Install app
        - backend: go to Back-End folder or command cd Back-End
        - run command: 
            ```
                python3 -m venv env #in mac
                py -m venv env # in window
                # It use to generate folder environment that use only in its sub folder

                # activate venv
                source env/bin/activate # in mac
                .\env\Scripts\activate $ in window

                pip install -r requirement.txt
                # install all package that's been using in the app
            ```
        - run 
            ```
                uvicorn main:app --reload 
                # serve the app
            ```    
        - Front end: 
            Go to individual folder (Front-End-Admin, Front-End-Client) And install by command
            ```
                npm install
            ```
            Run it by command
             ```
                npm run serve
             ```
                