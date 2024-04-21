FROM ubuntu:22.04

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=webuser1
ENV POSTGRES_PASSWORD=student
ENV POSTGRES_DB=csdashboard
ENV POSTGRES_HOST=192.168.56.20

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install net-tools python3 postgresql postgresql-client pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a user
RUN useradd -ms /bin/bash webuser1

# Set working directory
WORKDIR /home/student/Docker

# Copy the current directory contents into the container at /app
COPY . /home/student/Docker

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Remove default PostgreSQL configuration
RUN rm -f /etc/postgresql/14/main/postgresql.conf

EXPOSE 5432

# Set entry point to start PostgreSQL
ENTRYPOINT ["usr/lib/postgresql/14/bin/postgres", "-D", "/var/lib/postgresql/14/main", "-c", "config_file=/etc/postgresql/14/main/postgresql.conf"]

# Command to run the Python HTTP server
CMD ["python3", "app.py"]
