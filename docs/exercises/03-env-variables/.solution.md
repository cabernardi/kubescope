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
      containers:
      - image: ghcr.io/cabernardi/kubescope
        name: kubescope
        ports:
        - containerPort: 80
        env:
          - name: USERNAME
            value: cabernardi
          - name: PASSWORD
            value: mypwd
```
_Note: You can change the values of USERNAME and PASSWORD to your preference_

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
