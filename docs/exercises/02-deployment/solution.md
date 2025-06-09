# Solutions

## 1

**Declarative**

Create a file named `deployment.yaml` with the following contents:

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
```

Then apply the manifest to the cluster:
```bash
kubectl apply -f deployment.yaml
```

**Imperative**

```bash
kubectl create deployment kubescope --image ghcr.io/cabernardi/kubescope --port 80 --replicas 2 --namespace kubescope-ns
```

## 2 [Optional]

**Declarative**

Create a file named `service.yaml` with the following contents:
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: kubescope
  name: kubescope
  namespace: kubescope-ns
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: kubescope
  type: ClusterIP
```

Then apply the manifest to the cluster:
```bash
kubectl apply -f service.yaml
```

**Imperative**

```bash
kubectl create service clusterip kubescope --tcp 80:80 --namespace kubescope-ns
```

OR

```bash
kubectl expose deployment kubescope --port 80 --name kubescope --namespace kubescope-ns
```

### Notes

The `selector` block on the **Service** must match the `labels` on the **Deployment** `spec.template.metadata`, which are the labels that are applied to the **Pods** managed by the **Deployment**

## 3

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope-ns
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope-ns
```

## 4

Access [http://localhost:8000/health](http://localhost:8000/health)
