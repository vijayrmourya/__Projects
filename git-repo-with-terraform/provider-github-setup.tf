# Terraform Block
terraform {
  required_version = "~> 0.14" # which means any version equal & above 0.14 like 0.15, 0.16 etc and < 1.xx
}

provider "github" {
  token = var.git-token
  owner = var.git-owner
}
