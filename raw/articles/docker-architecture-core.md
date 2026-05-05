---
title: "Docker Architecture: Namespaces and Cgroups"
source: "autoresearch"
date_added: 2026-05-04
tags: [autoresearch, docker, architecture]
aliases: []
status: draft
summary: "Phân tích kiến trúc cốt lõi của Docker dựa trên công nghệ Namespaces và Control Groups (cgroups) của Linux kernel."
confidence: high
---

# Docker Architecture: Cgroups and Namespaces Overview

Docker containers rely on two fundamental Linux kernel features to provide lightweight, isolated environments: **Namespaces** and **Control Groups (cgroups)**. Docker itself is not a virtualization platform; rather, it orchestrates these kernel features to manage processes.

## 1. Namespaces: The Isolation Layer
Namespaces provide the "illusion" of a dedicated system by partitioning kernel resources. They ensure that processes in one container cannot see or interfere with processes in another container or on the host.

*   **PID Namespace:** Isolates the process ID space. The main process in a container becomes PID 1, meaning it is unaware of other processes on the host.
*   **Network Namespace:** Gives each container its own network stack (IP addresses, routing tables, socket listings, and network interfaces), independent of the host.
*   **Mount Namespace:** Isolates the filesystem, allowing each container to have its own mount points and view of the root filesystem.
*   **IPC Namespace:** Isolates Inter-Process Communication resources, such as POSIX message queues and shared memory.
*   **UTS Namespace:** Isolates the hostname and domain name, allowing the container to have a different hostname than the host.
*   **User Namespace:** Maps user and group IDs inside the container to different IDs on the host, enhancing security by limiting container privileges.

## 2. Control Groups (cgroups): The Resource Management Layer
While namespaces handle *what* a container can see, cgroups handle *how much* of the host's physical resources a container can consume. They prevent a single container from monopolizing host resources (like CPU, memory, or I/O) and impacting the performance of other containers or the host system.

*   **Resource Limitation:** You can set strict limits (e.g., maximum RAM usage or CPU shares).
*   **Prioritization:** Cgroups allow you to prioritize certain containers for hardware resources.
*   **Monitoring:** Cgroups provide tools to track and report the resource usage of a container.

## 3. How They Work Together in Docker
Docker’s architecture, specifically the container runtime (often `runc` via `containerd`), orchestrates these features when you run a command like `docker run`:

1.  **Request:** The Docker CLI sends a request to the Docker daemon (`dockerd`).
2.  **Orchestration:** `dockerd` instructs `containerd` to prepare the environment.
3.  **Kernel Interaction:** The runtime instructs the Linux kernel to:
    *   Create a new set of **namespaces** to isolate the process.
    *   Set up a new **cgroup** and apply the resource limits defined in the container configuration.
    *   Mount the container's root filesystem.
4.  **Execution:** The runtime executes the container's main process inside this isolated and resource-constrained environment.

In summary, namespaces provide the isolation to make containers act like separate virtual machines, while cgroups provide the resource management to keep them efficient and under control on a shared host.
