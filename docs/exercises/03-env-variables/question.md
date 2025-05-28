# 03 - Environment Variables

1. Edit/re-create the **Deployment** from [Question 2](../02-deployment/question.md), to add an **env** block to the kubescope **container** [[Ref]](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/). _Note: You can't set deployment environment variables imperatively_
    - Add `USERNAME` (case sensitive) variable with a value of your choice
    - Add `PASSWORD` (case sensitive) variable with a value of your choice

1. **Port-forward** the **Deployment** (or **Service**) port **80** to local port **8000** [[Ref]](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/#forward-a-local-port-to-a-port-on-the-pod)

1. Access http://localhost:8000/v1/protected
    - Log in with the credentials you set up on step 1
