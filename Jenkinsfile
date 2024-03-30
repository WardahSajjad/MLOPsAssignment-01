pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKERHUB_CREDENTIALS_ID = 'dockerCredentials-101'
        IMAGE_NAME = 'wardasajjad/mlops-assignment-01'
        TAG = 'latest'
    }

    stages {
        stage('Cloning Git Repository') {
            steps {
                // Assuming you want to checkout from Git; adjust as necessary
                git branch: 'main', url: 'https://github.com/WardahSajjad/MLOPsAssignment-01'
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
