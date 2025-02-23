# Provider configuration
provider "azurerm" {
    features {}
}

# Create resource group
resource "azurerm_resource_group" "backup_rg" {
    name = "backup-resources-rg"
    location = "eastus"
}

# Create backup vault
resource "azurerm_data_protection_backup_vault" "backup_vault" {
    name                    = "backup-vault"
    resource_group_name     = azurerm_resource_group.backup_rg.name
    location                = azurerm_resource_group.backup_rg.location
    datastore_type          = "VaultStore"
    redundancy              = "LocallyRedundant"
}