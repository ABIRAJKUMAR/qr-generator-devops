terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
  }
}

provider "null" {}

resource "null_resource" "minikube" {

  provisioner "local-exec" {
    command = "minikube start --driver=docker"
  }

  provisioner "local-exec" {
    command = "kubectl get nodes"
  }
}