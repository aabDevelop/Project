FOLDER_EXECUTABLE = bin/
EXECUTABLE_NAME = Project.exe

EXECUTABLE = $(FOLDER_EXECUTABLE)$(EXECUTABLE_NAME)
FOLDERS = bin bin/src bin/src/api bin/src/user
SOURSES = src/user/main.cpp src/api/ApiClass.cpp src/api/ApiFunction.cpp

CC = g++

CFLAGS = -c -Wall -Isrc/helper -Isrc/api 
LDFLAGS = 
OBJECTS = $(SOURSES:.cpp=.o)

OBJECTS_PATH = $(addprefix $(FOLDER_EXECUTABLE),$(OBJECTS))


#--------------------------------

all: $(SOURSES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)	
	$(CC) $(LDLAGS) $(OBJECTS_PATH) -o $@
	
.cpp.o:
	mkdir -p $(FOLDERS)
	$(CC) $(CFLAGS) $< -o $(FOLDER_EXECUTABLE)$@


clean:
	rm -rf $(OBJECTS) $(EXECUTABLE) 
