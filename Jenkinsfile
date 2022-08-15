pipeline {
    agent {
        label "BuiltIn-Agent"
    }

    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
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
                sh 'flit build'
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
                    sh 'python3 -m twine upload dist/\\* -u$PYPI_USERNAME -p$PYPI_PASSWORD'
                }
            }
        }
    }
}