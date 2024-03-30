pipeline {
    agent any
// checking jenkins pipeline
    environment {
        // Define environment variables
        DOCKERHUB_CREDENTIALS_ID = 'dockerCredentials-101'
        IMAGE_NAME = 'wardasajjad/mlops-assignment-01'
        TAG = 'latest'
    }

    agent any
    stages {
        stage('Cloning Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/WardahSajjad/MLOPsAssignment-01'
            }
        }

    stages {
        stage('Checkout') {
            steps {
                // Checkout source code from the SCM
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS_ID) {
                        // Push the image to Docker Hub
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    // Optional: Clean up the built image from the Jenkins agent
                    sh "docker rmi ${IMAGE_NAME}:${TAG}"
                }
            }
        }
    }

    post {
        success {
            // Actions to take if the pipeline succeeds
            mail to: 'wardasajjad54@gmail.com',
                 subject: "Success: Pipeline for ${IMAGE_NAME}:${TAG}",
                 body: "The pipeline has successfully built and pushed the Docker image."
        }
        failure {
            // Actions to take if the pipeline fails
            mail to: 'wardasajjad54@gmail.com',
                 subject: "Failure: Pipeline for ${IMAGE_NAME}:${TAG}",
                 body: "The pipeline has failed. Please check Jenkins for more details."
        }
    }
}
