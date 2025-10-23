pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                bat 'echo "📥 Загружаем код из GitHub..."'
                git branch: 'main', url: 'https://github.com/Fokin05/system-software-project.git'
            }
        }
        
        stage('Build') {
            steps {
                bat 'echo "🏗️ Собираем Docker образ..."'
                bat 'docker build -t system-software-app:jenkins .'
            }
        }
        
        stage('Test') {
            steps {
                bat 'echo "🧪 Тестируем приложение..."'
                bat 'docker images | findstr "system-software-app"'
            }
        }
    }
    
    post {
        always {
            bat 'echo "✅ Сборка завершена!"'
        }
    }
}
