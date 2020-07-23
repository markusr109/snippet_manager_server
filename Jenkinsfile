pipeline {
  agent any
  environment {
    SERVICE = 'snippets'
    PARAMETER_FILE = 'infrastructure/ecs-combined-settings.properties'
  }
  stages {
    stage('Build/Push') {
      steps {
        sh 'aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 884483681943.dkr.ecr.eu-central-1.amazonaws.com'
        sh 'docker build -t $SERVICE-$GIT_BRANCH .'
        sh 'docker tag $SERVICE-$GIT_BRANCH:latest 884483681943.dkr.ecr.eu-central-1.amazonaws.com/$SERVICE-$GIT_BRANCH:latest'
        sh 'docker push 884483681943.dkr.ecr.eu-central-1.amazonaws.com/$SERVICE-$GIT_BRANCH:latest'
      }
    }

    stage('Deploy') {
      steps {
        sh 'cat infrastructure/ecs-settings-$GIT_BRANCH.properties infrastructure/ecs-settings-common.properties > $PARAMETER_FILE'
        sh 'aws cloudformation deploy --stack-name $SERVICE-$GIT_BRANCH --template-file infrastructure/ecs.yml --parameter-overrides $(envsubst < $PARAMETER_FILE)'
        sh 'aws ecs update-service --force-new-deployment --service $SERVICE-$GIT_BRANCH --cluster dev'
      }
    }

    stage('Clean-Up ECR') {
      steps {
        sh 'aws ecr batch-delete-image --repository-name $SERVICE-$GIT_BRANCH --image-ids "$(aws ecr list-images --repository-name $SERVICE-$GIT_BRANCH --filter tagStatus=UNTAGGED --query=imageIds[*] --output json)" || true'
      }
    }

  }
}