
import pytest

def get_data():
    # Retrieve values from CSV
    
#     myDat=[]
#     myDat.append("A1")
#     myDat.append("A2")
#     myDat.append("A3")
    myData =[]
    Dict = {}
    Dict['FirstName'] = 'Abhishek'
    Dict['LastName'] = 'Puri'
    myData.append(Dict)
    
    Dict = {}
    Dict['FirstName'] = 'Riya'
    Dict['LastName'] = 'Bedi'
    myData.append(Dict)
    
    Dict = {}
    Dict['FirstName'] = 'Priyanka'
    Dict['LastName'] = 'Das'
    myData.append(Dict)
    
    Dict = {}
    Dict['FirstName'] = 'Ashish'
    Dict['LastName'] = 'Thakur'
    myData.append(Dict)
    
    Dict = {}
    Dict['FirstName'] = 'Yogesh'
    Dict['LastName'] = 'Chawla'
    myData.append(Dict)
    
    return myData
    #return ['value1', 'value2', 'value3']

@pytest.mark.parametrize("value", get_data())
def test_sample(value):
    pass
