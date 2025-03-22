# kubescope

Peek into your Kubernetes cluster to read data from configmaps, secrets, volumes, and environment variables.

## Motivation

This is a learning app, to use all endpoints you'll have to appropriately create, mount, and configure Kubernetes resources like ConfigMaps, Secrets, Volumes, Roles and RoleBindings, Service Accounts.

## Usage

Available as a container image

## Environment Variables

Key | Default | Description
--- | ---     | ---
USERNAME | - | Set it, along with "PASSWORD", to enable Basic HTTP Authentication to all endpoints (except healthcheck)
PASSWORD | - | Set it, along with "USERNAME", to enable Basic HTTP Authentication to all endpoints (except healthcheck)
