# Kubescope Exercises

## Pre-requisites

- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- A running [minikube](https://minikube.sigs.k8s.io/docs/start/) cluster
- A **Namespace** `kubescope` exists in the cluster
```bash
kubectl create namespace kubescope
```

## Exercises

1. [Create Pod](./01-pod-local-access/)

1. [Create Deployment](./02-deployment/)

1. [Create Deployment with environment variables](./03-env-variables/)

1. [Create Deployment with secret as environment variables](./04-secrets-as-env/)

1. [Create InitContainer, write to shared volume](./05-sidecar-write/)

1. Create Sidecar container, continuosly write to shared volume

1. Create Postgres Deployment (before volumes are introduced), add connection in Kubescope
    1. Add data
    1. Restart deployment
    1. Check data

1. Create ConfigMap, mount as volume
    1. Build txt file
    1. Build yaml file

1. Add volume o Postgres Deployment
