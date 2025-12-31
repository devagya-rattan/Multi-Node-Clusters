from kubernetes import client, config , watch
# Load config from default kubeconfig location (e.g. ~/.kube/config)
config.load_kube_config()
# Initialize the API client
v1 = client.CoreV1Api()

"""
1. List all pods 
"""
for pod in v1.list_pod_for_all_namespaces().items:
    print(f"{pod.metadata.namespace} | {pod.metadata.name}")

"""
2. Watch Real-Time Events
"""
w = watch.Watch()
for event in w.stream(v1.list_namespace):
    print(f"Event: {event['type']} {event['object'].metadata.name}")
