# Sample Flask App

## Functionalities

- Validates and saves user details.
- Retrieves all user details.
- Fetches information for a specific user.
- Handles exceptional cases.

## Installation

The app requires certain dependencies and a database connection to be successfully installed and run. Follow these steps to install it:

### Downloading the Code

Clone the app using the following command:
```bash
git@github.com:Jitendra1mp4/step-tech-flask.git
```
But if you are in branch other then main then use following command to clone the repo
```bash
git clone -b mybranch --single-branch git@github.com:Jitendra1mp4/step-tech-flask.git
```
like for steptech_assignment branch it would be

```bash
 git clone -b steptech_assignment --single-branch git@github.com:Jitendra1mp4/step-tech-flask.git
```

- ### Creating a Virtual Environment (Optional but Recommended)
 It is recommended to create a virtual environment. To do this, first install virtualenv:

```bash
cd step-tech-flask
pip install virtualenv
```
To create a virtual environment, run:

```
python -m venv <virtual_environment_name>
```

Now activate the virtual environment:
 - In windows 

```
.\<virtual_environment_name>\Scripts\activate.bat  # in CMD
.\<virtual_environment_name>\Scripts\Activate.ps1  # in Powershell

```


 - In Linux/Unix/Mac 

```
source <virtual_environment_name>/bin/activate
```


- ### Installing Dependencies

All the dependencies, such as `flask, flask-mysqldb, flask-wtf, wtf-form email-validator` etc., are listed in the 'requirements.txt' file.

Install all dependencies using the command:

```
pip install -r requirement.txt
```
## Setting up Database 

####  Before running the app, it's important to set up the database. Follow these steps:

- Run the MySQL server and create a database named sampleapp.
- Import sampleApp/assets/sampleapp.sql using tools like phpMyAdmin (XAMPP), MySQL Workbench, or manually execute the queries from the sampleApp/assets/sampleapp.sql file.

- Once the queries are executed successfully, you can run the app.

- Set following database variable in `__init__.py` like bellow :

```python
app.config['MYSQL_HOST'] = 'localhost' # your db host
app.config['MYSQL_USER'] = 'root'      # your db username
app.config['MYSQL_PASSWORD'] = ''      # your db  password 
app.config['MYSQL_DB'] = 'sampleApp'   # your database name
```
## Running the App 
before running the app using following command please insure that MySQL server is started.
Use the following command to run the app:

```
python run.py
```

This command will provide a URL (usually http://127.0.0.1:5000/) for the app. If the code executes successfully, paste the URL into your browser and enjoy the app!


# Database Schema
The database named as `sampleapp` should have users table with as following structure.

```sql
  `id` int(11) Primary  NOT NULL AUTO_INCREMENT,
  `name` varchar(35) NOT NULL,
  `email` varchar(25) NOT NULL,
  `role` varchar(45) NOT NULL
```
### Adding data to database

- User details can be added through the `/adduser` link after launching the app or by directly visiting the `add user` link from the navbar or home page.

- This will internally execute the command
  
```sql
INSERT INTO `users` (`name`, `email`, `role`) VALUES
('nameValue', 'emailValue', 'roleValue');
```
### Getting all users details

- All user details can retrieved through the `/users` link after launching the app or by directly visiting the `All Users` link from the navbar or home page.

- This will internally execute the command
  
```sql
SELECT * FROM `users` ;
```

### Getting specific user's details

- All user details can retrieved through the `/users/<user_id>` link after launching the app or by directly visiting the `Single User Detail` (hardcoded only for testing) link from the navbar or home page.

- This will internally execute the command
  
```sql
SELECT * FROM `users` where id = <idValue> ;
```
### Git Workflow
- The main branch serves as the master branch, and releases will be created from this branch.

- Any feature branch will be named as follows:
developerName-featureName

- Any contribution or feature request will be reviewed by the administrator first.


### How can I contribute 

"Please read `contribute.md` to become familiar with the rules for contributing to this project."


`Note: I've made adjustments to the text for clarity and consistency. Please make sure to replace <virtual_environment_name> and other placeholders with actual values.`

