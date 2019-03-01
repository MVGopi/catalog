# Item-Catalog Web APPLICATION
By Venkata Gopi This web app is a project for the Udacity FSND Course.

#About
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates mobile categories and their specifications. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

#In This Project
This project has one main Python module mobiles_store.py which runs the Flask application. A SQL database is created using the mobiles_database_setup.py module and you can populate the database with test data using mobile_data_insertion.py. The Flask application uses stored HTML templates in the templates folder to build the front-end of the application.

#Skills Required
1.Python
2.HTML
3.CSS
4.OAuth
5.Flask Framework

#Installation
There are some dependencies and a few instructions on how to run the application. Seperate instructions are provided to get GConnect working also.

#Dependencies
1.Vagrant-->https://www.vagrantup.com/

2.Udacity Vagrantfile-->https://github.com/udacity/fullstack-nanodegree-vm

3.Virtual Box-->https://www.virtualbox.org/wiki/Downloads

#How to Install
1.Install Vagrant & VirtualBox
2.Clone the Udacity Vagrantfile
3.Go to Vagrant directory and either clone this repo or download and place zip here
4.Launch the Vagrant VM (vagrant up)
5.Log into Vagrant VM (vagrant ssh)
6.Navigate to cd /vagrant as instructed in terminal
7.The app imports requests which is not on this vm. Run pip install requests
Or you can simply Install the dependency libraries (Flask, sqlalchemy, requests,psycopg2 and oauth2client) by running pip install -r requirements.txt

7.Setup application database python /Item-Catalog/mobiles_database_setup.py
8.Insert sample data python /Item-Catalog/mobiles_data_insertion.py
9.Run application using python /Item-Catalog/mobiles_store.py
10.Access the application locally using http://localhost:8888

#Using Google Login
To get the Google login working there are a few additional steps:

1.Go to Google Dev Console-->https://accounts.google.com/ServiceLogin/signinchooser?service=cloudconsole&passive=1209600&osid=1&continue=https%3A%2F%2Fconsole.developers.google.com%2F%3Fref%3Dhttps%3A%2F%2Fgithub.com%2FSkBadulla%2FItem_Catalog&followup=https%3A%2F%2Fconsole.developers.google.com%2F%3Fref%3Dhttps%3A%2F%2Fgithub.com%2FSkBadulla%2FItem_Catalog&flowName=GlifWebSignIn&flowEntry=ServiceLogin

2.Sign up or Login if prompted

3.Go to Credentials

4.Select Create Crendentials > OAuth Client ID

5.Select Web application

6.Enter name 'Book-Store'

7.Authorized JavaScript origins = 'http://localhost:8888'

8.Authorized redirect URIs = 'http://localhost:8888/home' && 'http://localhost:8888/index'

9.Select Create

10.Copy the Client ID and paste it into the data-clientid in login.html

11.On the Dev Console Select Download JSON

12.Rename JSON file to client_secrets.json

13.Place JSON file in book-store directory that you cloned from here

14.Run application using python /Item-Catalog/mobiles_store.py

#JSON Endpoints

company/1/JSON--->displays the details of mobile company like name,icon

mobile/1/JSON--->displays the details of particular mobile like name,price,ram,rom,cam
