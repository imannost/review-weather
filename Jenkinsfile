pipeline {
  agent any
  environment{
    DOCKERHUB_CREDENTIALS = credentials('DockerHub')
  }
  stages {
    stage('Build') {
      steps{
        sh 'docker build -t imannost/weather:v1.0 .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push imannost/weather:v1.0'
      }
    }
    stage ('Deploy') {
           steps {
               script{
                   sh "ansible-playbook  playbook.yml --extra-vars imannost/weather:v1.0"
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


