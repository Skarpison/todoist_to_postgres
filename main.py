from todoist_api_python.api import TodoistAPI
import psycopg2
from dotenv import load_dotenv
import os

# Loads the .env file
load_dotenv()

TODOIST_API_TOKEN = os.getenv("TODOIST_API_TOKEN")

DB_SETTINGS = {
	"dbname": os.getenv("DATABASE_NAME"),
	"user": os.getenv("DATABASE_USER"),
	"password": os.getenv("DATABASE_PASSWORD"),
	"host": os.getenv("DATABASE_HOST"),
	"port": os.getenv("DATABASE_PORT")
}

def fetch_tasks():
		api = TodoistAPI(TODOIST_API_TOKEN)
		try:
			tasks = api.get_tasks() # Fetch all active tasks
			return tasks
		except Exception as error:
			print(f"Error fetching tasks: {error}")
			return []

def connecat_to_db():
	try:
		conn = psycopg2.connect(**DB_SETTINGS)
		return conn
	except Exception as e:
		print(f"Database connection error: {e}")
		return None

def insert_tasks(conn, tasks):
	with conn.cursor() as cur:
		for task in tasks:
			try:
				cur.execute("""                    
					INSERT INTO todoist_tasks (id)
                    VALUES (%s)
                    ON CONFLICT (id) DO NOTHING;
				""", (task.id,))
			except Exception as e:
				print(f"Error inserting task: {e}")
	conn.commit()

if __name__ == "__main__":
	# Fetch tasks from Todoist
	tasks = fetch_tasks()

	if tasks:
		# Connect to the database
		conn = connecat_to_db()
		if conn:
			# Insert tasks into database
			insert_tasks(conn, tasks)
			conn.close()
			print("Tasks inserted successfully.")
		else:
			print("Failed to connect to the database.")
	else:
		print("No tasks to insert.")