def router(state):

    request = state["request"].lower()
    print("REQUEST:", request)

    # if "summary" in request:
    #     print("Routing to summary")
    #     return "summary"

    if any(word in request for word in ["summary", "summarize"]):
        print("Routing to summary")
        return "summary"
    
    print("Routing to qa")
    return "qa"