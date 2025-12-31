from kubernetes import client, config
# Load config from default kubeconfig location (e.g. ~/.kube/config)
config.load_kube_config()
# Initialize the API client
v1 = client.CoreV1Api()
for pod in v1.list_pod_for_all_namespaces().items:
    print(f"{pod.metadata.namespace} | {pod.metadata.name}")