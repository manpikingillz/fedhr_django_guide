pipeline {
 agent any
 environment {
    RELEASE='20'
 }

 stages {
  stage('Checkout') {
    agent any
    environment {
        LOCAL_ENV='yes'
    }
    steps {
        sh "echo This is the first stage from. Release is ${RELEASE} and ${LOCAL_ENV}"
    }

  }
 }
}
