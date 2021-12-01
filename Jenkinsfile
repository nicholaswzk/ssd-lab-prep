pipeline {

    agent any

    environment { 
        CI = 'true'
    }

    stages {
        stage('Build') {
		steps {
			script {
				echo '-------- Performing Build Stage --------'
                	}
           	}
	}
        stage('SonarQube Analysis') {
            steps {
                script {
                    echo '-------- Performing SonarQube Scan --------'
                    def scannerHome = tool 'ict3x03_SonarQube_Scanner';
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                       echo "SonarQube Analysis has no errors! Proceeding on!"
                }
             }
	 }
        stage('OWASP Dependency Check') {
			steps {
			    echo '-------- Performing OWASP Dependency Check --------'
				dependencyCheck additionalArguments: '--disableYarnAudit --format HTML --format XML', odcInstallation: 'Default'
				dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                echo "OWASP DependencyCheck has no errors! Proceeding on!"
			}
		}
    }
}
