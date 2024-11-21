# webserver

## Build application

docker build -t my_test_webserver .
docker run -d -p 8080:8080 my_test_webserver


## Example Usage

### Store Content

```bash
curl -X POST -d "Hello, World" http://localhost:8080/content/greeting
```

### Fetch Content

```bash
curl -X GET http://localhost:8080/content/greeting
Hello, World
```

### Fetch Headers

```bash
curl -I http://localhost:8080/content/greeting
```

### Compare Content Using ETags

Use the ETag value returned in headers for comparisons.
This structure ensures OCI compliance and uses Python to build a robust web application with ETag support.
