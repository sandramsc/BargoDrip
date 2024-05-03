# Use an official Python runtime as the base image 
FROM python:3

# Set the working directory in th econtainer
WORKDIR /app

# Copy the current directory contents into the conatiner at /app

COPY . /app

# Install app dependencies specified in requiremenets.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the commandto run the CLI tool
CMD ["python", "cli.py"]
