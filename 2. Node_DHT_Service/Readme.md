# 🚀 Deploy a Node.js App on Minikube with Prometheus & Grafana Monitoring

This README explains how to:

* Deploy a **Node.js application** on **Kubernetes (Minikube)**
* Expose the app using a Kubernetes Service
* Monitor the app and cluster using **Prometheus**
* Visualize metrics using **Grafana**

This setup is ideal for **learning DevOps, Kubernetes monitoring, and local testing inside a VM**.

---

##  Prerequisites

Your VM should have:

* Ubuntu 20.04+ (or similar Linux)
* 2 CPU cores, 4 GB RAM (recommended)
* Internet access
* sudo privileges

Installed tools:

* Docker
* kubectl
* Minikube

## 🟢 Step 1: Create Node.js App as provided in folder
Index.js(file)

## 🐳 Step 2: Dockerize the App as provided in folder
Output:
<img width="1919" height="883" alt="dockerhub_push" src="https://github.com/user-attachments/assets/be2adb88-fcd2-4ba9-af03-47947be82590" />
<img width="1157" height="982" alt="docker_smoke" src="https://github.com/user-attachments/assets/b150c687-1585-41da-ac32-1564de81aaf2" />
DockerHub:
<img width="1481" height="38" alt="image_smoke" src="https://github.com/user-attachments/assets/0aa7f703-a3fd-41e3-b1d0-4646f920bc82" />
## ☸️ Step 3: Kubernetes Deployment
Output:
<img width="1706" height="924" alt="k8s_smoke" src="https://github.com/user-attachments/assets/591102a6-21e6-420e-9cc1-f792fccc09d9" />
## 🌐 Step 4: Expose the App Ports
Output:
<img width="1553" height="381" alt="smokeVm_rules" src="https://github.com/user-attachments/assets/64ad8ca4-5b27-4cf6-9f3d-3d13181ce989" />
<img width="1592" height="895" alt="webpage+smoke" src="https://github.com/user-attachments/assets/ca9deed1-36e7-4180-9bbb-b594e335b301" />

## 📊 Step 5: Install Prometheus & Grafana (Helm)
Follow This link https://www.devopshint.com/monitor-kubernetes-cluster-using-prometheus-and-grafana/#google_vignette

## 🔍 Step 6: Configure Prometheus to Scrape Node.js Metrics
Follow This link https://www.devopshint.com/monitor-kubernetes-cluster-using-prometheus-and-grafana/#google_vignette

Output:
<img width="1916" height="979" alt="promethus_1" src="https://github.com/user-attachments/assets/3f973662-3d1b-4c58-aba4-40d80635bf0c" />
<img width="1370" height="860" alt="smokek8s" src="https://github.com/user-attachments/assets/d3118ba3-cb84-4a2f-934c-891a7b38a029" />





