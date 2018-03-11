#include "ApiClass.h"
#include <iostream>

ApiClass::ApiClass():value(0) {
	std::cout<<std::endl<<"create ApiClass value = "<<value<<std::endl;
}
ApiClass::ApiClass(int startValue):
		value(startValue){
	std::cout<<std::endl<<"create ApiClass value = "<<value<<std::endl;
}

ApiClass::~ApiClass() {
	std::cout<<std::endl<<"delete ApiClass"<<std::endl;
}

int ApiClass::method(int vl){
	value +=vl;
	return value;
}

