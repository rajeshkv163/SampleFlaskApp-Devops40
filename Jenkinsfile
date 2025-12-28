pipeline {
    agent { label 'worker1' }

    stages { //collection of jobs
        stage ('Run the docker container'){ //job6
        steps{  
            sh 'docker rm -f webos'
            sh 'docker pull jinny1/sampleappdevops40'
            sh 'docker run -dit --name webos -p 80:80 jinny1/sampleappdevops40'
        }
        }
        
    }
}
