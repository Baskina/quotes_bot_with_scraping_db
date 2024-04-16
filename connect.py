from mongoengine import connect

# Create a new client and connect to the server
client = connect(
    db='authors',
    username='baskinadevelopment',
    password='5fQLW8GKlk87ARN6',
    host='mongodb+srv://baskinadevelopment:5fQLW8GKlk87ARN6@cluster0.upbkmny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)