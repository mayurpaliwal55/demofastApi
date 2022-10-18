from fastapi.responses import JSONResponse

def is_valid_input(x,status_code=200):
    if x.islower():
        print(x)
        return { "message": "success"}
    for i in range(len(x)):
        if x[i].isupper():
            return { "message": "fail"}
    try:
        if isinstance(float(x),float):
            try:
                if isinstance(int(x),int):
                    item =  f"data type 'int' not allowed"
                    return JSONResponse(status_code=429,content=item)
            except:
                item =  f"data type 'float' not allowed"
                return JSONResponse(status_code=429,content=item)
    except:
        if x=="True" or x=="False":
            item =  f"Boolean Data Type Not Allowed"
            return JSONResponse(status_code=503,content=item)
        