pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8.5-alpine3.11'
                }
            }
            steps {
                sh 'python -m py_compile calculator.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}
