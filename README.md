# Flask JSON Server
This application allows users to create a JSON server via a designated endpoint. This makes it easier to create mock APIs and speed up the development process.

## Installation
Firstly, Docker must be installed for this application to work.

1. Clone this repository: `git clone https://github.com/inalbilal/flask-json-server.git`
2. Go to the cloned directory: `cd flask-json-server`
3. Start the application using Docker Compose: `docker-compose up -d`
4. Go to `http://localhost:8000/` in your browser.

## Usage
The application allows you to create mock servers on the `/create-server` page. On this page, you can specify properties such as an endpoint, name and JSON Data for the mock server.

You can access the mock servers you created by making a GET request to `/{slug}/{endpoint}`.

## Database Structure

The database used for this project has the following structure:

```
`id`, `endpoint`, `name`, `slug`, `content`, `created_at`, `updated_at`, `is_active` FROM `json_server`
```
