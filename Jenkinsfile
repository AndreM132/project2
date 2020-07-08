pipeline{
    agent any
    stages {
        stage("Script Executable") {
            steps {
               sh "chmod +x ./script/*"
                  }
        }
        stage('Configuration and Installation') {
            steps{
                sh './script/install.sh'
                sh './script/ansible.sh'
                 }
        }    
        stage('Depoly Docker Compose') {
            steps{
                sh './script/dockerdeploy.sh'   
            }}
           }   
}
