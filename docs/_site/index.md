# Kubescope

Peek into your Kubernetes cluster to read data from configmaps, secrets, volumes, and environment variables.

## Motivation

This is a learning app, to use all endpoints you'll have to appropriately create, mount, and configure Kubernetes resources like ConfigMaps, Secrets, Volumes, Roles and RoleBindings, Service Accounts.

1. [Suggested exercises](./exercises/exercises.md)

## Usage

Available as a container image, [ghcr.io/cabernardi/kubescope](https://github.com/cabernardi/kubescope/pkgs/container/kubescope).

## Environment Variables

Key | Default | Description | Required
--- | ---     | ---         | ---
USERNAME       | - | Set it, along with "PASSWORD", to enable Basic HTTP Authentication to all endpoints (except healthcheck) | no
PASSWORD       | - | Set it, along with "USERNAME", to enable Basic HTTP Authentication to all endpoints (except healthcheck) | no
DB_HOST        | - | Postgres DB Host          | no
DB_PORT        | 5432 | Postgres DB Port       | no
DB_USERNAME    | - | Postgres DB Username      | no
DB_PASSWORD    | - | Postgres DB Password      | no
DB_NAME        | - | Postgres DB Database Name | no
