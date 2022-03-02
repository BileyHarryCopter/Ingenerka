# SSH_KEY #
### Short instruction of autorization by ssh-key ###

### 1. Generation ssh-key on local point: ###
_1.1._ Open terminal and writedown this code with e-mail of your github account:

    ssh-keygen -t ed25519 -C "your_email@example.com"

_1.2._ Writedown this command to create new ssh-key:

    > Generating public/private ed25519 key pair.

_1.3._ Enter name of the file in which your ssh-key will be located

    > Enter a file in which to save the key (/Users/you/.ssh/id_ed25519): [Press enter]

_1.4._ Use your personal token for generation a key:

    > Enter passphrase (empty for no passphrase): [Press enter]

### 2. Adding the key in ssh-agent
_2.1_ Launch terminal in ssh-agent:

    eval "$(ssh-agent -s)"
    > Agent pid 59566

_2.2_ Add private ssh-key to ssh-agent:

    $ ssh-add ~/.ssh/id_ed25519

### 3. Adding the key to site
_3.1._ Choose "SSH and GPG keys" in user setting on the GitHub. Click on New SSH key or Add SSH key. Copy key into the frame "Key" from file of SSH key on your computer

_3.2._ After this to push the button "Add SSH key"

Thanks to allertion:

![This is SHREK, okey] (shrek.jpeg)
