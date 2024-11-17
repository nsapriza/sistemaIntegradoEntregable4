pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                dir("Entregable2"){
                    sh 'mvn -B -DskipTests clean package'
                } 
            }
        }
        stage('Test') {
            steps {
                dir("Entregable2"){
                    sh 'mvn test'
                }
            }
        }
        // stage('Deliver') {
        //     steps {
        //         sh './jenkins/scripts/deliver.sh'
        //     }
        // }
    }
}