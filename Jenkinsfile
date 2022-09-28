pipeline {
    agent {
        label "BuiltIn-Agent"
    }

    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }

    environment {
        TWINE_REPOSITORY_URL = "https://pypi.ehps.ncsu.edu"
    }
    
    stages {
        stage('Clone') {
            steps {
                cleanWs()
                git branch: 'main',
                    url: 'https://github.com/ncstate-sat/passwords.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'python3 -m build ./passwords'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'jenkins-pypi-api-token',
                    usernameVariable: 'PYPI_USERNAME',
                    passwordVariable: 'PYPI_PASSWORD'
                )]) {
                    sh 'python3 -m pip install -U twine'
                    sh 'python3 -m twine upload ./passwords/dist/\\* -u$PYPI_USERNAME -p$PYPI_PASSWORD'
                }
            }
        }
    }
}