1. Install Terraform: www.terraform.io
2. Download the Terraform modules for the cloud provider specified in main.tf: `$ terraform init`
3. Optionally, create a plan file to be executed: `$ terraform plan -out out.plan`
3. Run configurations in main.tf, k8s.tf, and variables.tf: `$ terraform apply`