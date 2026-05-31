# DockerShare 🚀

DockerShare is a lightweight containerized file-sharing server built using Docker and Nginx. It enables users to host and access files through a web browser on devices connected to the same local network.

The project demonstrates practical DevOps concepts including containerization, web server deployment, port mapping, container lifecycle management, networking, and troubleshooting.

---

## Features

* Dockerized deployment using Docker
* Nginx-based file hosting server
* Browser-based file access
* Cross-device access over local network
* QR Code connectivity for quick mobile access
* Lightweight and easy to deploy
* Simple and responsive landing page
* Supports sharing documents, images, videos, archives, and other file types

---

## Tech Stack

* Docker
* Nginx
* HTML5
* CSS3
* Python (QR Code Generation)

---

## Project Structure

```text
DockerShare/
│
├── shared-files/
│   ├── index.html
│   ├── qr.png
│   └── files/
│
├── Dockerfile
├── default.conf
├── generate_qr.py
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/DockerShare.git
cd DockerShare
```

### Build Docker Image

```bash
docker build -t dockershare .
```

### Run Container

```bash
docker run -d -p 8080:80 --name dockershare-container dockershare
```

---

## Usage

Open the application in your browser:

```text
http://localhost:8080
```

To access from another device on the same Wi-Fi network:

```text
http://YOUR_LOCAL_IP:8080
```

Example:

```text
http://192.168.1.5:8080
```

---

## Docker Commands Used

### View Running Containers

```bash
docker ps
```

### View All Containers

```bash
docker ps -a
```

### Stop Container

```bash
docker stop dockershare-container
```

### Start Container

```bash
docker start dockershare-container
```

### Restart Container

```bash
docker restart dockershare-container
```

### View Logs

```bash
docker logs dockershare-container
```

### Remove Container

```bash
docker rm -f dockershare-container
```

### Remove Image

```bash
docker rmi dockershare
```

---

## QR Code Support

The project includes a Python script that automatically generates a QR code for the current local network address.

Generate QR Code:

```bash
python generate_qr.py
```

Users can scan the QR code using their phone camera to access DockerShare instantly.

---

## Learning Outcomes

Through this project, I gained practical experience with:

* Docker image creation
* Docker container deployment
* Nginx web server configuration
* Port mapping and networking
* Container lifecycle management
* Local file hosting
* DevOps troubleshooting workflows
* Self-hosted application deployment

---

## Screenshots

Add screenshots here after project completion:

* Docker Image Build
* Running Container (`docker ps`)
* DockerShare Homepage
* Shared Files Directory
* QR Code Access
* Mobile Device Access

---

## Future Enhancements

* File upload support
* Password-protected access
* Download statistics
* Multi-user support
* Drag-and-drop uploads
* Cloud deployment support

---

## Author

**Chinmay Upadhyaya**


---

## License

This project is created for educational and learning purpose.
