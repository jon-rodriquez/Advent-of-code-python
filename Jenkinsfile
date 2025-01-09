pipeline {
  agent {
    docker { image 'alpine' }
  }
  stages {
    stage('Test') {
      steps {
        sh 'python3 --version'
      }
    }
  }
}
