# Ansible Flask App Deployment with HAProxy Load Balancer

This project contains an Ansible playbook (site.yaml) to deploy a Python Flask application across three web servers (devA, devB, devC) and configure HAProxy on a separate host (HAproxy) to act as a load balancer.

Access to the internal network (10.0.1.0/27) is managed via a Bastion host (bastionNSO).

## Project Structure
site.yaml - Main Ansible playbook
application2.py - Flask application
templates - Configuration templates
haproxy.cfg.j2 - HAProxy configuration template
flaskapp.service.j2 - Systemd service template

## Flask Application
The application returns the current time and server hostname:

## Deployment
Ensure SSH access is configured
Run the Ansible playbook
ansible-playbook -i hosts site.yaml