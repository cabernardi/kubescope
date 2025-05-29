# 03 - Environment Variables

1. Edit/re-create the **Deployment** from [Question 2](../02-deployment/), to add an **env** block to the kubescope **container** [[Ref]](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/). _Note: You can't set deployment environment variables imperatively_
    - Add one or more variables, e.g. `AMAZING`, with a value of your choice, like `kubescope_is_amazing`

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `GET /v1/env/{env}` entrypoint, and press "Try it"
    1. Input `AMAZING` and execute the request. This will read the environment variable `AMAZING` from inside the running `kubescope` container

1. [Alternative] Do the request directly at [http://localhost:8000/v1/env/AMAZING](http://localhost:8000/v1/env/AMAZING), or from the terminal
    - ```bash
      curl http://localhost:8000/v1/env/AMAZING
      ```

---
[Solution](./solution.md)
