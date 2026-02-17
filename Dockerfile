# base image

FROM  python:3.8-alpine

# set working directory

WORKDIR /app

# COPY DEPENDENCIES FILE FIRST (CACHING )

COPY requirements.txt .

# install dependencies

RUN pip install --no-cache-dir -r requirements.txt

# upper side line  meaning ->1️⃣ Creates temporary container
# 2️⃣ Executes pip install
# 3️⃣ Saves installed packages in image layer
# 4️⃣ Removes temporary container
# 5️⃣ Commits layer to image

# copy application files 
COPY app.py .

# Expose port 
EXPOSE 5000

# start application 
ENTRYPOINT ["python"]
CMD ["app.py"]


