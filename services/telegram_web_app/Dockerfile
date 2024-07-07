# Use the official Nginx image from Docker Hub
FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the static HTML file to the Nginx server
COPY src /usr/share/nginx/html