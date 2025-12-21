# Deploy NGINX on Minikube (Running Inside a VM)

This guide walks you through deploying **NGINX** on **Minikube** running inside a **Virtual Machine (VM)** (AWS EC2, VirtualBox, VMware, etc.). It is beginner-friendly and assumes basic Linux command-line knowledge.

---

##  Prerequisites

Make sure your VM has the following:

* Linux VM (Ubuntu 20.04+ recommended)
* At least **4 GB RAM** and **2 CPUs**
* Internet access
* User with `sudo` privileges

---

## 🔧 Step 1: Install Dependencies

### Update system

```bash
sudo apt update && sudo apt upgrade -y
```

### Install Docker

```bash
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```

Verify Docker:

```bash
docker --version
```

---

##  Step 2: Install kubectl

```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

Verify:

```bash
kubectl version --client
```

---

##  Step 3: Install Minikube

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube
```

Verify:

```bash
minikube version
```

---

##  Step 4: Start Minikube

### Use Docker as the driver (recommended for VMs)

```bash
minikube start --driver=docker
```

Check cluster status:

```bash
kubectl get nodes
```

---

##  Step 5: Deploy NGINX

### Create NGINX Deployment

```bash
kubectl create deployment nginx --image=nginx
```

Check deployment:

```bash
kubectl get deployments
kubectl get pods
```

---

##  Step 6: Expose NGINX Service

```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

Verify service:

```bash
kubectl get services
```

---

##  Step 7: Access NGINX

### Option 1: Using Minikube Service Command

```bash
minikube service nginx --url
```

Open the displayed URL in your browser.

---

### Option 2: Using kubectl port-forward (Best for VMs)

```bash
kubectl port-forward svc/nginx 8080:80
```

Now open in browser:

```
http://<VM_PUBLIC_IP>:8080
```

---

##  Verify Deployment

You should see the **NGINX Welcome Page** 🎉

Check logs if needed:

```bash
kubectl logs deployment/nginx
```

---

##  Cleanup

```bash
kubectl delete service nginx
kubectl delete deployment nginx
minikube stop
```

To delete cluster completely:

```bash
minikube delete
```

---

##  Common Issues & Fixes

###  minikube service not opening browser

Use `--url` flag or `kubectl port-forward` instead.

###  Docker permission denied

Run:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

###  VM Browser Access

Ensure VM security group allows inbound traffic on exposed port (e.g., 8080).

---

##  Notes

* For production use, prefer **Ingress + LoadBalancer**
* Minikube is for **development/testing only**

---

