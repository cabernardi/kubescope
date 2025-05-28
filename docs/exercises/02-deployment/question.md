# 02 - Deployment Creation

1. Create a **Deployment** named kubescope, with **2** replicas, listening on port **80**, using image `ghcr.io/cabernardi/kubescope`, on **Namespace** kubescope

1. [Optional] Create a **Service** named **kubescope** of type **ClusterIP**, on **Namespace** kubescope [[Ref]](https://kubernetes.io/docs/concepts/services-networking/service/)

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access http://localhost:8000/health
