apiVersion: apps/v1
kind: Deployment
metadata:
  name: hpa-demo-deployment
  labels:
    app: hpa-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hpa-nginx
  template:
    metadata:
      labels:
        app: hpa-nginx
    spec:
      containers:
      - name: hpa-nginx
        image: stacksimplify/kubenginx:1.0.0
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "500Mi"
            cpu: "200m"          
---
apiVersion: v1
kind: Service
metadata:
  name: hpa-demo-service-nginx
  labels:
    app: hpa-nginx
spec:
  type: LoadBalancer
  selector:
    app: hpa-nginx
  ports:
  - port: 80
    targetPort: 80