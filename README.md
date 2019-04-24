# Django Tutorials
---
Django is a python based framework for creating webservers.
Modular so you can pick and choose what you want in your project.

They have a 'batteries included' philosiphy, everythings included, they beleive. 

Elements of django:
- Templates
    - Text in text out, it is the part that spits the HTML to the client overall.
- Object relational mapper (ORM)
    - Python class --> SQL table
    - This means we dont have to directly work with SQL, we can let Python deal with it.
- Routing
    - Takes a URL and activates a Python callable. It is basically the decoder.
- Views
    -  Pure Python (the logic)
    - Always accept request
    - Spit out a response or exception

### Some django termanology
A project in django is the entire server.
A site is a web app, its a single feature.
