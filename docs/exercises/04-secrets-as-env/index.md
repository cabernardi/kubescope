# 03 - Environment Variables

1. Create a **Secret** of type **Opaque** named kubescope-credentials in **namespace** kubescope. The secret should contain two keys: `USERNAME` and `PASSWORD` (case sensitive), with values of your choice [[Ref]](https://kubernetes.io/docs/concepts/configuration/secret/#opaque-secrets)

1. Edit/re-create the **Deployment** from [Question 2](../02-deployment/), to add an **envFrom** block to the kubescope **container**. _Note: You can't mount secrets in the deployment imperatively_
    - The **envFrom** block should read from the **Secret** created in step 1 [[Ref]](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables)

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `GET /v1/protected` entrypoint, and press "Try it"
    1. Execute the request, and fill the authentication pop-up with the credentials you set up on step 1

1. [Alternative] Do the request directly at [http://localhost:8000/v1/protected](http://localhost:8000/v1/protected)
    - Log in with the credentials you set up on step 1

1. [Alternative] Use `curl -u your_username:your_password http://localhost:8000/v1/protected` to test from the terminal

You should get a `{"message": "You are authenticated!"}` response.

---
[Solution](./solution.md)
