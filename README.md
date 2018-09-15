# Windtunnel
A python program, that runs on AWS EC2, that updates a graph on a S3 Site
	S3 Hosts an upload page, to upload the excel document with data. THIS MUST BE CALLED File.xlsx
	Python Program converts a excel document with controls and test values, into a graph
	The python program then uploads this graph to S3
	S3 hosts the home page, displaying the graph.
