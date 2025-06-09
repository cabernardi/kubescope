# 05 - ConfigMap as File

With a running Kubescope deployment, from any previous exercise, with a local port forward, do:

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
    1. Expand the `GET /v1/config/color` endpoint, and press "Try it"

1. [Alternative] Do the request directly at [http://localhost:8000/v1/config/color](http://localhost:8000/v1/config/color), or from the terminal
    ```bash
      curl http://localhost:8000/v1/config/color
      ```

    The endpoint will respond with the default value:
    ```json
    {"color": "DEFAULT_BLUE"}
    ```

1. Create a INI file, named `config.ini`, with a `color` key under the `[general]` section, like this:
    ```ini
    [general]
    color = ORANGE
    ```

1. Create a **ConfigMap** named kubescope-config in **Namespace** kubescope-ns, based on the INI file from the previous step. [[Ref]](https://kubernetes.io/docs/concepts/configuration/configmap/#using-configmaps-as-environment-variables)
    - _Tip: use `--from-file`_

1. Edit/re-create the Kubescope **Deployment** from any previous exercise, mounting the kubescope-config **ConfigMap** as a volume, under the `/etc/kubeconfig`. [[Ref]](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#add-configmap-data-to-a-volume)
    - This will create a `config.ini` file in the `/etc/kubeconfig` directory, where the Kubescope app expects to read the configuration from.

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Repeat the first step, it now must respond with the color name configured on the `config.ini`.

---
[Solution](./solution.md)
