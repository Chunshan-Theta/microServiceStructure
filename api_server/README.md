###### NLU Service verification API

###### Deploy Environment

#Docker Deploy Steps

* start redis_server

```
cd redis_server
sh run.sh
```

* start worker

```
cd util
python3 simpleServer.py
```

* start api

```
sh docker_run.sh
```



# API


##### &raquo; handler/api/query/testHandler.py

` basic api `


Test request :
```
http://127.0.0.1:8088/api/Test
```


output:
```
{
    "re": "hello"
}
```

##### &raquo; handler/api/query/queryHandler.py

` oauth `

unittest: test_handler_api_queryHandler.py

Test request :

```
http://127.0.0.1:8088/api/query?q=你好 今天天氣很好
* header: token=eryuij345236sfdagete
```


output:
```
{
    "msgid": "q",
    "_text": "你好 今天天氣很好",
    "retCheck": true,
    "retStr": "你好 今天天氣很好",
    "token": "541dd339-8b57-41e9-b12b-7341a712fefd",
    "text_len": 9,
    "worker queue": "localhost:6379:nlumdl1-eryuij345236sfdagete-wk1",
    "in-time": "2019-08-14 11:35:10.777301",
    "out-time": "2019-08-14 11:35:10.793164",
    "exe-time": "0:00:00.015868"
}
```

##### &raquo; handler/api/query/statusHandler.py

` review status of server `

unittest: test_handler_api_statusHandler.py

Test request :

```
http://127.0.0.1:8088/api/status
```


output:
```
{
    "PreviousRequest_str": "queryHandler:\t2019-08-20 14:16:30.187795",
    "average_time": 0.018222
}
```


##### &raquo; handler/api/query/configHandler.py.py

` update config `

unittest: ` test_handler_api_configHandler.py `

` GET ` Test request :

```
http://127.0.0.1:8088/api/config

```


output:
```
{
    "users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "eryuij345236sfdagete": "token_id: eryuij345236sfdagete, model_ver: silkRuleBasedV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n"
    }
}
```

` POST ` Test request :

```
http://127.0.0.1:8088/api/config
```

body:
```
{
    "config":"{ \"token_id\": \"New_service\", \"model_ver\": \"silkBERTJoinV1\", \"servers\":[ {\"server_name\":\"nlumdl1\", \"ip\": \"xxx.xxx.xxx.xxx\", \"workers\": [ { \"worker_name\":\"nlumdl1-eryuij345236sfdagete-wk1\", \"MQip\":\"127.0.0.1\", \"MQport\": 6379 } ]} ] }"

}
```


output:
```
{
    "Old users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "eryuij345236sfdagete": "token_id: eryuij345236sfdagete, model_ver: silkRuleBasedV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n"
    },
    "New users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "eryuij345236sfdagete": "token_id: eryuij345236sfdagete, model_ver: silkRuleBasedV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "New_service": "token_id: New_service, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n"
    }
}
```

` DELETE ` Test request :

```
http://127.0.0.1:8088/api/config
```

body:
```
{
    "config_name":"eryuij345236sfdagete"

}
```


output:
```
{
    "Old users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "eryuij345236sfdagete": "token_id: eryuij345236sfdagete, model_ver: silkRuleBasedV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
    },
    "New users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
    }
}
```


` PUT ` Test request :

```
http://127.0.0.1:8088/api/config
```

body:
```
{
    "config":"{ \"token_id\": \"New_service\", \"model_ver\": \"put_test\", \"servers\":[ {\"server_name\":\"nlumdl1\", \"ip\": \"xxx.xxx.xxx.xxx\", \"workers\": [ { \"worker_name\":\"nlumdl1-eryuij345236sfdagete-wk1\", \"MQip\":\"127.0.0.1\", \"MQport\": 6379 } ]} ] }"

}
```


output:
```
{
    "Old users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "eryuij345236sfdagete": "token_id: eryuij345236sfdagete, model_ver: silkRuleBasedV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "New_service": "token_id: New_service, model_ver: update_test\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n"
    },
    "New users config": {
        "sdf235423tdthaer": "token_id: sdf235423tdthaer, model_ver: silkBERTJoinV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "eryuij345236sfdagete": "token_id: eryuij345236sfdagete, model_ver: silkRuleBasedV1\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n",
        "New_service": "token_id: New_service, model_ver: put_test\n\tserver_name: nlumdl1,\tserver_ip: xxx.xxx.xxx.xxx\n\t\tworker_name: nlumdl1-eryuij345236sfdagete-wk1,\tMQport: 6379,\tMQip: 127.0.0.1\n"
    }
}
```

# tools

##### &raquo;  util/logger.py

unittest: test_log_logger_get_logger.py

using:
```
self.logger = log_Object.get_logger()
self.logger.debug("some text.")
```



##### &raquo; util/config.py

unittest: test_util_config.py

using:
```
obj = {
            "token_id": "eryuij345236sfdagete",
            "model_ver": "silkRuleBasedV1",
            "servers":[
                    {"server_name":"nlumdl1",
                    "ip": "xxx.xxx.xxx.xxx",
                    "workers": [
                        {
                          "worker_name":"nlumdl1-eryuij345236sfdagete-wk1",
                          "MQip":"localhost",
                          "MQport": 6379
                        },
                        {
                          "worker_name":"nlumdl1-eryuij345236sfdagete-wk1",
                          "MQip":"localhost",
                          "MQport": 6379
                        }]
                    }]
            }
user_service = UserConfig(self.obj)
```


# config

> user config

##### &raquo; app_url.py

` valid token `

* configs is from all files in local folder named config.
* described about valid service of users.
* source format:

```
{
  "token_id": "eryuij345236sfdagete",
  "model_ver": "silkRuleBasedV1",
  "servers":[
    {"server_name":"nlumdl1",
     "ip": "xxx.xxx.xxx.xxx",
      "workers": [
                    {
                      "worker_name":"nlumdl1-eryuij345236sfdagete-wk1",
                      "MQip":"localhost",
                      "MQport": 6379
                    },
                    {
                      "worker_name":"nlumdl1-eryuij345236sfdagete-wk1",
                      "MQip":"localhost",
                      "MQport": 6379
                    }
                ]}
          ]
}
```
* load structure:

```
# variable initial (valid users.)

dir_path = "{}/config".format(os.path.dirname(os.path.realpath(__file__)))
config_files = [f for f in os.listdir(dir_path)]
users_config = {}
for f in config_files:
    with open("{}/{}".format(dir_path, f)) as file:
        temp_content = "".join(file.readlines()).strip("\n")
        temp_obj = json.loads(temp_content)
        users_config[temp_obj["token_id"]] = UserConfig(temp_obj)
configs = {'users_config': users_config}
```

> update 20190814
> user config

##### &raquo; server.py
` port ` ` run mode `
* configs is from file named server.config.
* described about basic setting of server, like port.
* source format:

```
[server.address]
Port = 8088
[server.log]
running_mode = DEV
server_log_dir = ./log/
```

* load structure:

```
import configparser

# get config
config = configparser.ConfigParser()
config.read('server.config')
server_port = config["server.address"]["Port"]

```