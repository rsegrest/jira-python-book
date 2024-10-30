# Code Example Repo for _Custom Jira DevOps with Python_ by Rick Segrest
This repo contains the example code from the tutorials for the book *Custom Jira DevOps with Python: Using the Atlassian Python API*.

The repo contains several files and folders:


* **documentation** &mdash; contains documentation references used by this README file.

* **main_project** &mdash; The example project described in the book
* **main_project/create_venv.bash** &mdash; A script for Linux and MacOS to create a Python virtual environment and "PIP install" all necessary dependencies.
* **main_project/create_venv.ps1** &mdash; A script for Windows PowerShell that does the same as "create_venv.bash"
* **main_project/set_python_path.bash** &mdash; A script for Linux and MacOS to set the PYTHONPATH environment variable to point to the current directory. This is useful if you are seeing import errors in your project.
* **main_project/set_python_path.bash** &mdash; A script for Windows PowerShell that does the same as "set_python_path.bash"
    * **main_project/configuration** &mdash; contains an example configuration file that allows the project to connect to Jira. You will need to log into ricksegrest.atlassian.net with the username <rsegrest99@hotmail.com> and the password "DevOps2025". You will then need to click on the "MPP User" avatar in upper-right corner of the screen, and then choose the "Security" tab. Next, under the "API Tokens" section, click "Create and manage API tokens," and then click the button that says "Create API token". To create the token, give it a name, and then copy and paste it into the jira.cfg file to set the "token=" variable to that new token's value. Also contains a Python function to read the configuration values.
        * **main_project/configuration/jira.cfg.template** &mdash; This is a sample template for the configuration file. You will need to remove the ".template" from the filename (so it is just called "jira.cfg"), and you will need to set the token variable to point to the token string described above, in quotes.
    * **main_project/interface** &mdash; The Python classes and functions that connect to and interact with the Atlassian Python API.
    * **main_project/output** &mdash; Classes and functions that convert the raw data received from the API into HTML and XLSX spreadsheet output.
    * **main_project/static/css** &mdash; Contains class definitions to improve the look and feel of the generated HTML tables
    * **main_project/templates** &mdash; HTML files that Jinja inserts dynamic data into to render the HTML tables on-screen.
    * **main_project/util** &mdash; The "utilities" folder, which right now only contains a function to check whether a key exists in a Python dictionary data structure.

[Description of the Test-Driven Development approach to software development](documentation/tdd.md)

![Book Cover](<documentation/book_cover.png>)