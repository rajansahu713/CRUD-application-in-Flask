# CRUD application in Flask

Introduction
>  In the application we are performing CRUD(Create, Read, Uodate, Delete) Operating using Flask.

Step1: Import all the requirements
Sqlalchemy is sqlite connector 
```python
from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
```

