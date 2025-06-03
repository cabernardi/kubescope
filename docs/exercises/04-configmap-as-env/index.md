# 04 - ConfigMap as Environment Variables

1. Create a **ConfigMap** of type **Opaque** named kubescope-config in **Namespace** kubescope. The ConfigMap should contain at least one key-value pair, e.g. `INCREDIBLE: kubescope`, under the `data` block [[Ref]](https://kubernetes.io/docs/concepts/configuration/configmap/#using-configmaps-as-environment-variables)

1. Edit/re-create the Kubescope **Deployment** from a previous exercise, to add an **envFrom** block to the kubescope **container**. _Note: You can't mount ConfigMaps in the deployment imperatively_
    - The **envFrom** block should read from the **ConfigMap** created in step 1 [[Ref]](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables)

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `GET /v1/env/{env}` endpoint, and press "Try it"
    1. Input `INCREDIBLE` and execute the request. This will read the environment variable `INCREDIBLE` from inside the running `kubescope` container

1. [Alternative] Do the request directly at [http://localhost:8000/v1/env/INCREDIBLE](http://localhost:8000/v1/env/INCREDIBLE), or from the terminal
    - ```bash
      curl http://localhost:8000/v1/env/INCREDIBLE
      ```

---
[Solution](./solution.md)
