QR Generator – DevOps CI/CD Project

A simple Flask-based QR Code Generator deployed through an end-to-end DevOps CI/CD pipeline using GitHub, Jenkins, Docker, Ansible, Terraform, Minikube, and Kubernetes.

🚀 Project Overview

This project demonstrates how application source code can move from GitHub to a running Kubernetes application through an automated CI/CD workflow.

Main Flow

Developer → GitHub → Jenkins Controller → Ansible-managed Docker Agent → Docker Image → Kubernetes/Minikube → QR Generator App

🛠️ Tech Stack

Tool

Purpose

Python / Flask

QR Generator web application

Git

Version control

GitHub

Source code repository

Docker

Containerization

Jenkins

CI/CD automation

Ansible

Jenkins Docker Agent automation

Terraform

Local Minikube infrastructure setup

Minikube

Local Kubernetes cluster

Kubernetes

Application deployment and service management

kubectl

Kubernetes command-line management

📁 Project Structure

qr-generator-devops/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── ansible/
│   └── playbook.yml
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── terraform/
│   └── main.tf
├── Dockerfile
├── Dockerfile.agent
├── .gitignore
└── README.md

🔄 CI/CD Pipeline

The Jenkins pipeline contains these main stages:

Clone GitHub – Fetches the source code from the main branch.

Build Docker Image – Builds qr-generator:latest.

Check Image – Verifies that the Docker image was created.

Deploy to Kubernetes – Applies the Kubernetes manifests to Minikube.

Verify Deployment – Checks Pods and Services.

🏗️ Architecture

Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Controller
    │
    ▼
Ansible-managed Docker Agent
    │
    ├── Docker CLI
    ├── kubectl
    └── Minikube tools
    │
    ▼
Docker Image
qr-generator:latest
    │
    ▼
Kubernetes / Minikube
    │
    ├── Deployment
    │      └── QR Generator Pod
    │
    └── NodePort Service
           │
           ▼
      QR Generator Web App

Terraform is used in this project to automate the Minikube startup/infrastructure setup. The Kubernetes Deployment and Service are applied later by the Jenkins pipeline.

⚙️ Setup

Prerequisites

Make sure the following are installed and running:

Docker

Git

Terraform

Minikube

kubectl

Ansible

Python 3.12+

1. Clone the Repository

git clone https://github.com/ABIRAJKUMAR/qr-generator-devops.git
cd qr-generator-devops

2. Start Minikube using Terraform

cd terraform
terraform init
terraform apply

Check the cluster:

minikube status
kubectl get nodes

3. Build the Jenkins Agent Image

From the project root:

docker build -t jenkins-agent-tools:latest -f Dockerfile.agent .

4. Run the Ansible Playbook

cd ansible
ansible-playbook playbook.yml

The playbook creates/manages the Jenkins Docker Agent.

5. Run Jenkins

Open:

http://localhost:8080

Create or configure a Jenkins Pipeline using the repository and Jenkinsfile/pipeline configuration.

6. Deploy with Jenkins

The Jenkins pipeline:

GitHub → Docker Build → Kubernetes Deploy → Verification

Kubernetes manifests are stored in:

k8s/deployment.yaml
k8s/service.yaml

🌐 Access the Application

After successful deployment:

minikube service qr-generator-service

The application runs on port 5000 inside the container and is exposed through a Kubernetes NodePort service.

🔍 Useful Commands

Minikube

minikube status
minikube start --driver=docker

Kubernetes

kubectl get nodes
kubectl get pods
kubectl get services
kubectl logs <pod-name>

Docker

docker ps
docker images

Terraform

terraform init
terraform apply
terraform destroy

Ansible

ansible-playbook playbook.yml

✅ Result

The project successfully demonstrates an automated local DevOps workflow where:

Source code is maintained in GitHub.

Jenkins executes the CI/CD pipeline.

Ansible manages the Jenkins Docker Agent.

Docker builds the application image.

Terraform starts the local Minikube environment.

Jenkins deploys the application to Kubernetes.

The QR Generator application runs through a Kubernetes NodePort Service.

🔮 Future Improvements

Deploy the application to AWS or another cloud platform.

Add automated unit/integration testing.

Add monitoring with Prometheus and Grafana.

Use Helm for Kubernetes deployments.

Add HTTPS and a custom domain.

Add webhook-based automatic Jenkins triggers.

👨‍💻 Author

Abiraj Kumar

DevOps CI/CD Project – QR Generator