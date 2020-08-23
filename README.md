# pi-mfrc522

Project to read rfid tags using raspberry pi 3 and rfid read RC522.

This project was based on this tutorial: https://pimylifeup.com/raspberry-pi-rfid-rc522/

In this project, I use 3 separated process in the boot of raspberry.

. API process
. Reader process
. Writer process

# API process

The API process hosts an api to an external devices read/write the rfid tag. There are specifics routes to each process. The route /write_tags is a POST request that write the received data to the tag while the tag is being read by the antemn. The route /read_tag is a GET request that reads the text from the current tag. Each route requires a specific process to be running, this processes are Reader and Writer, respectively.

# Reader Process

The Reader process is a process that keeps reading the antemn results and show the tag text value in a display LCD. If there's not tag close to the antemn, it shows the network IP.

# Writer Process

The Writer process is a process that keeps waiting a value to write to the current tag. This process is used in the write_tag route.
