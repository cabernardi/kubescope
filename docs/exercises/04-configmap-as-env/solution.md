# Solutions

## 1

**Declarative**

1. Create a `configmap.yaml` file with the encoded data generated on previously:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubescope-configmap
  namespce: kubescope
data:
  INCREDIBLE: kubescope
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f configmap.yaml
```

**Imperative**

```bash
kubectl create configmap kubescope-configmap --from-literal INCREDIBLE=kubescope -n kubescope
```

_Note: You can set any number of key-value pairs in the `data` block, or with the `--from-literal` flag_

## 2

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
      containers:
      - image: ghcr.io/cabernardi/kubescope
        name: kubescope
        ports:
        - containerPort: 80
        envFrom:
          - configMapRef:
              name: kubescope-configmap
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f deployment.yaml
```

## 3

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope
```

## 4

**Terminal**

```bash
curl http://localhost:8000/v1/env/INCREDIBLE
```

**UI**

1. Access [https://localhost:8000/docs](https://localhost:8000/docs)

1. Expand the `GET /v1/env` endpoint, and press "Try it"

1. Input `INCREDIBLE`, and execute the request.


These calls should respond with `{"variable": "INCREDIBLE", "value": "kubescope"}`, respectively.
