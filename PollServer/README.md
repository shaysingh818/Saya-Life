# Gateway Server
Gateway communicates with all the meters. Server needs to get the reports from these gateways and keep a persistent connection with them. 

# Features

##  HTTP LONG POOLING
1. Client polls the server requesting new information.  The server holds the request open until new data is available. Once available, the server responds and sends the new information. When the client receives the new information, it immediately sends another request, and the operation is repeated. This effectively emulates a server push feature.  
 
	* As usage grows, how will you orchestrate your realtime backend?
	* When mobile devices rapidly switch between WiFi and cellular networks or lose connections, and the IP address changes, does long polling automatically re-establish connections?
	* With long polling, can you manage the message queue and catch up missed messages?
	* Does long polling provide load balancing or failover support across multiple servers?


2. Features to consider

	* Presence – Detect when users enter/leave your app and whether machines are online, for applications like in-app chat.
	* Storage & Playback – Store realtime message streams for future retrieval and playback.
	* Mobile Push Gateway – Manage the complexities of realtime apps on mobile devices, including Push Notifications.
	* Analytics – Leverage visualizations into your realtime data streams.	

## NANOMSG ~ socket library

1. nanomsg is a socket library that provides several common communication patterns. It aims to make the networking layer fast, scalable, and easy to use. Implemented in C, it works on a wide range of operating systems with no further dependencies.

2. The communication patterns, also called "scalability protocols", are basic blocks for building distributed systems. By combining them you can create a vast array of distributed applications. The following scalability protocols are currently available:

	* PAIR - simple one-to-one communication
	* BUS - simple many-to-many communication
	* REQREP - allows to build clusters of stateless services to process user requests
	* PUBSUB - distributes messages to large sets of interested subscribers
	* PIPELINE - aggregates messages from multiple sources and load balances them among many destinations
	* SURVEY - allows to query state of multiple applications in a single go	
3. Scalability protocols are layered on top of the transport layer in the network stack. At the moment, the nanomsg library supports the following transports mechanisms:

	* INPROC - transport within a process (between threads, modules etc.)
	* IPC - transport between processes on a single machine
	* TCP - network transport via TCP
	* WS - websockets over TCP

1.) Need to figure out a way to manage DEAD connections
2.) Find a way to use nanomsg to send reports
	





