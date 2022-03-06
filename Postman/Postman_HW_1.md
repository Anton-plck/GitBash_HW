***
### ***Создать запросы в Postman.***

#### *Protocol:* **http**
#### *IP:* **162.55.220.72**
#### *Port:* **5005**

###### ***EP_1***
###### *Method:* **GET**
###### *EndPoint:* **/get_method**
###### *request url params:* 
 ###### - *name:* **str**
 ###### - *age:* **int**

###### *response:* 
###### [
   ###### “Str”,
   ###### “Str”
###### ]

***

###### ***EP_2***
###### *Method:* **POST**
###### *EndPoint:* **/user_info_3**
###### *request form data:* 
 ###### - *name:* **str**
 ###### - *age:* **int**
 ###### - *salary:* **int**

###### *response:* 
###### {'name': name,
   ###### 'age': age,
   ######       'salary': salary,
   ######       'family': {'children': [['Alex', 24], ['Kate', 12]],
   ######                  'u_salary_1_5_year': salary * 4}}
   
   ***
   
   
