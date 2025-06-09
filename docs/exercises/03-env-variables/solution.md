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
  namespace: kubescope-ns
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
      containers:
      - image: ghcr.io/cabernardi/kubescope
        name: kubescope
        ports:
        - containerPort: 80
        env:
          - name: AMAZING
            value: kubescope
          - name: COOL
            value: kubernetes
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f deployment.yaml
```

## 2

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope-ns
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope-ns
```

## 3

**Terminal**

```bash
curl http://localhost:8000/v1/env/AMAZING
curl http://localhost:8000/v1/env/COOL
```

**UI**

1. Access [https://localhost:8000/docs](https://localhost:8000/docs)

1. Expand the `GET /v1/env` endpoint, and press "Try it"

1. Input `AMAZING` or `COOL`, and execute the request.


These calls should respond with `{"variable": "AMAZING", "value": "kubescope"}` and `{"variable": "COOL", "value": "kubernetes"}`, respectively.
