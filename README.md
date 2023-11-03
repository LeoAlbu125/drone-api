# Drone API

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
- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server locally

From within the `./src` directory first ensure you are working using your created virtual environment.

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

If you dont want to run locally you can use it with the public [link](https://drone-api-0-001.onrender.com). (there is a problem with tests running in the online DB, some of them fail because the DB "receives too much connections at the same time")

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
