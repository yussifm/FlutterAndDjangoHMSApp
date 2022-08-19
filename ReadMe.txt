# install the package virtualenv
~~~pip install virtualenv

# setup envioronment for the python api
python -m virtualenv projectenv

# if using python >= 3.3
~~~~~ python -m venv env

# start the environment in linux using 
~~~~~~ blackhat_hms/bin/activate

# or in windows
# windows
projectenv\Scripts\activate

python -m venv <venv-name>
# To activate
#C:\Users\..\<venv-name>
.\Scripts\activate.bat

~~~~~ env\activate.bat
or navigate into the bin folder and type "activate" from you commad line 

# when you are done using the environment, type in the command below
~~~~ deactivate


Follow link to see how to setup python enviroment
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/









# To generate your requrements file do:
pip freeze > requirements.py

# To install the requrements do: 
pip install -r requirements.py

# If you want to make sure pip is using python3, you can do this:
Cd blackhat_hms
 pip3 freeze > requirements.py
 pip3 install -r requirements.py

# Or:
pip3 freeze > requirements.py

To install packages
pip3 install -r requirements.py


django create new project
~~~ django-admin startproject {project-name}

~~~ python manage.py runserver 



https://www.django-rest-framework.org/
https://docs.djangoproject.com/en/4.1/intro/tutorial01/


SUperUser credentials
username: zak
Email: zak@gmail.com
password: 12345678









