# Desired clusters:
# 1. basic default (kublet, vmas)
# 2. VMAS, Azure CNI w/ virtual node w/ autoscaling example https://github.com/Azure-Samples/virtual-node-autoscale
# 3. VMSS, Azure CNI, standared sku load balancer https://docs.microsoft.com/en-us/azure/aks/load-balancer-standard
# 4. VMSS, Azure CNI, standard sku load balancer, multiple node pools, Windows
# 5. VMSS, Azure CNI, standard sku load balancer, multiple node pools, Windows, autoscaler https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler
# 6. VMSS, Azure CNI, standard sku load balancer, multiple node pools, Windows, autoscaler, internal load balancer https://docs.microsoft.com/en-us/azure/aks/internal-lb
# 7. VMSS, Azure CNI, standard sku load balancer, multiple node pools, Windows, autoscaler, internal load balancer, nginx ingress controller https://docs.microsoft.com/en-us/azure/aks/ingress-basic
# 8. VMSS, Azure CNI, standard sku load balancer, multiple node pools, Windows, autoscaler, internal load balancer, http application routing https://docs.microsoft.com/en-us/azure/aks/http-application-routing
# 9. AAD-enabled https://docs.microsoft.com/en-us/azure/aks/azure-ad-integration-cli
# 10. Custom coreDNS https://docs.microsoft.com/en-us/azure/aks/coredns-custom

resource "azurerm_resource_group" "k8s" {
    name     = "${var.resource_group_name}"
    location = "${var.location}"
}

resource "random_id" "log_analytics_workspace_name_suffix" {
    byte_length = 8
}

resource "azurerm_log_analytics_workspace" "test" {
    # The WorkSpace name has to be unique across the whole of azure, not just the current subscription/tenant.
    name                = "${var.log_analytics_workspace_name}-${random_id.log_analytics_workspace_name_suffix.dec}"
    location            = "${var.log_analytics_workspace_location}"
    resource_group_name = "${azurerm_resource_group.k8s.name}"
    sku                 = "${var.log_analytics_workspace_sku}"
}

resource "azurerm_log_analytics_solution" "test" {
    solution_name         = "ContainerInsights"
    location              = "${azurerm_log_analytics_workspace.test.location}"
    resource_group_name   = "${azurerm_resource_group.k8s.name}"
    workspace_resource_id = "${azurerm_log_analytics_workspace.test.id}"
    workspace_name        = "${azurerm_log_analytics_workspace.test.name}"

    plan {
        publisher = "Microsoft"
        product   = "OMSGallery/ContainerInsights"
    }
}

resource "azurerm_kubernetes_cluster" "k8s" {
    count               = "${var.instance_count}"
    name                = "${var.cluster_name}-${count.index}"
    location            = "${azurerm_resource_group.k8s.location}"
    resource_group_name = "${azurerm_resource_group.k8s.name}"
    dns_prefix          = "${var.dns_prefix}"

    network_profile {
        network_plugin     = "azure"
    }

    agent_pool_profile {
        name            = "agentpool"
        count           = "${var.agent_count}"
        vm_size         = "Standard_DS2_v2"
        os_type         = "Linux"
        os_disk_size_gb = 30
        type            = "VirtualMachineScaleSets"
        vnet_subnet_id  = "${azurerm_subnet.kubesubnet.id}"
    }

    linux_profile {
        admin_username = "azureuser"

        ssh_key {
            key_data = "${file("${var.ssh_public_key}")}"
        }
    }

    service_principal {
        client_id     = "${var.client_id}"
        client_secret = "${var.client_secret}"
    }

    addon_profile {
        oms_agent {
        enabled                    = true
        log_analytics_workspace_id = "${azurerm_log_analytics_workspace.test.id}"
        }
    }

    tags = {
        Environment = "Development"
    }
}

resource "azurerm_virtual_network" "test" {
  name                = "${var.virtual_network_name}"
  location            = "${azurerm_resource_group.k8s.location}"
  resource_group_name = "${azurerm_resource_group.k8s.name}"
  address_space       = ["${var.virtual_network_address_prefix}"]

  subnet {
    name           = "${var.aks_subnet_name}"
    address_prefix = "${var.aks_subnet_address_prefix}" 
  }

}

resource "azurerm_subnet" "kubesubnet" {
  name                  = "${var.aks_subnet_name}"
  virtual_network_name  = "${azurerm_virtual_network.test.name}"
  resource_group_name   = "${azurerm_resource_group.k8s.name}"
  address_prefix        = "${var.aks_subnet_address_prefix}" 
}