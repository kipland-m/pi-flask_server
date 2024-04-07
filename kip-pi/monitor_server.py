from flask import Flask, request

# Create instance of Flask App
app = Flask(__name__)

# define route to send hardware data to
@app.route('/receive_hardware_data', methods=['POST'])
def receive_hardware_data():
    data = request.json

    # Process the received data 
    for item in data:
        print(item)
        
    return 'Data received successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
