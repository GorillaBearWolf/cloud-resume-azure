"""Azure-hosted static cloud resume infrastructure"""

import pulumi
import pulumi_azure_native as azure_native

cloud_resume = azure_native.resources.ResourceGroup("cloud-resume",
    location="eastus",
    resource_group_name="cloud-resume",
    opts = pulumi.ResourceOptions(protect=True))
