terraform {
  backend "azurerm" {}
  }
provider "azurerm" {
  features {}
}
data "azurerm_subscription" "current"{}

locals {
  base_name = "${var.my_name}-${var.environment}"
  network_base_name = "${local.base_name}-ntwrk"

}

resource "azurerm_resource_group" "myresgroup" {
  name     =  "${local.network_base_name}-rg"
  location = var.location
}

resource "azurerm_virtual_network" "myvnet" {
  name                =  "${local.network_base_name}-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.myresgroup.location
  resource_group_name = azurerm_resource_group.myresgroup.name
  
}
resource "azurerm_subnet" "subnet" {
    name = "${azurerm_virtual_network.myvnet.name}-vms-snet"
    resource_group_name = azurerm_resource_group.myresgroup.name
    virtual_network_name = azurerm_virtual_network.myvnet.name
    address_prefixes = [ "10.0.2.0/24" ]
  
}
 module "vm" {
source = "./vm_module"
base_name = local.base_name
location = var.location
 vms_subnet_id= azurerm_subnet.subnet.id
  my_public_ip=var.my_public_ip
   my_password=var.my_password
}
