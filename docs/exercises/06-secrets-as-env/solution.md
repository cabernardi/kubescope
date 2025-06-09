# Solutions

## 1

**Declarative**

1. Encode the credential string as Base64.
_Note: You can change the values to be encoded to your preference_

```bash
echo -n "cabernardi" | base64
echo -n "mypwd" | base64
```

2. Create a `secret.yaml` file with the encoded data generated on previously:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kubescope-credentials
  namespce: kubescope
data:
  PASSWORD: bXlwd2Q=
  USERNAME: Y2FiZXJuYXJkaQ==
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f secret.yaml
```

**Imperative**

_Note: You can change the values of USERNAME and PASSWORD to your preference_

```bash
kubectl create secret generic kubescope-credentials --from-literal USERNAME=cabernardi --from-literal PASSWORD=mypwd -n kubescope
```

## 2

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
        envFrom:
          - secretRef:
              name: kubescope-credentials
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f deployment.yaml
```

## 3

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope-ns
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope-ns
```
