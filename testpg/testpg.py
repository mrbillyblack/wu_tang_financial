#!/usr/bin/python3

from flask import Flask, render_template
import json
import mysql.connector
import requests

app = Flask(__name__)

def verify_address(address: str, city: str, state: str, zip_code: str) -> bool:
    fpath = './auth.json'
    with open(fpath, 'r') as json_file:
        smarty_auth = json.load(json_file)

    
    auth_token = str(smarty_auth["AUTH_TOKEN"])
    auth_id = str(smarty_auth["AUTH_ID"])
    
    license = 'us-core-cloud'

    delimiter = '+'
    
    address = address.split()
    address = delimiter.join(address)

    city = city.split()
    city = delimiter.join(city)

    state = state

    zip_code = zip_code

    endpoint = 'https://us-street.api.smarty.com/street-address?auth-id={}& \
    auth-token={}&license={}&street={}&city={}&state={}&candidates=1'\
    .format(auth_id, auth_token, license, address, city, state)

    response = requests.get(endpoint)
    if not response.json()["errors"]:
        if response.json() is None:
            return False
    return True


def fetch_data():
    host = '172.19.0.9'
    user = 'root'
    password = 'root' 
    database = 'member'

    connection = mysql.connector.connect(
    	host=host,
    	user=user,
    	password=password,
    	database=database
    )
  
    cursor = connection.cursor()

    query = 'SELECT * FROM members'

    cursor.execute(query)
    
    rows = cursor.fetchall()

    data = {
        "Index" : [ row[0] for row in rows ],
        "FirstName": [ row[1] for row in rows ],
        "LastName": [ row[2] for row in rows ],
        "Address": [ row[3] for row in rows ],
        "City": [ row[4] for row in rows ],
        "State": [ row[5] for row in rows ],
        "ZipCode": [ row[6] for row in rows ],
        "Country": [ row[7] for row in rows ],
        "Valid": [ row[8] for row in rows ]     
    }
    
    rows = []

    for i in range(len(data["Index"])):
        valid = verify_address(data["Address"][i], data["City"][i], data["State"][i], str(data["ZipCode"]))
        
        if valid != False:
            valid = '❌'
        else: 
            valid = '✅'

        row = [data["FirstName"][i], data["LastName"][i], data["Address"][i], data["City"][i], data["State"][i], \
        data["ZipCode"][i], data["Country"][i], valid]

        
        rows.append(row)

    return rows

@app.route('/')
def index():
    rows = fetch_data()
    columns = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "Country", "Valid?"]

    # data = [
    #     [i for i in data["FirstName"]],
    #     [i for i in data["LastName"]],
    #     [i for i in data["Address"]],
    #     [i for i in data["City"]],
    #     [i for i in data["State"]],
    #     [i for i in data["ZipCode"]],
    #     [i for i in data["Country"]],
    #     [i for i in data["Valid"]]
    # ]

    return render_template('index.html', columns=columns, rows=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

