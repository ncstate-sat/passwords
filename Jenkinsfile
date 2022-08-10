pipeline {
    agent {
        label "BuiltIn-Agent"
    }
    
    stages {
        stage('Clone') {
            steps {
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
                    sh 'python3 -m twine upload --repository testpypi dist/\\* -u$PYPI_USERNAME -p$PYPI_PASSWORD'
                }
            }
        }
    }
}