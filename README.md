# log-watching-solution
I recently had an interview at BrowserStack. The first round was Machine coding.
My problem statement for the same was
"
The first problem requires you to implement a log watching solution (similar to the tail -f command in UNIX). However, in this case, the log file is hosted on a remote machine (the same machine as your server code).

You have to implement the following:
A server-side program to monitor the given log file and capable of streaming updates that happen in it. This will run on the same machine as the log file.
A web-based client (accessible via URL like http://localhost/log) that prints the updates in the file as and when they happen and NOT upon page refresh. The page should be loaded once and it should keep getting updated in real-time. The user sees the last 10 lines in the file when he lands on the page.
The server should not retransmit the entire file every time. It should only send the updates. You may implement the server in any programming language. You may not, however, use off-the-shelf libraries or tools that provide tail-like functionalities. The server should be able to handle multiple clients at the same time.

We will be evaluating you for code quality, testability, modularity, corner cases, etc.


Technical Specifications:
This problem consists of two parts,
transmitting the updates to the users browser.
monitoring and reading the file

Transmitting the updates to the users browser
There are two broad approaches,
the client polls the server for updates
the server pushes updates to the clients
Since we have to be as real-time as possible we'll go with the second approach.
You will need to implement Websockets and integrate them with the second part of the problem.

For file reading and monitoring
We are not allowed to use any third-party libraries for this bit."

Read the modified time of the file -> last_modified
Seek to the end of the file and save the position -> last_read_position
keep reading the file backward till you find 10 new line characters, you now have the last 10 lines of the file, and send it to the user over the WebSocket connection.
Keep polling the modified time of the file, if it is changed
if it's changed seek to last_read_position and read till the end of the file and send the data to the user via WebSocket.
Save the new end of the file as last_read_position
save the new last_modified and go to 4

I implemented a solution in python using async.io library and cleared this round and was invited for the interview with one of the senior directors.
Unfortunately I could not clear the interview round but had an amazing experience at Browserstack.
