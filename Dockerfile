# Dockerfile

# Use the official Python 3.10 slim image, which matches your .python-version file
FROM python:3.10-slim

# Install Tectonic - this is the key step for your PDF generation
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://get.tectonic-typesetting.org/install-from-env.sh | sh

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8080

# The command to run your Streamlit application
CMD ["streamlit", "run", "frontend.py", "--server.port=8080", "--server.address=0.0.0.0"]