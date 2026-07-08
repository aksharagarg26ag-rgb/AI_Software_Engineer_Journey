class App:

    def __init__(self):

        self.routes = {}

    def get(self, path):

        print(path)

app = App()

app.get("/home")

#
class App:

    def __init__(self):

        self.routes = {}

    def get(self, path):

        def decorator(func):

            print("Registering", path)

            return func

        return decorator
app = App()

@app.get("/home")
def home():

    print("Home Page")

#
class App:

    def __init__(self):

        self.routes = {}

    def get(self, path):

        def decorator(func):

            self.routes[path] = func

            return func

        return decorator


app = App()


@app.get("/home")
def home():

    print("Home Page")


@app.get("/about")
def about():

    print("About Page")


@app.get("/predict")
def predict():

    print("Prediction")


print(app.routes)

print("\nCalling Route...\n")

app.routes["/predict"]()