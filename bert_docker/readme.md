# Expose a chatbot using a simple python web server

## Build and save docker image to local registry

`docker run -d -p 5000:5000 --restart=always --name registry registry:2`

`docker build . -t localhost:5000/bert_qa`

`docker push localhost:5000/bert_qa`

## Deploy to kubernetes as a pod

`Kubectl create -f pod.yaml`
*Port forwarding*

`kubectl port-forward --address 0.0.0.0 pod/bert-pod 8501:8501`

*Accepts requests as a json*

`curl -d '{"context": "Salad. This is a vegan meal", "question": "is this meal vegan?"}' -X POST <ip_address>:8501`
