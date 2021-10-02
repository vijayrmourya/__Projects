output "repo-name" {
  value = github_repository.example.full_name
}

output "repo-url" {
  value = github_repository.example.html_url
}

output "SSH-clone-url" {
  value = github_repository.example.ssh_clone_url
}

output "HTTP-clone-url" {
  value = github_repository.example.http_clone_url
}

output "git-clone-url" {
  value = github_repository.example.git_clone_url
}

output "repository-visibility" {
  value = github_repository.example.visibility
}
