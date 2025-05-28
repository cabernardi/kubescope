# 01 - Pod Creation

1. Create a **Pod** named kubescope, using image `ghcr.io/cabernardi/kubescope`, allowing traffic to port **80**, on **Namespace** kubescope [[Ref]](https://kubernetes.io/docs/concepts/workloads/pods/)

1. **Port-forward** the **Pod** port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access [http://localhost:8000/health](http://localhost:8000/health)

---
[Solution](./solution.md)
