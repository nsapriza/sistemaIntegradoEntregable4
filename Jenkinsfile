pipeline {
    agent any
    stages {
        stage('Build Entregable 2') { 
            steps {
                dir("Entregable2"){
                    sh 'mvn -B -DskipTests clean package'
                } 
            }
        }
        stage('Test Entregable 2') {
            steps {
                dir("Entregable2"){
                    sh 'mvn test'
                }
            }
        }
        stage('Test Entregable 1') {
            steps {
                    sh 'python3 Entregable1/tests.py'
            }
        }
        stage('Test Entregable 3') {
            steps {
                    sh 'python3 Entregable3/test.py'
            }
        }
        // stage('Deliver') {
        //     steps {
        //         sh './jenkins/scripts/deliver.sh'
        //     }
        // }
    }
}