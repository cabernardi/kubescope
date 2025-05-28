# 05 - Init Containers

1. Edit/re-create the **Deployment** from [Question 4](../04-secrets-as-env/), to add a **Init Container**. _Note: You can't do this imperatively_ [[Ref]](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
    - On the **Init Container**, use image `alpine:latest`, set the **command** to `["sh", "-c", "echo 'Hello from init container!' > /etc/init/hello-init.txt'"]`, and mount a **Volume** named **init-volume** to `/etc/init`, as **readOnly: false**.
    - On the `kubescope` container, mount the same **Volume**, to the same path, but as **readyOnly: true**.

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)

1. Use the endpoint `/v1/txt` to read the contents of `/etc/init/hello-init.txt`. The response should match the message writen by the **Init Container**
    - This means that the `kubescope` container was able to read the `hello-init.txt` file, created by the **Init Container**, from the shared **Volume** folder `/etc/init`

---
[Solution](./solution.md)
