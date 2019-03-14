# Generic Service

## Deployment

Application tier API deployment using docker-compose.

## Assumptions

* Log is ordered by date, ASC, so it can be reversed for queries using limit.
* Log rotation is being used, and logs correspond to the current month.

## TODO

* Create CI pipeline with CircleCI
    * Create image releases and latest versions per branch
* Enforce SSL
* Handle pagination
* Add non blocking runtime: Gunicorn, Nginx
* Improve Swagger API definition retrieval