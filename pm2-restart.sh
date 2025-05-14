#!/bin/bash

# Load your environment (especially important if using NVM)
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"

# Ensure correct Node version is loaded
#nvm use 18  # hope this is automatic

# Restart your PM2 process
pm2 restart alledaags

