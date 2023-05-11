
# Planner-FastAPI

This is an api for creating planners.

## Endpoints
| Endpoint         | Method   | Route             | Description                                |
|------------------|----------|------------------|--------------------------------------------|
| User Signup      | POST     | /user/signup      | Register a new user                         |
| User Login       | POST     | /user/login       | Log in with user credentials                |
| Get All Events   | GET      | /event/           | Get a list of all events                    |
| Get Event by ID  | GET      | /event/{id}       | Get a specific event by ID                  |
| Update Event     | PUT      | /event/{id}       | Update an existing event by ID              |
| Create Event     | POST     | /event/new        | Create a new event                          |


## Tech Stack
**Server:** Python, FastAPI


## Author

- [@alomia](https://www.github.com/alomia)
