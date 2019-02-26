# locust_example
Example of a load test using Locust.io

To run this example you will need to install:
https://locust.io
https://github.com/typicode/json-server

Both have good examples on how to install, and install globally.

Once you have set these up you can run:
1) json-server --watch db.json
2) locust -f swarm_on_json_server.py --host=http://localhost:3000

Note that json-server doesn't scale very far, and locust quickly takes it down.
While this is satisfying to watch, I am looking for a more robust example to test against, suggestions welcome.