pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code...'
                checkout scm
            }
        }
        
        stage('Info') {
            steps {
                sh 'echo "System info:"'
                sh 'uname -a'
                sh 'docker --version'
                sh 'git --version'
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "🏗️ Building Docker image..."'
                sh 'docker build -t system-software-app:jenkins .'
            }
        }
        
        stage('Verify') {
            steps {
                sh 'echo "✅ Verifying image..."'
                sh 'docker images | grep system-software-app'
            }
        }
    }
}
