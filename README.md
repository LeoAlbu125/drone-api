# Drone API

I was motivated to create this API because in the future I will implement more endpoint and use it to communicate with small drones that I will create later, so to hit two bunnies with only one slash I made this to store images and register my drones, later I will implement some face recognition models together with the API to make some expiriments with my drones.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.
- [python-jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server locally

From within the `./src` directory first ensure you are working using your created virtual environment.

After that create a .env file and configure the DB URI, set a variable with the name DB_NAME and put these other variables in it too

```
DB_NAME = 'PUT YOUR DB URI HERE'
AUTH0_DOMAIN = "dev-wxmngepzwpjnyg04.us.auth0.com"
API_AUDIENCE = 'http://127.0.0.1:5050/'
DRONE_USER = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODk4MTAwNSwiZXhwIjoxNjk5MDY3NDA1LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyJdfQ.UpPEZNnGgCKECwv2OAD60ATNnlsdkbV3T2zhI9LT_Kz7AHiQ79jSufEdjMroboW4irZ-xkK4tkJX5lwc9aUIxwOQgW39mIRXHjFyjADxW_x8mkByMg4Ue9n02EtPnguzAJh6JiVqzguj6pD-sSOmJ29PwJlOwBIyf2a17XbipnOB3wgo-41zwJXfCMc1u_JAUUjBzKf0SC0AebHc_991yJtPeC0_GmcE5HWwlr60ubUohJx3dQtSSCuADxwGQsZkciY6T1g2JW9GQmymJKzu7Q6uj2BTcVcGPJdNBl8UkJxlYSSrDWK0JB9GymdbBzsfuhX7hflwZBa6KK3eZl5HZg'
ADMIN_USER = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkV0ZUo5b0tZbkV2NzlzNFpmNWx0WCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eG1uZ2Vwendwam55ZzA0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYUBjbGllbnRzIiwiYXVkIjoiaHR0cDovLzEyNy4wLjAuMTo1MDUwLyIsImlhdCI6MTY5ODkwNjc0NywiZXhwIjoxNjk4OTkzMTQ3LCJhenAiOiJPc0QyNzFRdGJ0cGlFRWFsWXhYbmNQeDJYdXFvQWxzYSIsInNjb3BlIjoiZ2V0OnBob3RvcyBwb3N0OnBob3RvcyBwYXRjaDpkcm9uZXMgZGVsZXRlOnBob3RvcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpwaG90b3MiLCJwb3N0OnBob3RvcyIsInBhdGNoOmRyb25lcyIsImRlbGV0ZTpwaG90b3MiXX0.Sk9KAPJN6nAako6sChzcPq3vWCSI63hH9TwBdgwshMjkBf6sfZv3sQKckQeGcswReIC752aOSuB1LHqb_BN5Fbz00C57xjpX1nxBO2PFBNDxwKPzObMPAiGiFCj6lvntn5WEUANCy56QXOlCc3VizQvTMGSIRECDjsHj-i5D0IXPZJGx59TErARgc4V6wFMnlpW19SM-j4v-IQhGXX_-BESAcBugouvKMJBob_0UtbGIkUoo-DpzFjD9zLFNqcQ5dEvq1NwsojkcDO9Z_inlTpo1L92L1ejLxUhMKN_H0WspdD0j0nuFjUMGgMVfuCt1hrNqQi3M2u8i5SqbBPKALA'
```

Each time you open a new terminal session, run:

```bash
export FLASK_APP=droneapi.py;
```

To run the server, execute:

```bash
flask run -p 5050
```

The `--reload` flag will detect file changes and restart the server automatically.

## Using the exposed link

If you dont want to run locally you can use it with the public **[link](https://drone-api-0-001.onrender.com)**. (there is a problem with tests running in the online DB, some of them fail because the DB "receives too much connections at the same time")

# API Reference

()You should substitute `<your-api-base-url>` for the local link or the exposed one.)

## Authentication

This API uses authentication to secure certain endpoints. You need to include a valid JWT token in the `Authorization` header for these protected endpoints. The token should be in the format: `Bearer YOUR_TOKEN`. (I will send two tokens one for the ADMIN ROLE and other for the DRONE ROLE)

---

## 1. Get All Drones

* **Endpoint:** `/drones`
* **HTTP Method:** GET
* **Description:** Get a list of all drones.
* **Authentication:** None required.
* **CURL Example:**

```
curl -X GET http://your-api-base-url/drones

```

## 2. Get Photos by Drone

* **Endpoint:** `/<drone_id>/photos`
* **HTTP Method:** GET
* **Description:** Get photos associated with a specific drone.
* **Authentication:** Requires a valid JWT token with `get:photos` permission. (DRONE, ADMIN)
* **CURL Example:**

```
curl -X GET -H "Authorization: Bearer YOUR_TOKEN" http://your-api-base-url/1/photos 
```

  Replace `YOUR_TOKEN` with a valid JWT token and your-api-base-url with the local or exposed URL.

## 3. Post a Photo

* **Endpoint:** `/photos`
* **HTTP Method:** POST
* **Description:** Add a new photo associated with a drone.
* **Authentication:** Requires a valid JWT token with `post:photos` permission. (DRONE, ADMIN)
* **CURL Example:**

```
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{
  "tag": "Aerial View",
  "content": "URL to Photo 3",
  "drone_id": 1
}' http://your-api-base-url/photos
```

 Replace `YOUR_TOKEN` with a valid JWT token and your-api-base-url with the local or exposed URL.

## 4. Patch Drone Details

* **Endpoint:** `/drones/<id>`
* **HTTP Method:** PATCH
* **Description:** Update details of a specific drone.
* **Authentication:** Requires a valid JWT token with `patch:drones` permission. (ADMIN)
* **CURL Example:**

```
curl -X PATCH -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{
  "drone_name":"new_name", "drone_model":"new_model"
}' http://your-api-base-url/drones/1
```

  Replace `YOUR_TOKEN` with a valid JWT token and your-api-base-url with the local or exposed URL.

## 5. Delete a Photo

* **Endpoint:** `/photos/<id>`
* **HTTP Method:** DELETE
* **Description:** Delete a specific photo by its ID.
* **Authentication:** Requires a valid JWT token with `delete:photos` permission. (ADMIN)
* **CURL Example:**

```
curl -X DELETE -H "Authorization: Bearer YOUR_TOKEN" http://your-api-base-url/photos/3
```

  Replace `YOUR_TOKEN` with a valid JWT token and your-api-base-url with the local or exposed URL.

---

## Error Handling

The API handles errors with the following error codes and messages:

* 404 Not Found: When a requested resource does not exist.
* 422 Unprocessable Entity: When there is a problem with the request or database operation.
* 500 Internal Server Error: For internal server errors.
