pipeline {
    agent any

    environment {
        API_TOKEN = credentials('pypi_api_token')
    }

    stages {
        stage('Build') {
            steps {
                sh "python3.9 -m pip install -U build"
                sh "python3.9 -m build"
                sh "python3.9 -m pip install -U twine"
                sh 'python3.9 -m twine upload --repository testpypi dist/\* -u%__token__% -p%API_TOKEN%'
            }
        }
    }
}