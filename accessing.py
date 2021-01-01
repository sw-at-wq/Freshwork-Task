import code as x 

x.create("Andrea",25)    #to create a key with key_name,value given and with no time-to-live property


x.create("src",70,3600)  #to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("Andrea")         #it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("src")            #it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("Andrea",50)    #it returns an ERROR since the key_name already exists in the database
                         #use delete operation and recreate it
 
x.delete("Andrea")       #it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
