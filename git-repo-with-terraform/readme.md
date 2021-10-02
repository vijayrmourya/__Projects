## <b><u><i>git-repo-with-terraform (GitHub-Terraform PROJECT)</b></u></i>
***
<b> To create and manage GitHub repository using terraform provider and github token.</b>

- f0-repository.tf: to define all repo details like name, description and privacy etc.
- output.tf: to define all the reference attributes as the output
- provider-github-setup.tf: terraform and GitHub provider setup
- variable-github-token.tf: to keep secrets of the github and refer in repo creation and keeping it in gitignore to keep it local 
  (this secret sharing is for a local/personal repo we need to use other methods like hashicorp vault when the repo is going to be managed by a team)
***

## <b><u>Commands:</b></u>
***
- terraform init
- terraform fmt
- terraform validate
- terraform plan
- terraform apply -auto-approve
- terraform output > output.txt
- terraform destroy -auto-approve
***
