<h1>COCTALES WEB APP</h1>
<h2>Search, discover, and connect with fellow cocktail lovers through my social cocktail app.</h1>

<img src="static/images/landing.PNG" ALT="Landing-page">

<h3>The app offers this functionality</h3>
<h4>Social sharing</h4>
<p>Allow users to share their experiences and content on this media  
  platform through cocktale rooms, which can help promote your app and 
  increase user engagement.</p>

<h4>User profile</h4>
<p>Allow users to create profiles that showcase their favorite cocktails, bars, and reviews. 
    Users can follow each other and connect with like-minded cocktail enthusiasts.</p>

<h4>Cocktail categories</h4>
<p>provides information on the different categories of cocktails, including 
    classics, popular drinks, and seasonal drinks. Users can also create their own
    indegenous categories </p>


<img src="static/images/Dashboard.PNG" ALT="Dashboard">

<H2>Deploying on EC2</H2>

### Setup
Update the System
```bash
sudo apt-get update
```
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/salawekesa/COCKTALES-app.git
```
You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Download django usig pip
```bash
sudo apt install python3-pip -y
```
```bash
pip install django
```
Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
python3 manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python3 manage.py migrate
```

One last step and then our COCKTALE App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
python3 manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple COCKTALE App. Start the server by following command

```bash
python3 manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.

Cheers and Happy Coding :)
