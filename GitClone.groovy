pipeline {
    agent any

    stages {
        stage('Git-Clone') {
            steps {
                echo 'Hello Cloning your git'
				git config --global --unset credential.helper
                git credentialsId: 'GitToken', url: 'https://github.com/vijayrmourya/_Projects'
                echo 'clone successful'
            }
        }
    }
}