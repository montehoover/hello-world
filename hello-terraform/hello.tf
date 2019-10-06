provider "azurerm" {
}
resource "azurerm_resource_group" "rg" {
        name = "helloTerraform"
        location = "westeurope"
}