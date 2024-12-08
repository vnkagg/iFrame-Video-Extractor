import os
import platform
import shutil
from setuptools import setup

# Function to register the native messaging host
def post_install():
    system = platform.system()
    json_file = 'com.az.iframe.bridge.json'

    # Define paths based on the operating system
    if system == 'Windows':
        # Path for the registry location
        target_dir = os.path.expandvars(
            r'%APPDATA%\Google\Chrome\User Data\NativeMessagingHosts'
        )
    elif system == 'Darwin':  # macOS
        target_dir = os.path.expanduser(
            '~/Library/Application Support/Google/Chrome/NativeMessagingHosts'
        )
    else:  # Linux
        target_dir = os.path.expanduser(
            '~/.config/google-chrome/NativeMessagingHosts'
        )

    # Create the directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Copy the JSON file to the target directory
    shutil.copy(json_file, target_dir)
    print(f"Native messaging host registered at {target_dir}")

    # (Optional) Place chrome.py in a system-wide accessible location
    script_target_dir = shutil.which('python')  # Same directory as the Python executable
    shutil.copy('chrome.py', script_target_dir)
    print(f"chrome.py placed at {script_target_dir}")


# Define the setup script
setup(
    name='chrome_iframe_bridge',
    version='1.0.0',
    description='Native messaging host for a Chrome extension',
    author='Your Name',
    packages=['chrome_iframe_bridge'],
    package_data={'chrome_iframe_bridge': ['com.az.iframe.bridge.json']},
    entry_points={
        'console_scripts': [
            'chrome-iframe-bridge=chrome_iframe_bridge.chrome:main'
        ],
    },
    install_requires=[],
    # Custom hook to execute the post-install script
    cmdclass={
        'install': lambda cmd: (cmd.run(), post_install())[1],
    },
)
