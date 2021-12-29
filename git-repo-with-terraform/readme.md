## <b><u><i>git-repo-with-terraform (GitHub-Terraform PROJECT)</b></u></i>

***
<b> To create and manage GitHub repository using terraform provider and github token.</b>

- <b>f0-repository.tf:</b>
  to define all repo details like name, description and privacy etc.

- <b>output.tf:</b>
  to define all the reference attributes as the output

- <b>provider-github-setup.tf:</b>
  terraform and GitHub provider setup

- <b>variable-github-token.tf:</b>
  file is not added in git, it keeps secrets of the github and refer in repo creation and keeping it in gitignore to
  keep it local
  <b><i>(this secret sharing method is for a local/personal repo we need to use other methods like hashicorp vault/AWS secrets manager when
  the repo is going to be managed by a team)</i></b>

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
