FROM python:3.11-slim

WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# copy requirements
COPY requirements.txt .

# install python packages
RUN pip install --no-cache-dir -r requirements.txt

# copy application files
COPY . .

# create directories
RUN mkdir -p uploads results

# expose port
EXPOSE 5000

# run the app
CMD ["python", "app.py"]
