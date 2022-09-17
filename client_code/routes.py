import random
import anvil.http

def get_temp_history():
    
    my_history = []
    for i in range(1,10):
      my_history.extend([{'time':f'2022-09-{i}T{j}:00:00', 'temperature': random.uniform(20,27)} for j in range(1, 24)])
    
    return my_history

def get_limite():
  return { "Limite": 25 }

def get_users():
  return [
    { 
      "id": '1',
      "nome": "Exemplo 1",
      "email": "Exemplo1@gmail.com",
      "acesso": "Admin"
    },
    { 
      "id": '2',
      "nome": "Exemplo 2",
      "email": "Exemplo2@gmail.com",
      "acesso": "User"
    },
    { 
      "id": '3',
      "nome": "Exemplo 3",
      "email": "Exemplo3@gmail.com",
      "acesso": "User"
    }
  ] 
    
def set_limite(my_limit):
  pass

  
  