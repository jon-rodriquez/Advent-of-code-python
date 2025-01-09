pipeline {
  agent {
    docker { image 'ubuntu:24.04' }
  }
  stages {
    stage('Test') {
      steps {
        sh 'python3 --version'
      }
    }
  }
}
