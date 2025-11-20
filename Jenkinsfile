pipline {
   agent any 

   environment {
       PROJECT_NAME = 'devopsfastapi'
       DOCKER_HOST = 'tcp://localhost:2375'
   }

   stages {
       stage('Checkout') {
           steps {
               checkout scm
               echo 'code recupere du repository Git'
           }
       } 

       stage('Test Users Service') {

           steps {
               echo 'lancement des tests users service...'
               sh '''
                    cd users-service
                    python -m venv venv
                    source venv/bin/activate
                    pip install -r requirement.txt
                    pytest tests/ -v
               '''
           } 
       } 
    
       stage('Build Docker Images') { 
           steps { 
               echo 'Construction des images Docker...'
               sh '''
                   cd users-service 
                   docker build -t users-service:latest .

                   cd ../product-service
                   docker build -t products-service:latest .
      
                   cd ../order-service
                   docker build -t order-service:latest .
               ''' 
           } 
       } 

       stage('Deploy to swarm') {
           steps { 
               echo 'deploiment sur docker swarm...'
               sh '''             
                   docker swarm init --advertise-addr 127.0.0.1 2>/dev/null || true 
                   docker stack deploy -c docker-compose.swarm.yml --with-registry-auth ${PROJECT_NAME}'
                 
                   echo "status des services:"
                   docker service ls
               '''
           }
       }
     
       stage('health check') {
           steps {
               echo 'verification de la santé des services...'
               sh '''
                   sleep 30
                   curl -f http://localhost/users/ || echo "service users non encore prét"

                   curl -f http://localhost/ || echo "service principal non encore prét" 

               '''
          } 
       }  
   }  
  
   post { 
       always { 
           echo 'nettoyage...'
           sh ''' 
               echo "service deployés:"
               docker service ls
               echo "conteneur en cours:"
               docker ps
           '''
       }   
       success { 
           echo 'deploiment reussi!'
           sh '''

               echo "dep Devopsfastapi reussi"
               echo "acceder a l'appliquation: http://localhost"
               echo "accedez a users service: http://localhost/users/"
           ''' 
       } 
       failure { 
           echo 'echec du pipline'
           sh ''' 
               echo "deppanage:"
               docker service ls
               docker ps -a 
           ''' 
       }   
   }    
}
