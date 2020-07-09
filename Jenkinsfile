pipeline{
    agent any
    stages {
        stage("Script Executable") {
            steps {
               sh "chmod +x ./script/*"
                  }
        }
        stage('Build') {
            steps{
                sh './script/build.sh'
                sh './script/ansible.sh'
            }
           }
        stage('Depoly Docker Compose') {
            steps{
                sh './script/deploy.sh'   
            }}
           }   
}
