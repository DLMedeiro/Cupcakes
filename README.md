# Cupcakes

## Check it out at: 

https://dlmedeiro.github.io/Cupcakes/

## Setup

#### Linux:

``` python3 -m venv venv ```

``` source venv/bin/activate```

``` pip install -r requirements.txt```

``` createdb playlist-app```

``` flask run ```

#### Windows:
``` $ python3 -m pip virtualenv env ```

``` $ venv\Scripts\activate.bat```

``` (venv) $ python3 -m pip install -r requirements.txt```

#### Database:

Set up postgres connection and update password information if needed.

``` (psql) CREATE DATABASE cupcakes ```

``` (psql) CREATE DATABASE cupcakes_test ```

``` (venv) $ python seed.py ``` 

#### Testing:

``` (venv) $ python -m unittest -v tests ```


## Routes

__GET /__: Returns an HTML page showing an empty list where cupcakes will appear and a form where new cupcakes can be added.

This page is entirly static.

Using Axios and jQuery this page will:
* Query the API to get cupcakes and add them to the page.
* Handles form submission to both let the API know about the new cupcake and updates the list on the page to show it.

__GET /api/cupcakes__: Get data about all cupcakes.

Example Response: ``` {cupcakes: [{id, flavor, size, rating, image}, ...]} ```

The values will come from each cupcake instance.

__GET /api/cupcakes/[cupcake-id]__: Get data about a single cupcake.

Example Response: ``` {cupcake: {id, flavor, size, rating, image}} ```

This will raise a 404 if the cupcake cannot be found.

__POST /api/cupcakes__: Create a cupcake with flavor, size, rating and image data from the body of the request.

Example Response: ``` {cupcake: {id, flavor, size, rating, image}} ```

__PATCH /api/cupcakes/[cupcake-id]__ : Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request.

Example Response for a newly updated cupcake: ``` {cupcake: {id, flavor, size, rating, image}} ```

This will raise a 404 if the cupcake cannot be found.

__DELETE /api/cupcakes/[cupcake-id]__: Delete cupcake with the id passed in the URL

Example Response: ``` {message: "Deleted"} ```

This will raise a 404 if the cupcake cannot be found.

## Technologies used

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height = 50px width=50px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height = 50px width=50px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height = 50px width=50px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain-wordmark.svg" height = 50px width=50px//> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jquery/jquery-plain-wordmark.svg" height = 50px width=50px//>