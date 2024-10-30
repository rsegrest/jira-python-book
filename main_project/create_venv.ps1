# Define the default path for the virtual environment
$DEFAULT_PATH = "atlassian_venv"

# Check if an argument was provided
if ([string]::IsNullOrEmpty($args[0])) {
    $VENV_PATH = $DEFAULT_PATH
} else {
    $VENV_PATH = $args[0]
}

Write-Output "Creating virtual environment at $VENV_PATH"

# Create the virtual environment
python -m venv $VENV_PATH

# Activate the virtual environment
# Note: In PowerShell, activation is different than in BASH. Here's how you can do it inline:
& "$VENV_PATH/Scripts/Activate.ps1"

# Install requirements
python -m pip install -r requirements.txt
