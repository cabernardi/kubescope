# 08 - Inter-pod communication

1. Create a **Secret** `postgres-secret`, in **Namespace** kubescope, with keys `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD`. The values can be set up to your preference.
    - Remember to encode the values as base64

1. Create a **Deployment** named `postgres`, with **1** replica, listening on port **5432**, using image `postgres:17-alpine`, on **Namespace** kubescope. Mount the `postgres-secret` **Secret** from the previous step as environment variables.

1. Create a **Service** named `postgres` of type **ClusterIP**, on **Namespace** kubescope [[Ref]](https://kubernetes.io/docs/concepts/services-networking/service/)

1. Create a **Secret** `kubescope-db-secret`, in **Namespace** kubescope, with keys `DB_HOST`, `DB_USERNAME`, `DB_PASSWORD`, and `DB_NAME`.
    - The value of `DB_USERNAME` must match the value of `POSTGRES_USER` from the first step
    - The value of `DB_PASSWORD` must match the value of `POSTGRES_PASSWORD` from the first step
    - The value of `DB_NAME` must match the value of `POSTGRES_DB` from the first step
    - The value of `DB_HOST` must match the name of the postgres **Service** created in the previous step [[Ref]](https://kubernetes.io/docs/concepts/services-networking/service/#dns). _Note: coredns is installed by default by minikube_
    - Remember to encode the values as base64

1. Edit/re-create the Kubescope **Deployment** from a previous exercise, to mount the `kubescope-db-secret` **Secret** from the previous step as environment variables.

1. **Port-forward** the Kubescope **Deployment** (or **Service**) port **80** to local port **8000**

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `POST /v1/db/add` endpoint, and press "Try it"
    1. Type in any string, and execute the request. Do this a couple times.
    1. Expand the `GET /v1/db/get-all` endpoint, press "Try it", and execute the request

The `GET /v1/db/get-all` endpoint should respond with a list of names that you added using `POST /v1/db/add`. This means that the Kubescope **Pods** are able to reach the Postgres **Pod**, through the Postgres **Service**, to read and write data to the postgres database.
