pipeline {
    agent any

    stages {

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                bat 'pip install flake8'
                bat 'flake8 .'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }
    }
}