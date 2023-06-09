import re
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS,cross_origin
import subprocess

app = Flask(_name_, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('try.html')

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

    match_list = re.search(r'\blist\b', user_input, flags=re.IGNORECASE)
    match_date = re.search(r'\bdate\b', user_input, flags=re.IGNORECASE)
    match_time = re.search(r'\buptime\b', user_input, flags=re.IGNORECASE)
    match_user = re.search(r'\bwho\b', user_input, flags=re.IGNORECASE) 
    match_create_directory = re.search(r'\bcreate directory\b', user_input, flags=re.IGNORECASE)
    match_create_file = re.search(r'\bcreate\b file\b', user_input, flags=re.IGNORECASE)
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
        # if the keyword "date" is present, run the appropriate Linux command to get the current date
        command = ['date']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_time:
        # if the keyword "uptime" is present, run the appropriate Linux command to get the system uptime
        command = ['uptime']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_user:
        # if the keyword "who" is present, run the appropriate Linux command to get the currently logged-in users
        command = ['who']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_create_directory:
        # if the keyword "create directory" is present, extract the directory name and create the directory using the appropriate Linux command
        directory_name = re.search(r'\bcreate directory named (.+) in the current directory', user_input, flags=re.IGNORECASE).group(1)
        command = ['mkdir', directory_name]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = f"Directory '{directory_name}' created successfully."
    elif match_create_file:
        # if the keyword "create file" is present, extract the file name and create the file using the appropriate Linux command
        file_name = re.search(r'\bcreate file named (.+) in the current directory', user_input, flags=re.IGNORECASE).group(1)
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
        # if user input is not a recognized command, run the user input as a Linux command and return the output as a bot response
        process = subprocess.Popen([user_input], stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        bot_response = output.decode('utf-8')
    else:
        bot_response = "I'm sorry, I don't understand that command."

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
        command = ['free']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_network:
        # if the keyword "network" is present, run the appropriate Linux command to retrieve network interface information
        command = ['ifconfig']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_disk:
        # if the keyword "disk" is present, run the appropriate Linux command to retrieve disk usage information
        command = ['df', '-h']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_cpu:
        # if the keyword "cpu" is present, run the appropriate Linux command to retrieve CPU information
        command = ['top', '-n', '1']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    else:
        bot_response = "I'm sorry, I don't understand that command."

    return jsonify({'bot_response': bot_response})
@app.route('/chat/kube_health_checks', methods=['GET'])
def kube_health_checks():
    # retrieve the user input from the query parameter
    user_input = request.args.get('input')
    
    # use regex to extract keywords from the user input
    
    match_pods = re.search(r'\bpods\b', user_input, flags=re.IGNORECASE)
    match_nodes = re.search(r'\bnodes\b', user_input, flags=re.IGNORECASE)
    match_deployments = re.search(r'\bdeployments\b', user_input, flags=re.IGNORECASE)
    match_services = re.search(r'\bservices\b', user_input, flags=re.IGNORECASE)
    match_persistent_volumes = re.search(r'\bpersistent volumes\b', user_input, flags=re.IGNORECASE)
    match_stateful_sets = re.search(r'\bstateful sets\b', user_input, flags=re.IGNORECASE)
    match_liveness_probes = re.search(r'\bliveness probes\b', user_input, flags=re.IGNORECASE)
    match_readiness_probes = re.search(r'\breadiness probes\b', user_input, flags=re.IGNORECASE)   
    if match_pods:
        # if the keyword "pods" is present, run the appropriate Kubernetes command to retrieve pod information
        command = ['kubectl', 'get', 'pods', '-o', 'wide']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_nodes:
        # if the keyword "nodes" is present, run the appropriate Kubernetes command to retrieve node information
        command = ['kubectl', 'get', 'nodes', '-o', 'wide']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_services:
       # if the keyword "services" is present, run the appropriate Kubernetes command to retrieve service information
        command = ['kubectl', 'get', 'services', '-o', 'wide']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_persistent_volumes:
       # if the keyword "persistent volumes" is present, run the appropriate Kubernetes command to retrieve persistent volume information
        command = ['kubectl', 'get', 'persistentvolumes', '-o', 'wide']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_stateful_sets:
       # if the keyword "stateful sets" is present, run the appropriate Kubernetes command to retrieve stateful set information
        command = ['kubectl', 'get', 'statefulsets', '-o', 'wide']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
        
    elif match_deployments:
        # if the keyword "deployments" is present, run the appropriate Kubernetes command to retrieve deployment information
        command = ['kubectl', 'get', 'deployments', '-o', 'wide']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_liveness_probes:
        # if the keyword "liveness probes" is present, run the appropriate Kubernetes command to retrieve liveness probe information
        command = ['kubectl', 'describe', 'pods', '--all-namespaces']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    elif match_readiness_probes:
        # if the keyword "readiness probes" is present, run the appropriate Kubernetes command to retrieve readiness probe information
        command = ['kubectl', 'describe', 'pods', '--all-namespaces']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        bot_response = output.decode('utf-8')
    else:
        bot_response = "Sorry, I didn't understand your query."
    
    return jsonify({'bot_response': bot_response})


if _name_ == '_main_':
    app.run(host='192.168.1.173',debug=True)
