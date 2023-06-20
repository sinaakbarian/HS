#### Here is the code for Setting up a RESTful API with Python & nginx.

To get the result, first run ``` python app.py```. Then run ```sudo nginx -c nginx/flask_app.conf``` and run Test commands (e.g., curl 127.0.0.1/timestamp) to see the result.

#### This is for the following part:
---
### 3. Setup a RESTful API with python & nginx.
- Using localhost
- Free to choose any python web component
- All outputs in JSON

API definition: /timestamp
> return current UNIX timestamp
```
# Test command:
curl 127.0.0.1/timestamp

# Expected outcome:
{"timestamp":1624900201}
```

API definition: /readdata
> read POST JSON input and send it back
```
# Test command:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"abc","password":"xyz"}' \
  http://127.0.0.1/readdata

# Expected outcome:
{"username":"abc","password":"xyz"}
```

bad input
```
# Test command:
curl 127.0.0.1/noexist

# Expected outcome:  (404)
... 
404 Not Found 
...
```

#### What to submit:
- Python code

