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
        sshagent(['node-0-cred']) {
          sh 'scp -r -o StrictHostKeyChecking=no playbook.yml service.yml deployment.yml root@94.26.239.183:/root/k8s'
          script {
            try {
            //  sh 'ssh root@94.26.239.183 kubectl apply -f /root/k8s/deployment.yaml /root/k8s/playbook.yml  /root/k8s/service.yml --kubeconfig=/root/.kube/config'
              sh 'ansible-playbook  playbook.yml --extra-vars $IMAGE_BASE:$IMAGE_TAG'
            } catch(error) { }
          }
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


