import boto3, sys, re

r53 = boto3.client('route53')

def collectHealthCheckArgs(*args):

    return createHealthCheck(CallerReference=args[0], **kwargs)
  
    
def createHealthCheck(**kwargs):

    return r53.create_health_check(**kwargs) 

if __name__ == "__main__":
  
    args = [val for val in sys.argv[1:]]
    if len(args) != 6:
          print("\nPlease use format:\n\n\t 'JobName' 'IPAddress|fqdn' 'Port'" \
              "'Type' 'ResourcePath''FailureThreshold'")                        
          print("\n\tExample => Job1 54.19.13.3  80 HTTP  / 4\n")
    else:
        #pattern match ip address 
        pattern = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

        if re.search(pattern,  args[1]):
            response = collectHealthCheckArgs(*args)
            kwargs = {'HealthCheckConfig':{
                'IPAddress': args[1],'Port': int(args[2]), 'Type': args[3],
                'ResourcePath': args[4],'FailureThreshold': int(args[5])
            }}
            response = collectHealthCheckArgs(*args)
        else:
            kwargs = {'HealthCheckConfig':{
                'FullyQualifiedDomainName': args[1],'Port': int(args[2]), 'Type': args[3],
                'ResourcePath': args[4],'FailureThreshold': int(args[5])
            }}
            response = collectHealthCheckArgs(*args)

        print(response['HealthCheck']['Id'])

#create basic health check for Route53 - 
#health checks are required for configuring failover routing policies in Route53
#Elliott Arnold 7-22-21

#example usage =>  python3 app.py DTX si3mshady.com 80 HTTP  / 4
#example usage =>  python3 app.py DTX2 54.19.13.3  80 HTTP  / 4






