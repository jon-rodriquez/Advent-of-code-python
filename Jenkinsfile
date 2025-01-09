pipeline {
  agent {
    docker { image 'alpine:latest' }
  }
  stages {
    stage('Test') {
      steps {
        sh 'python3 --version'
      }
    }
  }
}
