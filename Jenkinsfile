pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "koduro"
        IMAGE_NAME = "kofioduro.py"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Kofi Oduro - Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Kofi Oduro - Login to Dockerhub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                }
            }
        }

        stage('Kofi Oduro - Push image to Dockerhub') {
            steps {
                script {
                    sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}