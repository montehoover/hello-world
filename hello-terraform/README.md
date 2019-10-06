1. Install Terraform: www.terraform.io
2. Download the Terraform modules for the cloud provider specified in hello.tf: `$ terraform init`
3. Create the environment variables required by Terraform: `$ source terraform_azure_vars.sh`
4. Run hello.tf: `$ terraform apply`