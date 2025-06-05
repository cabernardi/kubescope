# 09 - Data Persistence

Requires [Question 8](../08-database/) to be successfuly completed.
---

1. Create a **PersistentVolumeClaim (PVC)** named `postgres-data`, allocating `10Mi`, with `ReadWriteOnce` **accessMode**, and using the `standard` **storageClassName**. _Note: You can't create a PVC imperatively_ [[Ref]](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/#create-a-persistentvolumeclaim)
    - _There's no need to create a **PersistentVolume** too, as minikube already implementes Dynamic Provisioning [[Ref]](https://minikube.sigs.k8s.io/docs/handbook/persistent_volumes/)_

1. Edit the `postgres` **Deployment** to add a **volume** based on the **PersistentVolumeClaim**. Mount this volume to `/var/lib/postgresql/data`. _Note: you can't create deployments with volumes imperatively_ [[Ref]](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/#create-a-pod)

1. **Port-forward** the Kubescope **Deployment** (or **Service**) port **80** to local port **8000**

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `POST /v1/db/init` endpoint, press "Try it", and execute the request (if it fails, wait a few seconds and try again, the `postgres` **Pod** might not be ready to receive connections yet)
    1. Expand the `POST /v1/db/add` endpoint, and press "Try it"
    1. Type in any string, and execute the request. Do this a couple times.
    1. Expand the `GET /v1/db/get-all` endpoint, press "Try it", and execute the request

Now, let's validate the data persistency on the database:

1. Restart the `postgres` **Deployment**. A couple ways to do it:
    - `kubectl rollout restart deployment/postgres -n kubescope`
    - If you're using an interface for Kubernetes, you can simply delete the `postgres` running **Pod**, a new one will automatically be allocated

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `POST /v1/db/init` endpoint, press "Try it", and execute the request (if it fails, wait a few seconds and try again, the `postgres` **Pod** might not be ready to receive connections yet)
    1. Expand the `GET /v1/db/get-all` endpoint, press "Try it", and execute the request.

The `GET /v1/db/get-all` endpoint should now respond with the same list as before the restart. This means that the data under `/var/lib/postgresql/data`, where Postgres stores the database, is kept intact even after the **Pod** is replaced by new ones, because it's part of a Kubernetes **PersistentVolume**.

---
[Solution](./solution.md)
