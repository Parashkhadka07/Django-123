dictt={
    "a":2,
    "b":22,
    "d":5,
    "g":56,
    "r":24,
    "h":7,
    

}
sorted_dict=dict(sorted(dictt.items(),key=lambda data:data[1],reverse=True))
print(sorted_dict)