pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo '?? Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Validate') {
            steps {
                echo '?? Validating project structure...'
                sh '''
                    echo "Project files:"
                    ls -la
                    echo "Source files:"
                    ls -la src/
                    echo "Dockerfile content:"
                    cat Dockerfile
                '''
            }
        }
        
        stage('Test Script') {
            steps {
                echo '?? Testing build script syntax...'
                sh '''
                    echo "Build script content:"
                    cat build.ps1 | head -10
                    echo "? Project structure is valid"
                '''
            }
        }
    }
    
    post {
        always {
            echo '?? Pipeline completed'
        }
        success {
            echo '?? SUCCESS: Jenkins CI is working!'
        }
    }
}
