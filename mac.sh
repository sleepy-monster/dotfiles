#!/bin/bash

####################################
# Usage:
# ./mac.sh
####################################

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> $HOME/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"



# source "${HOME}/.zsh_aliases"


# Install Packages
brew bundle --file=config_mac/Brewfile
