#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading the system..."
apt update && apt upgrade -y

# Install dependencies for the setup (git, proot-distro, python3, pip)
echo "Installing required dependencies..."
pkg install -y proot-distro git python python3 python3-pip

# Clone the SafeTEXT repository from GitHub
echo "Cloning SafeTEXT repository..."
git clone https://github.com/geniecreatordesign/SafeTEXT.git /data/data/com.termux/files/home/SafeTEXT

# Navigate to the SafeTEXT directory
cd /data/data/com.termux/files/home/SafeTEXT

# Install Python dependencies in a virtual environment
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Create a shortcut script to run SafeTEXT automatically
echo "Creating shortcut to run SafeTEXT..."
echo -e '#!/bin/bash\nsource /data/data/com.termux/files/home/SafeTEXT/venv/bin/activate\npython /data/data/com.termux/files/home/SafeTEXT/SafeTEXT.py' > /data/data/com.termux/files/usr/bin/safetext
chmod +x /data/data/com.termux/files/usr/bin/safetext

# Confirming installation success
echo "SafeTEXT installation complete!"
echo "You can now run SafeTEXT by simply typing 'safetext' from Termux."
