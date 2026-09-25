pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out GitHub repository...'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker images...'
                bat 'docker-compose build'
            }
        }

       stage('Docker Run') {
    steps {
        echo 'Stopping old containers...'
        bat 'docker-compose down --remove-orphans'

        echo 'Starting Docker containers...'
        bat 'docker-compose up -d'
    }
}

        stage('Check Containers') {
            steps {
                echo 'Checking running containers...'
                bat 'docker-compose ps'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL!'
        }
        failure {
            echo 'BUILD FAILED - Check the console output.'
        }
    }
}