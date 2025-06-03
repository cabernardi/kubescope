# Solutions

## 2

**Declarative**

1. Create a `configmap-file.yaml` file with the encoded data generated on previously:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubescope-config
  namespce: kubescope
data:
  config.ini: |
    [general]
    color = ORANGE
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f configmap-file.yaml
```

**Imperative**

Create a file `config.ini` with the following contents:
```ini
[general]
color = ORANGE
```

```bash
kubectl create configmap kubescope-config --from-file config.ini -n kubescope
```

_Note: You can set any value for the `color` configuration_

## 3

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
        volumeMounts:
          - name: kubescope-config-volume
            mountPath: /etc/kubescope
            readOnly: true
      volumes:
        - name: kubescope-config-volume
          configMap:
            name: kubescope-config
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f deployment.yaml
```

## 4

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope
```

## 5

**Terminal**

```bash
curl http://localhost:8000/v1/config/color
```

**UI**

1. Access [https://localhost:8000/docs](https://localhost:8000/docs)

1. Expand the `GET /v1/config/color` endpoint, press "Try it", and execute the request


This call should respond with `{"color": "ORANGE"}`
