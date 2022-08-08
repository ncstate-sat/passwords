pipeline {
    agent any

    environment {
        API_TOKEN = credentials('jenkins-pypi-api-token')
    }

    stages {
        stage('Build') {
            steps {
                sh "python3.9 -m pip install -U build"
                sh "python3.9 -m build"
                sh "python3.9 -m pip install -U twine"
                sh 'python3.9 -m twine upload --repository testpypi dist/\\* -u$API_TOKEN_USR -p$API_TOKEN_PSW --verbose'
            }
        }
    }
}