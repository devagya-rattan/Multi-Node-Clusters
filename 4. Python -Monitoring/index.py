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

"""
2. Create Deployments
"""

apps_v1 = AppsV1Api()

deployment = V1Deployment(
    metadata=V1ObjectMeta(name="my-python-app"),
    spec=V1DeploymentSpec(
        replicas=2,
        selector=V1LabelSelector(match_labels={"app": "my-python-app"}),
        template=V1PodTemplateSpec(
            metadata=V1ObjectMeta(labels={"app": "my-python-app"}),
            spec=V1PodSpec(containers=[
                V1Container(
                    name="python-container",
                    image="python:3.11-slim",
                    command=["python", "-m", "http.server"]
                )
            ])
        )
    )
)

