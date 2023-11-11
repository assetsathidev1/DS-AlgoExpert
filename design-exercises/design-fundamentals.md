# Systems Design Fundamentals Course

## Introduction
- Topics that will covered in the course: 
    1. Fundamental Concepts: Client-Server, Network protocols etc
    2. Key Characteristics of Distributed Systems: Availability, Reliability, Consistency, Throughput, Latency etc
    3. Actual Components: Load Balancers, Caches, Databases, Message Queues, Proxy, leader election etc
    4. Named/real tech products/services: Zookeeper, GCS, MR etc.

## Client-Server Model
- Client requests a service/data from the server. So it requests a resource; and the server responses with the resource.
- Backbone of modern internet apps
- Browser(Client) does a DNS lookup to get the IP address of the server. Then it sends a HTTP request to the server. The server responds with the resource.
- IP address is a 32 bit number. It is divided into 4 parts, each part is called an octet. Each octet is represented in decimal form. So the range of each octet is 0-255. So the range of IP address is
- Example IP address: 127.0.0.1 -> localhost ; 192.168.x.y -> private network ;
- A server listens to requests on specific ports. A port is a 16 bit number. So the range of ports is 0-65535. Some ports are reserved for specific services. For example, port 80 is reserved for HTTP service.
- Most clients know the port number based on Network Protocol. For example, HTTP uses port 80, HTTPS uses port 443, SSH uses port 22 etc.
