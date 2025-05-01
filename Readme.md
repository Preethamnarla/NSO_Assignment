# Ansible Flask App Deployment with HAProxy Load Balancer

This project contains an Ansible playbook (site.yaml) to deploy a simple Python Flask application across three web servers (devA, devB, devC) and configure HAProxy on a separate host (HAproxy) to act as a load balancer.

Access to the internal network (10.0.1.0/27) is managed via a Bastion host (bastionNSO).

## Project Structure