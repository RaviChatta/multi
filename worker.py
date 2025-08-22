import os
import subprocess
import json
import time

with open("config.json", "r") as jsonfile:
    bots = json.load(jsonfile)

bot_processes = []

for bot_name, bot_config in bots.items():
    
    time.sleep(5)  # Optional delay between bot startups

    # Set environment variables for this bot
    for env_name, env_value in bot_config.get('env', {}).items():
        os.environ[env_name] = env_value
    
    bot_dir = f"/app/{bot_name}"

    # Install requirements if requirements.txt exists
    requirements_file = os.path.join(bot_dir, 'requirements.txt')
    if os.path.exists(requirements_file):
        subprocess.run(['pip', 'install', '--no-cache-dir', '-r', requirements_file], check=True)

    # Determine how to run the bot
    if 'run' in bot_config:
        bot_file = os.path.join(bot_dir, bot_config['run'])
        print(f'Starting {bot_name} bot with {bot_file}')
        p = subprocess.Popen(['python3', bot_file], cwd=bot_dir, env=os.environ)
        bot_processes.append(p)
    elif 'dockerfile' in bot_config:
        print(f'Building and starting {bot_name} bot from Dockerfile')
        # Build Docker image
        subprocess.run(['docker', 'build', '-t', bot_name, bot_dir], check=True)
        # Run Docker container with environment variable for port
        p = subprocess.Popen(['docker', 'run', '-e', f"PORT={bot_config['env']['PORT']}", bot_name])
        bot_processes.append(p)
    else:
        print(f"No valid run method found for {bot_name}, skipping.")

# Wait for all bot processes to finish
for p in bot_processes:
    p.wait()
