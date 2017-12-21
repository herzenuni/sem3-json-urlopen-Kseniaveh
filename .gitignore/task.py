from urllib.request import urlopen
import json
import pprint

def InputVkIds():
  print('Введите список id, через запятую:')
  id = input()
  return id

def SendRequestVk(ids):
  request = "https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site,first_name,last_name,status,online,last_seen&v=5.69".format(id = ids)
  print('Сформированный запрос:', request)
  obj={}
  try:
	  request_obj = urlopen(request)#отправка на сервер
	  obj = json.loads(request_obj.read())#конвертируем ответ сервера в JSON
  except:
	  obj={"response":"error","message":"Ошибка соединения с сервером!, Проверьте соединение!"}#имитируем JSON при ошибке сервера, для того чтобы функция не возращала пустых значений
  return obj

def JsonConsoleWriter(json):
  if (json.get('response') != None and json.get('response')!="error"):#двойная проверка JSON 1: для случая когда сервер отработал запрос, но вернул JSON с ошибкой в котором нет поля response 2: для случая когда сервер вообще ничего не вернул, это вариант exept 
      print('Ответ сервера:')
      resp=json.get('response')#складываем в переменную значение поля response
      for field in resp:
          print(" First name: " + str(field['first_name']))
          print(" Last name: " + str(field['last_name']))
          print(" Online: " + str(field['online']))
          print(" Sex: " + str(field['sex']))
          print(" Last_seen: " + str(field['last_seen'])+ '\n') 
  else:
    if (json.get('response') != None):
  	  if (json.get('error') != None):
  	  	print('Сервер вернул ошибку:')
  	  	pprint.pprint(json['error'])
  	  else:
  	  	print('Неизвестная ошибка!');
    else:
  	  resp=json.get('response')
  	  print(resp);
        
JsonConsoleWriter(SendRequestVk(InputVkIds()))
