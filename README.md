# fotoblog

This project is the development of the OpenClassrooms tutorial: [Allez plus loin avec le framework Django](https://openclassrooms.com/fr/courses/7192426-allez-plus-loin-avec-le-framework-django)

The only difference is that I didn't use venv + SQLite, but two containers: a python container and a postgresql container created using docker (dockerfile and docker compose)

As I have always worked with gitlab, I also took the opportunity to set up a **github action** to run **pylint django**. The idea was not to have a good or bad score, just to see how the github actions work. Now there is an action running pylint django every time I push something new here.

How to use this project?

- **git clone**
- **docker compose up** (you need the docker daemon running)
- open localhost in your fav browser or click here : **http://localhost:8000/**
