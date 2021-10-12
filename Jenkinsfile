pipeline {
  agent any
  stages {
    stage('Building image') {
      steps{
        sh 'docker build -t imannost/weather .'
      }
    }
    stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DockerHubPassword', usernameVariable: 'DockerHubUser')]) {
          sh "docker login -u ${env.DockerHubUser} -p ${env.DockerHubPassword}"
          sh 'docker push imannost/weather:latest'
        }
      }
    }
  }
}

