def router(state):

    request = state["request"].lower()
    print("REQUEST:", request)

    if "summary" in request:
        print("Routing to summary")
        return "summary"
    
    print("Routing to qa")
    return "qa"