try:
    import langchain.agents.middleware
    print("Exists")
except ImportError:
    print("Does not exist")
