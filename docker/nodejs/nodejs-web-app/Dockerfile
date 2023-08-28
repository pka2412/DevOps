#get the node base image from docker-hub or locally
FROM node:alpine3.17
#set the working directory inside the container
WORKDIR app
#copy the contents of host current directory to the container current directory
COPY . .
#initialize node app and install express package
#RUN npm init -y && npm install express
#expose the 3000 port to access the web-app
EXPOSE 3000
#start the web-app
CMD ["node","index.js"]
