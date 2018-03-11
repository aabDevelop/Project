#include <iostream>

#include "ApiFunction.h"
#include "ApiClass.h"

int main(){
	std::cout<<"start work"<<std::endl;
	std::cout<<"=============================================="<<std::endl;
	std::cout<<"call apiFunction(10,20) = "<<apiFunction(10,20)<<std::endl;
	std::cout<<"call apiFunction(30,40) = "<<apiFunction(30,40)<<std::endl;

	std::cout<<"=============================================="<<std::endl;
	ApiClass ac01;
	std::cout<<"call ac01.method(30) = "<<ac01.method(30)<<std::endl;
	std::cout<<"call ac01.method(40) = "<<ac01.method(40)<<std::endl;

	std::cout<<"=============================================="<<std::endl;
	ApiClass ac02(10);
	std::cout<<"call ac02.method(30) = "<<ac02.method(30)<<std::endl;
	std::cout<<"call ac02.method(40) = "<<ac02.method(40)<<std::endl;

}
