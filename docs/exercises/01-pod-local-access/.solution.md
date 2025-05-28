# Solutions

## 1

**Imperative**

```bash
kubectl run kubescope --image ghcr.io/cabernardi/kubescope --port 80 --namespace kubescope
```

**Declarative**

Create a file named `pod.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kubescope
  namespace: kubescope
spec:
  containers:
  - image: ghcr.io/cabernardi/kubescope
    name: kubescope
    ports:
    - containerPort: 80
```

Then apply the manifest to the cluster:
```bash
kubectl apply -f pod.yaml
```

## 2

```bash
kubectl port-forward pod/kubescope 8000:80 --namespace kubescope
```
