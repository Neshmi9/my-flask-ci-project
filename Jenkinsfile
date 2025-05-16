pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-ci-app"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Static Code Testing') {
            steps {
                sh 'pip install flake8'
                sh 'export PATH=$PATH:~/.local/bin && flake8 app.py'
            }
        }

        stage('Dynamic Code Testing') {
            steps {
                sh 'pip install pytest'
                sh 'export PATH=$PATH:~/.local/bin && pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy to DEV') {
            steps {
                echo 'Deploying to DEV environment...'
                sh 'echo Simulated DEV deploy'
            }
        }

        stage('Deploy to PROD') {
            steps {
                input message: 'Deploy to PROD?'
                echo 'Deploying to PROD environment...'
                sh 'echo Simulated PROD deploy'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
