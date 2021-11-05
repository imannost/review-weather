pipeline {
  agent any
  environment{
    DOCKERHUB_CREDENTIALS = credentials('DockerHub')
    IMAGE_TAG = 'v$BUILD_NUMBER'
    IMAGE_BASE = 'imannost/weather'
    IMAGE_NAME = '$IMAGE_BASE:$IMAGE_TAG'
  }
  stages {
    stage('Build') {
      steps{
        sh 'docker build -t $IMAGE_NAME .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Publish') {
      steps {
        sh 'docker push $IMAGE_NAME'
      }
    }
    stage ('Deploy') {
      steps {
        withKubeConfig([credentialsId: 'jenkins-deployer-credentials', serverUrl: 'http://94.26.239.183']) {
          sh 'ansible-playbook  playbook.yml --extra-vars $IMAGE_NAME'
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


