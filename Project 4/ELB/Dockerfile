# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set environment variables for application
ENV APP_HOME=/app \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR $APP_HOME

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/Het4304/30_Days_DEVOPS.git $APP_HOME

# Set working directory to the specific project folder
WORKDIR $APP_HOME/Project_4

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Define command to run the application
CMD ["python3", "app2.py"]