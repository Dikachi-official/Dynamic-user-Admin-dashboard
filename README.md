# Dynamic-user-Admin-dashboard
<b>Built with Django framework and MongoDB(Djongo) so as not to change Django ORM<br/>
<h2>Usage:</h2>
1. <strong>Install djongo:</strong>
    <p>pip install djongo</p>

2. <p>Into settings.py file of your project, add:</p>
<br/>


    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'your-db-name',
            'CLIENT': {
               'host': 'your-db-host',
               
            }
        }
    }
    
3. <p>Run manage.py makemigrations <app_name></p>  
   <p>followed by manage.py migrate (ONLY the first time to create collections in mongoDB)</p>
 
4. YOUR ARE SET! HAVE FUN!


<h2>Requirements:</h2>

<li> Python 3.6 or higher.</li>

<li> MongoDB 3.4 or higher.</li>


<h2>How it works</h2>
<p>djongo is a SQL to mongodb query compiler. It translates a SQL query string into a mongoDB query document. As a result, all Django features, models etc. work as is.</p>

<strong>Django contrib modules:</strong>

  
<p>'django.contrib.admin',</p>
<p>'django.contrib.auth',</p>    
<p>'django.contrib.sessions',</p>

<br/>

<b>Features</b>
<li>Use Django Admin GUI to access MongoDB.</li>
<li>Embedded Model.</li>
<li>Embedded Array.</li>
<li>Embedded Form Fields.</li>
