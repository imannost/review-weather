pipeline {
  agent any
  environment{
    DOCKERHUB_CREDENTIALS = credentials('DockerHub')
    IMAGE_TAG = "v$BUILD_NUMBER"
    IMAGE_BASE = 'imannost/weather'
  }
  stages {
    stage('Build') {
      steps{
        sh 'docker build -t $IMAGE_BASE:$IMAGE_TAG .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Publish') {
      steps {
        sh 'docker push $IMAGE_BASE:$IMAGE_TAG'
      }
    }
    stage ('Deploy') {
      steps {
        withKubeConfig([credentialsId: 'kube-cred', serverUrl: 'https://94.26.239.183:6443']) {
          sh '''
          #!/bin/sh
          export DOCKER_IMAGE=$IMAGE_BASE:$IMAGE_TAG'
          '''
          sh 'envsubst < deployment.yml | kubectl apply -f -'
          sh 'envsubst < service.yml | kubectl apply -f -'
        }
      }
    }
  }
  post {
    always {
      sh 'docker logout'
      cleanWs()
    }
  }
}
