# County Stats

### Setup (requires python3 and pip3)

1. Fork/clone or clone down this repo
2. Create a virtual environment on command line: `virtualenv venv`
3. Activate in CL with `source venv/bin/activate`
4. Run `pip3 install -r requirements.txt`
5. Run `export FLASK_APP=app` and `export FLASK_ENV=development`
6. You may need to install Flask-SQLAlchemy, Marshmallow, and some other dependencies independently

---

### Testing
The testing suite runs on unittest, to see them in action run `python3 -m unittest test.py` in the root directory.

---

### Available Endpoints


---

### Containers
See `Dockerfile` and `docker-compose.yml` for an attempt at creating containers. I found this would build an image/container, but had less luck on the actual functionality. 

---
