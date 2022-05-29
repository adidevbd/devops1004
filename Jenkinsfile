properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("clone"){
        git "https://github.com/adidevbd/devops1004.git"
    }
    stage("show files"){
        bat "dir"
    }
}
