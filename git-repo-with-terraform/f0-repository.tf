resource "github_repository" "example" {
  name                   = "Practice_repo"
  description            = "The repo craeted using terraform and github token"
  visibility             = "private"
  allow_merge_commit     = true
  allow_rebase_merge     = true
  delete_branch_on_merge = false
  gitignore_template     = "JENKINS_HOME"
  //  https://github.com/github/gitignore
}