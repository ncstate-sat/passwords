pipeline {
    agent any

    environment {
        API_TOKEN = credentials('jenkins-pypi-api-token')
    }

    stages {
        stage('Build') {
            steps {
                sh "flit build"
                sh "python3 -m pip install -U twine"
                sh 'python3 -m twine upload --repository testpypi dist/\\* -u$API_TOKEN_USR -p$API_TOKEN_PSW --verbose'
            }
        }
    }
}