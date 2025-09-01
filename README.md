# guestbook-ui-workflow

Steps 1: 
```
eksctl create cluster -f /Users/ranjiniganeshan/udemy/Argocd/dev-cluster.yaml
```
```
eksctl create cluster -f /Users/ranjiniganeshan/udemy/Argocd/dev-cluster.yaml
2025-09-01 15:27:34 [ℹ]  eksctl version 0.212.0
2025-09-01 15:27:34 [ℹ]  using region us-east-1
2025-09-01 15:27:34 [!]  Amazon EKS will no longer publish EKS-optimized Amazon Linux 2 (AL2) AMIs after November 26th, 2025. Additionally, Kubernetes version 1.32 is the last version for which Amazon EKS will release AL2 AMIs. From version 1.33 onwards, Amazon EKS will continue to release AL2023 and Bottlerocket based AMIs. The default AMI family when creating clusters and nodegroups in Eksctl will be changed to AL2023 in the future.
2025-09-01 15:27:36 [ℹ]  setting availability zones to [us-east-1c us-east-1f]
2025-09-01 15:27:36 [ℹ]  subnets for us-east-1c - public:192.168.0.0/19 private:192.168.64.0/19
2025-09-01 15:27:36 [ℹ]  subnets for us-east-1f - public:192.168.32.0/19 private:192.168.96.0/19
2025-09-01 15:27:37 [ℹ]  nodegroup "ng-1" will use "ami-05a4569e0854a2c75" [AmazonLinux2/1.32]
2025-09-01 15:27:38 [ℹ]  using Kubernetes version 1.32
2025-09-01 15:27:38 [ℹ]  creating EKS cluster "dev21-argocd-cluster" in "us-east-1" region with un-managed nodes
2025-09-01 15:27:38 [ℹ]  1 nodegroup (ng-1) was included (based on the include/exclude rules)
2025-09-01 15:27:38 [ℹ]  will create a CloudFormation stack for cluster itself and 1 nodegroup stack(s)
2025-09-01 15:27:38 [ℹ]  if you encounter any issues, check CloudFormation console or try 'eksctl utils describe-stacks --region=us-east-1 --cluster=dev21-argocd-cluster'
2025-09-01 15:27:38 [ℹ]  Kubernetes API endpoint access will use default of {publicAccess=true, privateAccess=false} for cluster "dev21-argocd-cluster" in "us-east-1"
2025-09-01 15:27:38 [ℹ]  CloudWatch logging will not be enabled for cluster "dev21-argocd-cluster" in "us-east-1"
2025-09-01 15:27:38 [ℹ]  you can enable it with 'eksctl utils update-cluster-logging --enable-types={SPECIFY-YOUR-LOG-TYPES-HERE (e.g. all)} --region=us-east-1 --cluster=dev21-argocd-cluster'
2025-09-01 15:27:38 [ℹ]  default addons metrics-server, vpc-cni, kube-proxy, coredns were not specified, will install them as EKS addons
2025-09-01 15:27:38 [ℹ]  
2 sequential tasks: { create cluster control plane "dev21-argocd-cluster", 
    2 sequential sub-tasks: { 
        2 sequential sub-tasks: { 
            1 task: { create addons },
            wait for control plane to become ready,
        },
        create nodegroup "ng-1",
    } 
}
2025-09-01 15:27:38 [ℹ]  building cluster stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:27:39 [ℹ]  deploying stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:28:09 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:28:41 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:29:42 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:30:43 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:31:44 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:32:45 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:33:52 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:34:53 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:35:55 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-cluster"
2025-09-01 15:36:00 [ℹ]  creating addon: metrics-server
2025-09-01 15:36:00 [ℹ]  successfully created addon: metrics-server
2025-09-01 15:36:02 [!]  recommended policies were found for "vpc-cni" addon, but since OIDC is disabled on the cluster, eksctl cannot configure the requested permissions; the recommended way to provide IAM permissions for "vpc-cni" addon is via pod identity associations; after addon creation is completed, add all recommended policies to the config file, under `addon.PodIdentityAssociations`, and run `eksctl update addon`
2025-09-01 15:36:02 [ℹ]  creating addon: vpc-cni
2025-09-01 15:36:02 [ℹ]  successfully created addon: vpc-cni
2025-09-01 15:36:03 [ℹ]  creating addon: kube-proxy
2025-09-01 15:36:04 [ℹ]  successfully created addon: kube-proxy
2025-09-01 15:36:04 [ℹ]  creating addon: coredns
2025-09-01 15:36:05 [ℹ]  successfully created addon: coredns
2025-09-01 15:38:09 [ℹ]  building nodegroup stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:38:12 [ℹ]  deploying stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:38:12 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:38:43 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:39:28 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:41:20 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:42:38 [ℹ]  waiting for CloudFormation stack "eksctl-dev21-argocd-cluster-nodegroup-ng-1"
2025-09-01 15:42:38 [ℹ]  waiting for the control plane to become ready
2025-09-01 15:42:38 [✔]  saved kubeconfig as "/Users/ranjiniganeshan/.kube/config"
2025-09-01 15:42:38 [ℹ]  no tasks
2025-09-01 15:42:38 [✔]  all EKS cluster resources for "dev21-argocd-cluster" have been created
2025-09-01 15:42:40 [ℹ]  nodegroup "ng-1" has 2 node(s)
2025-09-01 15:42:40 [ℹ]  node "ip-192-168-2-92.ec2.internal" is ready
2025-09-01 15:42:40 [ℹ]  node "ip-192-168-32-137.ec2.internal" is ready
2025-09-01 15:42:40 [ℹ]  waiting for at least 2 node(s) to become ready in "ng-1"
2025-09-01 15:42:40 [ℹ]  nodegroup "ng-1" has 2 node(s)
2025-09-01 15:42:40 [ℹ]  node "ip-192-168-2-92.ec2.internal" is ready
2025-09-01 15:42:40 [ℹ]  node "ip-192-168-32-137.ec2.internal" is ready
2025-09-01 15:42:40 [✔]  created 1 nodegroup(s) in cluster "dev21-argocd-cluster"
2025-09-01 15:42:41 [ℹ]  kubectl command should work with "/Users/ranjiniganeshan/.kube/config", try 'kubectl get nodes'
2025-09-01 15:42:41 [✔]  EKS cluster "dev21-argocd-cluster" in "us-east-1" region is ready

```
