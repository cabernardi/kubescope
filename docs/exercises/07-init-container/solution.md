# Solutions

## 1

Create/edit a file named `deployment.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: kubescope
  name: kubescope
  namespace: kubescope
spec:
  replicas: 2
  selector:
    matchLabels:
      app: kubescope
  template:
    metadata:
      labels:
        app: kubescope
    spec:
      initContainers:
      - image: alpine:latest
        name: txt-writer
        command:
          - "/bin/sh"
          - "-c"
          - "echo 'Hello from init container!' > /etc/init/hello-init.txt"
        volumeMounts:
          - name: init-volume
            mountPath: /etc/init
            readOnly: false
      containers:
      - image: ghcr.io/cabernardi/kubescope
        name: kubescope
        ports:
        - containerPort: 80
        volumeMounts:
          - name: init-volume
            mountPath: /etc/init
            readOnly: true
      volumes:
        - name: init-volume
          emptyDir: {}
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f deployment.yaml
```

## 2

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope
```

## 3

**Swagger**

1. Access [http://localhost:8000/docs](http://localhost:8000/docs)
1. Expand `GET /v1/txt`, and click on `Try it out`
1. Insert `/etc/init/hello-init.txt` as the path and run the request

**curl**

```bash
curl http://localhost:8000/v1/txt?path=/etc/init/hello-init.txt
```

The output should be `"Hello from init container!\n"`

_Note: Remember to use your own credentials on the `-u` argument, or swagger_
