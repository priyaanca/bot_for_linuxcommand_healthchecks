import re
from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

# Welcome
@app.route('/chat/greetings', methods=['GET'])
def chat_greetings():
    # retrieve the user input from the query parameter
    user_input = request.args.get('input').lower()

    # check for a greeting or expression of gratitude
    if user_input in ['hello', 'hi', 'hey']:
        bot_response = "Hello there, how can I assist you today?"
    elif user_input in ['run command']:
        bot_response = "These are the commands I can help you with"
    elif user_input in ['thank you', 'thanks', 'appreciate it']:
        bot_response = "You're welcome!"
    else:
        bot_response = "I'm sorry, I don't understand. Could you please rephrase your message?"

    return jsonify({'bot_response': bot_response})

@app.route('/chat/linux_commands', methods=['GET'])
def chat_linux_commands():
    # retrieve the user input from the query parameter
    user_input = request.args.get('input')

    if user_input in ['top', 'memory used', 'disc usage', 'network']:
        # if user input is a health check command, return an error message
        bot_response = "I'm sorry, I cannot run that command from here."
        
    match_list = re.search(r'\blist\b', user_input, flags=re.IGNORECASE)
    match_date = re.search(r'\bdate\b', user_input, flags=re.IGNORECASE)
    match_time = re.search(r'\buptime\b', user_input, flags=re.IGNORECASE)
    match_user = re.search(r'\bwho\b', user_input, flags=re.IGNORECASE) 
    match_create_directory = re.search(r'\bcreate directory\b', user_input, flags=re.IGNORECASE)
    match_create_file = re.search(r'\bcreate file\b', user_input, flags=re.IGNORECASE)
    match_copy_file = re.search(r'\bcopy file\b', user_input, flags=re.IGNORECASE)
    match_move_file = re.search(r'\bmove file\b', user_input, flags=re.IGNORECASE)
    match_remove_file = re.search(r'\bremove file\b', user_input, flags=re.IGNORECASE)
    match_remove_directory = re.search(r'\bremove directory\b', user_input, flags=re.IGNORECASE)

    if match_list:
        # if the keyword "list" is present, run the appropriate Linux command to list the files in the current directory
        command = ['ls', '-al']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_date:
        # if the keyword "list" is present, run the appropriate Linux command to list the files in the current directory
        command = ['date']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_time:
        # if the keyword "list" is present, run the appropriate Linux command to list the files in the current directory
        command = ['uptime']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_user:
        # if the keyword "list" is present, run the appropriate Linux command to list the files in the current directory
        command = ['who']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_create_directory:
       
        command = ['mkdir', directory_name]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_create_file:
        # if the keyword "create file" is present, extract the file name and create the file using the appropriate Linux command
        file_name = re.search(r'\bcreate\b file (.+)', user_input, flags=re.IGNORECASE).group(1)
        command = ['touch', file_name]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = f"File '{file_name}' created successfully."
    elif match_copy_file:
        # if the keyword "copy file" is present, extract the source and destination file paths and copy the file using the appropriate Linux command
        source_path, destination_path = re.search(r'\bcopy file (.+) to (.+)', user_input, flags=re.IGNORECASE).groups()
        command = ['cp', source_path, destination_path]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = f"File '{source_path}' copied to '{destination_path}' successfully."
    elif match_move_file:
        # if the keyword "move file" is present, extract the source and destination file paths and move the file using the appropriate Linux command
        source_path, destination_path = re.search(r'\bmove file (.+) to (.+)', user_input, flags=re.IGNORECASE).groups()
        command = ['mv', source_path, destination_path]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = f"File '{source_path}' moved to '{destination_path}' successfully."
    elif match_remove_file:
        # if the keyword "remove file" is present, extract the file path and remove the file using the appropriate Linux command
        file_path = re.search(r'\bremove file (.+)', user_input, flags=re.IGNORECASE).group(1)
        command = ['rm', file_path]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = f"File '{file_path}' removed successfully."
    elif match_remove_directory:
        # if the keyword "remove directory" is present, extract the directory name and remove the directory using the appropriate Linux command
        directory_name = re.search(r'\bremove directory (.+)', user_input, flags=re.IGNORECASE).group(1)
        command = ['rm', '-rf', directory_name]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = f"Directory '{directory_name}' removed successfully."
    
    elif user_input:
        # if user input is not a health check command, run the Linux command and return the output as a bot response
        process = subprocess.Popen([user_input], stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        bot_response = output.decode('utf-8')
    

    else:
        # if user input is not a valid command, return an error message
        bot_response = "I'm sorry, I cannot run that command from here."
        return jsonify({'bot_response': bot_response})

    # return the output as a bot response
    return jsonify({'bot_response': bot_response})


# Health checks endpoint
@app.route('/chat/health_checks', methods=['GET'])
def chat_health_checks():
    # retrieve the user input from the query parameter
    user_input = request.args.get('input')
    
    # use regex to extract keywords from the user input
    match_memory = re.search(r'\bmemory\b', user_input, flags=re.IGNORECASE)
    match_network = re.search(r'\bnetwork\b', user_input, flags=re.IGNORECASE)
    match_disk = re.search(r'\bdisk\b', user_input, flags=re.IGNORECASE)
    match_cpu = re.search(r'\bcpu\b', user_input, flags=re.IGNORECASE)
    
    if match_memory:
        # if the keyword "memory" is present, run the appropriate Linux command to retrieve the memory usage
        process = subprocess.Popen(['free'], stdout=subprocess.PIPE)
        output, error = process.communicate()
        bot_response = output.decode('utf-8')
    elif match_cpu:
        # if the keyword "top" is present, run the appropriate Linux command to retrieve network interface information
        process = subprocess.Popen(['top','-n','1'], stdout=subprocess.PIPE)
        output, error = process.communicate()
        bot_response = output.decode('utf-8')
    elif match_network:
        # if the keyword "network" is present, run the appropriate Linux command to retrieve network interface information
        process = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE)
        output, error = process.communicate()
        bot_response = output.decode('utf-8')
    elif match_disk:
        # if the keyword "disk" is present, run the appropriate Linux command to retrieve disk usage information
        process = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
        output, error = process.communicate()
        bot_response = output.decode('utf-8')
    else:
        # if none of the keywords are present, return an error message
        bot_response = "I'm sorry, I don't understand that command."

    return jsonify({'bot_response': bot_response})



if __name__ == '__main__':
    app.run(debug=True)
