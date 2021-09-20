from newrelic.agent import background_task

@background_task()
def hello():
    print("Hello from Python!")

if __name__ == '__main__':
    hello()
