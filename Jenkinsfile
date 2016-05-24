/** Jenkinsfile for Fluidity 
 *  
 *  Place this file in a Fluidity branch so Jenkins knows to build that branch. This
 *  also requires a Dockerfile to be present.
 * 
 *  Original author: Tim Greaves <tim.greaves@imperial.ac.uk>
**/

/** WeUseAnyNode.com **/
node {
  
  stage "Building"
  
  /** Get the source as specified by Jenkins following the build initialisation; there
   *  may be a bug here where it gets the *latest* revision as opposed to the one which
   *  triggered the build (this from reading bug reports on the Jenkins forum)           **/
  checkout scm

  /** Build the docker image, using the Dockerfile in the repo and using HUDSON_COOKIE
   *  as a consistent and unique identifier for this build                               **/
  sh 'docker build -t $HUDSON_COOKIE .'
  
  stage "Testing"

  /** Run tests in the built container                                  **/
  sh '''
  docker run -a stdout -t $HUDSON_COOKIE bash -c 'make unittest'
  docker run -a stdout -t $HUDSON_COOKIE bash -c 'make testtest'
  docker run -a stdout -t $HUDSON_COOKIE bash -c 'make mediumtest'
  '''
  
}
