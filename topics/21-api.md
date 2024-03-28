# API (Application Programming Interface)
Is a set of routines and standards (contracts) specific to an application, so that other applications can use the functionalities of that application.

### Why use an API?
In recent years, the Internet has transformed from a network of web servers that served mostly static pages to web browsers...
![over_net](/imgs/api/over_net.png)

...in a client-server architecture, where web and mobile applications communicate with different applications, increasingly through simple but powerful RESTful APIs.

![over_net2](/imgs/api/over_net_2.png)

### The rules of the game
Basically, an API is a contract that defines how one application will communicate with another. How data will be sent and received.
![api_arch](/imgs/api/api_architecture.png)

### What is a REST API?
REST is an acronym for `REpresentational STATE Transfer`, which is an architectural style for distributed systems.

### How to communicate with her?
- Our protocol (e.g. https)
- Our server has an address (ex: pokeapi.co)
- Our server has a port (ex: 8080 for http and 443 for https)
- And we need to access a resource or as we usually call it, endpoint or route (ex: /api/character)
```url
https://pokeapi.co/api/v2/pokemon/15
```

### Our verbs
The **HTTP protocol is the basis used behind REST APIs and "requests" them using several "types".** The most common are:
- `POST`: (Create) Create a resource
- `GET`: (Read) Get a resource
- `PUT`: (Update) Update a resource
- `DELETE`: Remove a resource

### Types of APIs
**1. RESTful APIs:** Representational State Transfer (REST) APIs adhere to the principles of REST architecture. They use HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources, often returning data in JSON or XML format.

**2. SOAP APIs:** Simple Object Access Protocol (SOAP) APIs use XML-based messaging protocol for exchanging structured information in a decentralized, distributed environment. They are typically used in enterprise-level applications.

**3. GraphQL APIs:** GraphQL is a query language for APIs and a runtime for executing those queries by using a type system you define for your data. It enables clients to request only the data they need, reducing over-fetching and under-fetching of data.

**4. Webhooks:** Webhooks are user-defined HTTP callbacks that are triggered by specific events. They enable real-time communication between systems by notifying external services when certain events occur.

**5. WebSocket APIs:** WebSocket is a communication protocol that provides full-duplex communication channels over a single TCP connection. WebSocket APIs enable bidirectional, real-time communication between clients and servers.

**6. Public APIs:** Public APIs are exposed by organizations to external developers and third-party vendors. They allow developers to access certain features or data of a service or platform, often with usage restrictions and authentication requirements.

**7. Private APIs:** Private APIs are intended for internal use within an organization or by selected partners. They are not exposed to the public and may provide access to sensitive data or functionality.

**8. Partner APIs:** Partner APIs are similar to private APIs but are shared with trusted partners or affiliates to enable collaboration or integration between organizations.

**9. Open APIs:** Open APIs, also known as open web APIs or external APIs, are publicly available APIs that can be accessed and used by any developer. They are typically well-documented and do not require special permission for access.

**10. Internal APIs:** Internal APIs are used for communication between different components or services within an organization's infrastructure. They facilitate modularity, scalability, and maintainability of complex systems.


### What is the difference between REST and RESTful?
REST is an architectural style for distributed systems, while RESTful is the implementation of that style.