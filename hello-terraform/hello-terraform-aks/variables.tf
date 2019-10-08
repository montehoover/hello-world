# execute the following with specified SP details to set these variables:
# export TF_VAR_client_id=
# export TF_VAR_client_secret=
variable "client_id" {}
variable "client_secret" {}

variable "instance_count" {
    default = 0
}

variable "agent_count" {
    default = 8
}

variable "ssh_public_key" {
    default = "~/.ssh/id_rsa.pub"
}

variable "dns_prefix" {
    default = "tf"
}

variable cluster_name {
    default = "tf"
}

variable resource_group_name {
    default = "rg"
}

variable location {
    default = "West Europe"
}

variable log_analytics_workspace_name {
    default = "testLogAnalyticsWorkspaceName"
}

# refer https://azure.microsoft.com/global-infrastructure/services/?products=monitor for log analytics available regions
variable log_analytics_workspace_location {
    default = "westeurope"
}

# refer https://azure.microsoft.com/pricing/details/monitor/ for log analytics pricing 
variable log_analytics_workspace_sku {
    default = "PerGB2018"
}

variable "virtual_network_name" {
  description = "Virtual network name"
  default     = "aksVirtualNetwork"
}

variable "virtual_network_address_prefix" {
  default     = "10.0.0.0/8"
}

variable "aks_subnet_name" {
  default     = "kubesubnet"
}

variable "aks_subnet_address_prefix" {
  default     = "10.240.0.0/16"
}