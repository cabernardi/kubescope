# Solutions

## 1

1. Create a `postgres-data.yaml` file with the following contents:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-data
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Mi
  storageClassName: standard
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f postgres-data.yaml
```

## 2

1. Edit the file named `postgres-deployment.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  selector:
    matchLabels:
      app: postgres
  replicas: 1
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:17-alpine
          ports:
          - containerPort: 5432
            name: db
          envFrom:
            - secretRef:
                name: postgres-secret
          volumeMounts:
            - name: data
              mountPath: /var/lib/postgresql/data
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: postgres-data
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f postgres-deployment.yaml
```

## 3

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope-ns
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope-ns
```
