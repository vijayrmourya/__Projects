pipeline {
    agent any

    stages {
        stage('Git-Clone') {
            steps {
                echo 'Hello Cloning your git'
				sh "git config --global --unset credential.helper"
				sh "ls -lrt"
                git credentialsId: 'GitToken', url: 'https://github.com/vijayrmourya/_Projects'
                echo 'clone successful'
            }
        }
    }
}