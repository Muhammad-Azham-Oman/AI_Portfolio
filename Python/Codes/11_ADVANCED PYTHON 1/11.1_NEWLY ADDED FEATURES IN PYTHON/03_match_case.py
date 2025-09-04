def system(status):
    match status:
        case(200):
            return("ok")
        case(404):
            return("Server not found")
        case(500):
            return("Internal Server Error.")
        case _:
            return("Not Found")
        
print(system(200))