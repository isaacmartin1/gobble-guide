# Use a lightweight Python image
FROM python:3.13

# Set a working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the environment file (you can also use Docker's --env-file option instead)
COPY .env .

# Copy the rest of the application code
COPY . .

# Expose the port your Flask app runs on
EXPOSE 3000

# Set the command to run the app
CMD ["python", "main.py"]
