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
        stage('Compile Entregable 2') {
            steps {
                dir("Entregable2"){
                    sh 'mvn package'
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
        stage('Deliver') {
            steps {
                dir("Entregable2"){
                    sh 'cp target/prog-app-1.0.jar ../'
                    echo 'menu.py can now be run'
                }
            }
        }
        stage('Send ok email') {
            steps {
                mail bcc: '', body: 'All is well with the latest pipline run', subject: 'Latest pipeline run', to: 'nsapriza1@correo.um.edu.uy'
            }
        }
    }
}