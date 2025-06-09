# Solutions

## 1

**Declarative**

1. Encode the credential string as Base64.
_Note: You can change the values to be encoded to your preference_

```bash
echo -n "db" | base64
echo -n "user" | base64
echo -n "db_pass" | base64
```

2. Create a `postgres-secret.yaml` file with the encoded data generated on previously:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: postgres-secret
  namespce: kubescope
data:
  POSTGRES_DB: ZGI=
  POSTGRES_USER: dXNlcg==
  POSTGRES_PASSWORD: ZGJfcGFzcw==
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f postgres-secret.yaml
```

**Imperative**

_Note: You can change the values of POSTGRES_DB, POSTGRES_USER, and POSTGRES_PASSWORD to your preference_

```bash
kubectl create secret generic postgres-secret --from-literal POSTGRES_DB=db --from-literal POSTGRES_USER=user --from-literal POSTGRES_PASSWORD=db_pass -n kubescope
```

## 2

Create/edit a file named `postgres-deployment.yaml` with the following contents:

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
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f postgres-deployment.yaml
```

## 3

**Declarative**

Create/edit a file named `postgres-service.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
  labels:
    app: postgres
spec:
  type: ClusterIP
  ports:
    - port: 5432
      name: db
  selector:
    app: postgres
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f postgres-service.yaml
```

**Imperative**

```bash
kubectl create service clusterip postgres --tcp 5432:5432 --namespace kubescope-ns
```

OR

```bash
kubectl expose deployment postgres --port 5432 --name postgres --namespace kubescope-ns
```

## 4

**Declarative**

1. Encode the `postgres` **Service** name to use as the Host

```bash
echo -n "postgres" | base64 -d
```

1. Create a `kubescope-db-secret.yaml` file with the encoded data generated on previously

_Note: Use the same values configured on the postgres secret_

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: kubescope-db-secret
  namespce: kubescope
data:
  DB_NAME: ZGI=
  DB_USERNAME: dXNlcg==
  DB_PASSWORD: ZGJfcGFzcw==
  DB_HOST: cG9zdGdyZXM=
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f kubescope-db-secret.yaml
```

**Imperative**

_Note: Use the same values configured on the postgres secret_

```bash
kubectl create secret generic kubescope-db-secret \
  --from-literal DB_NAME=db \
  --from-literal DB_USERNAME=user \
  --from-literal DB_PASSWORD=db_pass \
  --from-literal DB_HOST=postgres \
  -n kubescope
```

## 5

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
              name: kubescope-db-secret
```

Then apply the manifest to the cluster:

```bash
kubectl apply -f deployment.yaml
```

## 6

```bash
kubectl port-forward deployment/kubescope 8000:80 --namespace kubescope-ns
```

**If the Service was created**
```bash
kubectl port-forward service/kubescope 8000:80 --namespace kubescope-ns
```
