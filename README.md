# ClusterCommands

These are some commands I've written to make running stuff on the cluster (manually) a little easier. Here are the commands as of 8/20/2015:

  - runjar - adds some stuff to the classpath, sets some options, and runs your jar
  - rechup - same as runjar, but uses nohup and sends output to file


### Installation
Installation is a little bit weird. 
 - Navigate to your home folder
 - " git clone " this repository into a distinct folder name you won't delete accidentally, I chose " _CLUSTER_COMMANDS "
 - Navigate into that folder, and run " sh update.sh ". This will just " git stash; git pull; chmod +x <commands> ".
 - edit your .bashrc file, add a line that looks like this: 
```sh
export PATH=$PATH:/home/WHQ_NT_DOMAIN/mc023219/_CLUSTER_COMMANDS
```
 - Now, either log out and back in, or run " source .bashrc " to update your PATH and gain access to the commands. If you want, you can run them without parameters. They will fail, but will also print usage instructions.

Whenever you want to update the repo contents (if you see a new command, for example) just run "sh update.sh" and it will fetch all of the new stuff for you and make sure the commands still have execute permissions.
