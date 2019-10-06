#!/bin/sh
echo "Setting environment variables for Terraform"
export ARM_SUBSCRIPTION_ID=c18d96e9-f9b1-4b9e-81c6-954ac48f67df
export ARM_CLIENT_ID=8da5f11e-b9b3-4cd7-904e-f9eb8de261d6
export ARM_CLIENT_SECRET=8005acd5-9746-4eff-bfd5-e940863fc0b8
export ARM_TENANT_ID=72f988bf-86f1-41af-91ab-2d7cd011db47

# Not needed for public, required for usgovernment, german, china
export ARM_ENVIRONMENT=public
