context={
    "1":{
        "project":"ironman",
        "role":"lead engineear"
    },
    "2":{
        "project":"hulk",
        "role":"physichist"
    }
}
def projects(id=None):
    print("the id of the sanskari project is ",id)

    project=context[id]
    print(project)
    contextt={
        "details":project
    }
    print(contextt)
    
projects("1")