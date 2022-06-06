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
The testing suite runs on unittest, to see them in action run `python3 -m unittest test.py` in the root directory. Tests cover happy/sad paths, showing what a successful request looks like and what an unsuccessful request might look like.

---

### Available Endpoints
#### GET number of all county entries
<details>
  <summary> Request </summary>
  
  *GET `http://127.0.0.1:5000/api/v1/county`*
  
  </details>
  
  <details>
    <summary> Response </summary>
  
`{  "Number of stored counties": 3193 } `


  
</details>

---

#### GET the happiness index for a specific county
<details>
  <summary> Request </summary>
  
  *GET `http://127.0.0.1:5000/api/v1/county/10003`*
  
  </details>
  
  <details>
    <summary> Response </summary>
  
```  
{
    "h_index": 101.1,
    "zip": "10003"
} 
```

</details>

---

#### GET the specified statistic from 2 or more counties (mean, median, range, stdev)
<details>
  <summary> Request </summary>
  
  *GET `http://127.0.0.1:5000/api/v1/county/happiness_stats/mean?10001&10003&10005`*
  
  other possibilities:
  
  *GET `http://127.0.0.1:5000/api/v1/county/happiness_stats/median?10001&10003&10005`*
  
  *GET `http://127.0.0.1:5000/api/v1/county/happiness_stats/range?10001&10003&10005`*
  
  *GET `http://127.0.0.1:5000/api/v1/county/happiness_stats/stdev?10001&10003&10005`*
  
  </details>
  
  <details>
    <summary> Response </summary>
  
```  
{
    "mean": 100.85
}
```
  
</details>

---

### Containers
See `Dockerfile` and `docker-compose.yml` for an attempt at creating containers. I found this would build an image/container, but had less luck on the actual functionality. As far as adding more information to the DB, a user would just need to add data to the preexisting JSON file.

---
