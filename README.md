# secret-santa-emailer
Secret Santa Emailer

This is still a work in progress. Notes about the current version:
  - This uses a dumb but effective randomized brute force algorithm
  - This version has a few requirements which need to be simplified
  - Files should be renamed to be more user friendly

## Setup
brew tap caskroom/fonts
brew cask install font-arial
pip install -r requirements.txt
cp -r example_config ~/.secret_santa/
mkdir images
Download an image into ./images/ and name it secret_santa.png (I google image searching 'mental health at christmas' seems to yield a really good image)

## Configuration
Edit ~/.secret_santa/names.conf to match the names and contact information of your participants
Edit ~/.secret_santa/credentials.yaml to match your email credentials (currently only works with gmail)

## Usage
./selector.py --names ~/.secret_santa/names.yaml 
